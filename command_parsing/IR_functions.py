#!/usr/bin/env python

"""Functions to analyse IR packets"""

__author__      = "Petr Klus"
__copyright__   = "None really"


import matplotlib.pyplot as plt
import numpy as np
import re
import itertools
from termcolor import colored

tick_size = 100

def print_arduino(ircom, varname="test"):
    out = "int {}[] = ".format(varname) + "{"
    parts = []
    for seq in ircom:
        on, off = seq
        parts.append("{}, {}".format(on, off))
    out+=", ".join(parts) + "};"
    return out


def find_gap_index(array, min_gap_size=500):    
    # known issue - significant gap not always present
    for index, element in enumerate(array):
        on, off = element
        if off > min_gap_size:
            return index
    return False

def split_signal(ircom):
    # TODO - include gap
    gap_index = find_gap_index(ircom)
    if gap_index:
        return ircom[:gap_index], ircom[gap_index+1:]
    else:
        return ircom, []


def create_curve(test, tst=1):
    # build_curve from intervals for plotting
    curve = []
    for entry in test:
        on, off = entry
        curve += [tst] * on
        zero = 0.1 if tst ==1 else -0.1
        curve += [zero] * off
    return curve


def plot_signal(ircoms):  
      
    def plot_diff(curve1, curve2, offset):
        a = np.array(curve1)
        b = np.array(curve2)
        if len(a) < len(b):
            c = b.copy()
            c[:len(a)] += a
        else:
            c = a.copy()
            c[:len(b)] += b
    
        allowed_delta = 10
        last_zero = 0
        for i in range(len(c)):
            cur_el = c[i]
            if cur_el == 0:
                if i - last_zero < allowed_delta:
                    # remove gap
                    for j in xrange(last_zero, i):
                        c[j] = 0
                last_zero = i            
        plt.plot(c + offset)
        return c
    
    curves = []
    for index, ircom in enumerate(ircoms):    
        offset = 2.5*index
        part1, part2 = split_signal(ircom)    
        curve1 = create_curve(part1)
        plt.plot(np.array(curve1) + offset)
        if part2:
            curve2 = create_curve(part2, tst=-1)  
            plt.plot(np.array(curve2) + offset)
        else:        
            curve2 = create_curve(part1, tst=-1)        
            plt.plot(np.array(curve2) + offset, ls="--")            
        curves.append(curve1)
        curves.append(curve2)
        plot_diff(curve1, curve2, offset)

    
    ret = plot_diff(curves[0], np.array(curves[2])*(-1), -6)    
    # plt.ylim(-0.2, 0.2 + 2*len(ircoms))
    plt.show()
    return ret

# packet start
# 0x11100010

def analyse_pulses(ircom):
    # analyse "pulse" length
    crest_distances = []
    cur_t = 0
    for item in ircom:
        on, off = item
        next_on = on+off
        crest_distances.append(next_on)

    tot_pulse_length = np.mean(filter(lambda x: x < 200, crest_distances))/2

    # there is a slight delay in creating the "1" vs gap
    pulse_lengths = np.array(filter(lambda el: el[0]<100 and el[1]<100, ircom)).mean(0)
    print "Total pulse length (mean):", tot_pulse_length
    print "Individual pulse lengths (pos, neg):", pulse_lengths[0], pulse_lengths[1]


def translate_to_binary_str(ircom):
    approx_pulses = lambda num: int(round(num/100.0))
    signal = ""
    for el in ircom:
        on, off = el
        signal += "".join(["1"]* approx_pulses(on))
        signal += "".join(["0"]* approx_pulses(off))
    return signal


# separator between triplets of commands
command_end = "11110"
def split_into_command_strings(ircom_bin):
    # get parts by detecting signal start    
    if ircom_bin.startswith('11100010'):
        # normal command
        split_part = '11100010'
    elif ircom_bin.startswith('11100001'):
        # toggle command
        split_part = '11100001'
    else:
        raise Exception("Invalid command start")
    pieces = [m.start() for m in re.finditer(split_part, ircom_bin)]

    command_ranges = zip(pieces, pieces[1:]) + [(pieces[-1], len(ircom_bin))]
    command_strings = [ircom_bin[start:end] for start, end in command_ranges] #end is not inclusive
    return command_strings


