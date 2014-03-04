#!/usr/bin/env python

"""Putting it all together + analysis"""

__author__      = "Petr Klus"
__copyright__   = "None really"


from IR_functions import *
from IR_captured import *


plot_signal([cap.ir_24_3_COOL, cap.ir_24_3_HEAT])

# output for copy&paste to arduino code for testing
print print_arduino(cap.ir_24_3_COOL, "autoSun25")


plot_signal([ir_24_3_COOL, ir_24_3_HEAT, ir_24_3_FAN, ir_24_3_AUTO, ir_24_3_DEHUM])

# packet start
# 0x11100010
# separator between triplets of commands
command_end = "11110"
split_into_command_strings(translate_to_binary_str(ir_24_3_AUTO))

# comparison
print generate_pulses(x)[10:20]
print ir_24_3_COOL[10:20]

# see total pulse length and individual lenghts
# also make sure we realise that reference is at the bottom :)
plot_signal([ir_24_3_COOL, generate_pulses(translate_to_binary_str(ir_24_3_COOL))])


# leftoff here
auto_fan_command = generate_pulses(translate_to_binary_str(ir_24_3_COOL))
print_arduino(auto_fan_command, "cool24_fan3")


