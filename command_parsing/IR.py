#!/usr/bin/env python

"""Putting it all together + analysis"""

__author__      = "Petr Klus"
__copyright__   = "None really"


from IR_functions import *
from IR_captured import *


plot_signal([ir_24_3_COOL, ir_24_3_HEAT])

# output for copy&paste to arduino code for testing
print print_arduino(cap.ir_24_3_COOL, "autoSun25")


plot_signal([ir_24_3_COOL, ir_24_3_HEAT, ir_24_3_FAN, ir_24_3_AUTO, ir_24_3_DEHUM])
plot_signal([irT_29_3_HEAT, ir_24_3_HEAT])


# packet start
# 0x11100010
# separator between triplets of commands
command_end = "11110"
split_into_command_strings(translate_to_binary_str(ir_24_3_AUTO))
split_into_command_strings(translate_to_binary_str(irT_29_3_HEAT))

# comparison
print generate_pulses(x)[10:20]
print ir_24_3_COOL[10:20]

# see total pulse length and individual lenghts
# also make sure we realise that reference is at the bottom :)
plot_signal([ir_24_3_COOL, generate_pulses(translate_to_binary_str(ir_24_3_COOL))])


# leftoff here
auto_fan_command = generate_pulses(translate_to_binary_str(ir_24_3_COOL))
print_arduino(auto_fan_command, "cool24_fan3")



# encode into ascii
import itertools
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


def translate_print_first(label, ircom):
    ircom_bin = translate_to_binary_str(ircom)
    print map(bin_to_ascii, split_into_command_strings(ircom_bin))[0], label

    

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

for label, ircom in analyse_titles:
    translate_print_first(label, ircom)

# print 
# ircom_bin = translate_to_binary_str()
# print "\n".join(map(bin_to_ascii, split_into_command_strings(ircom_bin)))













