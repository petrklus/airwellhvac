#!/usr/bin/env python

"""Putting it all together + analysis"""

__author__      = "Petr Klus"
__copyright__   = "None really"


from IR_functions import *
from IR_captured import *

# plot sample packet
plot_signal(get_ir())

fetch_analyses = [
    (16, "HEAT",    1),
    (16, "COOL",    1),   
    (16, "AUTO",    1),        
    (16, "FAN",     1),
    (16, 'DEHUM',   1)
]

for query in fetch_analyses:
    ircoms = get_ir(*query)
    label = ", ".join(map(str,query))
    translate_print_first(label, ircoms[0], print_binary=True)

# packet structure
# start




split_into_command_strings(translate_to_binary_str(ir_24_3_AUTO))
split_into_command_strings(translate_to_binary_str(irT_29_3_HEAT))


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