# values measured & tweaked using visualisation function
def generate_pulses(ircom_bin, total_pulse_length=93.66, individual_lengths=(88.1, 91.8)):
    # always start in 0
    cur_state = 0
    pulses = []
    pos_diff = individual_lengths[1] - individual_lengths[0]
    for i, el in enumerate(ircom_bin):
        if cur_state >= 0 and el == "1":
            cur_state +=1
        elif cur_state <= 0 and el == "0":
            cur_state -=1
        else:            
            if cur_state > 0:                
                pulses.append(int(total_pulse_length * abs(cur_state)-pos_diff))
            else:
                pulses.append(int(total_pulse_length * abs(cur_state)+pos_diff))
            if el == "1":
                cur_state = 1
            else:
                cur_state = -1
    # last element
    if cur_state > 0:                
        pulses.append(int(total_pulse_length * abs(cur_state)-pos_diff))
    else:
        pulses.append(int(total_pulse_length * abs(cur_state)+pos_diff))
    pulses.append(0)
    
    return zip(pulses[::2], pulses[1::2])




# encode into ascii
def bin_to_ascii(ones_zeros, char_offset=97):
    """Use on split commands
    NOTE - ENDs of splits are padded, therefore can introduce erroneous gaps
    """
    # http://docs.python.org/3.1/library/itertools.html#recipes
    def grouper(n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return itertools.izip_longest(*args, fillvalue=fillvalue)
    
    out = ""
    for quadruple in grouper(4, ones_zeros, "0"):    
         out += chr(int('0b{}'.format("".join(quadruple)), 2)+char_offset)
    return out

# TODO highlight
def translate_print_first(label, ircom, print_binary=False, highlight=(0, 0)):
    ircom_bin = translate_to_binary_str(ircom)
    
    def assign_colour((index, x)):
        h_start, h_end = highlight
        h_col = "on_yellow" if index >= h_start and index < h_end else "on_grey"
        if x == "1":
            return colored("1", "blue", h_col)
        else:
            return colored("0", "red", h_col)
    
    if print_binary:
        first_line = split_into_command_strings(ircom_bin)[0]
        line = "".join(
            map(
                assign_colour, 
                enumerate(first_line)
            )
        )
        print line, label
    else:
        print map(bin_to_ascii, split_into_command_strings(ircom_bin))[0], label

def construct_command_part(temperature, mode, fan_speed, power_toggle):    
    """Constructs command"""

    # failsafe checks
    if mode == "DEHUM" and fan_speed > 1:
        raise Exception("Invalid mode - DEHUM can only have fan speed of 1")      

    temperatures = {
        16 : "10101001",
        17 : "10100110",
        18 : "10100101",
        19 : "10011010",
        20 : "10011001",
        21 : "10010110",
        22 : "10010101",
        23 : "01101010",
        24 : "01101001",
        25 : "01100110",
        26 : "01100101",
        27 : "01011010",
        28 : "01011001",
        29 : "01010110",
        30 : "01010101"
    }
    
    modes = {
        "HEAT":    "100110",
        "COOL":    "101001",
        "AUTO":    "100101",
        "FAN" :    "011001",
        "DEHUM":   "011010"
    } 
    
    fan_speeds = {
        1: "1010",
        2: "1001",
        3: "0110",
        4: "0101",
    }
    
    power_toggles = {
        True: "01",
        False: "10",
    }
    
    start_pad = "111000"
    second_pad = "1010101010"
    third_pad = "10101010101010101010101010101010100110"
    
    command_part = "{}{}{}{}{}{}{}".format(
        start_pad,
        power_toggles[power_toggle],        
        modes[mode],
        fan_speeds[fan_speed],
        second_pad,
        temperatures[temperature],
        third_pad
    )
    return command_part
    

def construct_full_command(temperature=16, mode="HEAT", fan_speed=4,power_toggle=False):
    command_third = construct_command_part(temperature, mode, fan_speed, power_toggle)
    full_command = "{}{}{}1111".format(*([command_third] * 3))
    return full_command


def arduino_flat_array(ircom_bin):
    pulses = generate_pulses(ircom_bin)
    pulses_flat = []
    for (on, off) in pulses:
        pulses_flat+= [on, off]
    return pulses_flat
