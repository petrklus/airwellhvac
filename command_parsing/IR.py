#!/usr/bin/env python

"""Putting it all together + analysis"""

__author__      = "Petr Klus"
__copyright__   = "None really"


from IR_functions import *
from IR_captured import *

# plot sample packet
plot_signal(get_ir())

def visualise(fetch_analyses, highlight=(28,36)):
    print "".join([str(num/10) if num%10 == 0 else "-" for num in range(80)])
    print "".join(map(str, range(10) * 8))
    for query in fetch_analyses:
        ircoms = get_ir(*query)
        label = ", ".join(map(str,query))    
        translate_print_first(label, ircoms[0], print_binary=True, highlight=highlight)
    
##
# highlight&compare modes
fetch_analyses = [
    (16, "HEAT",    1),
    (16, "COOL",    1),   
    (16, "AUTO",    1),        
    (16, "FAN",     1),
    (16, 'DEHUM',   1)
]
visualise(fetch_analyses, highlight=(8, 14))

##
# highlight&compare fan speeds
fetch_analyses = [
    (16, 'COOL',    1),
    (16, "HEAT",    1),
    (16, "HEAT",    2),   
    (16, "HEAT",    3),        
    (16, "HEAT",    4),
]
visualise(fetch_analyses, highlight=(14, 19))

# temperature
fetch_analyses = [(temp, "HEAT", 4) for temp in range(16,31)]
visualise(fetch_analyses)

# power state
fetch_analyses = [
    (30, 'HEAT', 4, True),
    (30, 'HEAT', 4, False),
    (21, 'FAN', 4, True),
    (21, 'FAN', 4, False),
]
visualise(fetch_analyses, highlight=(0, 8))



# packet structure
# 0-7   :   8 bits start - 11100010 normal, TODO power toggle
# 8-13  :   6 bits mode (may include flap orientation?)
# 14-18 :   4 bits fan speed
# 19-27 :   padding? 010101010
# 28-35 :   8 bits temperature
# 36-70 :   padding?


split_into_command_strings(translate_to_binary_str(ir_24_3_AUTO))
split_into_command_strings(translate_to_binary_str(irT_29_3_HEAT))

def construct_command(temperature=16, mode="HEAT", fan_speed=4,power_toggle=False):
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
        1: "10101",
        2: "10011",
        3: "01101",
        4: "01011",
    }
    
    power_toggles = {
        True: "01",
        False: "10",
    }
    
    command_part = "111000{}{}010110101010100101010110101010101010101010101010101010100110".format(
        power_toggles[power_toggle],        
        modes[mode]
    )
        
    

visualise(records.keys(), highlight=(6, 8))    
    
    
    


plot_signal([ir_24_3_COOL, ir_24_3_HEAT])


# output for copy&paste to arduino code for testing
print print_arduino(cap.ir_24_3_COOL, "autoSun25")


plot_signal([ir_24_3_COOL, ir_24_3_HEAT, ir_24_3_FAN, ir_24_3_AUTO, ir_24_3_DEHUM])
plot_signal([irT_29_3_HEAT, ir_24_3_HEAT])


# packet start
# 0x11100010
# separator between triplets of commands
command_end = "11110"


# comparison
print generate_pulses(x)[10:20]
print ir_24_3_COOL[10:20]

# see total pulse length and individual lenghts
# also make sure we realise that reference is at the bottom :)
plot_signal([ir_24_3_COOL, generate_pulses(translate_to_binary_str(ir_24_3_COOL))])


# leftoff here
auto_fan_command = generate_pulses(translate_to_binary_str(ir_24_3_COOL))
print_arduino(auto_fan_command, "cool24_fan3")


    

analyse_titles = [
    # fans are auto here
    ("Normal heat 24C", ir_24_3_HEAT),
    ("Normal cool 24C", ir_24_3_COOL),
    ("Normal auto 24C", ir_24_3_AUTO),
    ("Normal dehum 24C", ir_24_3_DEHUM),
    ("Normal fan 24C", ir_24_3_FAN),
    ("25C, fan 1, heat", ir_a),
    ("25C, fan2, heat", ir_b),
    ("25C, fan3, heat", ir_c),
    ("Toggle heat 29C", irT_29_3_HEAT)
]


# print 
# ircom_bin = translate_to_binary_str()
# print "\n".join(map(bin_to_ascii, split_into_command_strings(ircom_bin)))













