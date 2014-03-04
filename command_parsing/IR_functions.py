#!/usr/bin/env python

"""Functions to analyse IR packets"""

__author__      = "Petr Klus"
__copyright__   = "None really"


import matplotlib.pyplot as plt
import numpy as np
import re

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
    pieces = [m.start() for m in re.finditer('11100010', ircom_bin)]

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




