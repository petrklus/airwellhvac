#!/usr/bin/env python

"""Captured IR packets"""

__author__      = "Petr Klus"
__copyright__   = "None really"


# 29C, fan 3
ircom = [[294, 278], [88, 100], [88, 190], [186, 182], [186, 104], [84, 100], [88, 94], [84, 102], [88, 100], [88, 190], [88, 90], [96, 94], [184, 104], [84, 94], [86, 100], [88, 100], [88, 100], [88, 94], [84, 100], [88, 100], [88, 104], [84, 94], [84, 102], [88, 100], [88, 100], [88, 94], [84, 100], [88, 100], [88, 100], [88, 180], [188, 102], [292, 280], [88, 100], [88, 190], [186, 180], [186, 104], [84, 100], [88, 94], [86, 100], [88, 100], [88, 190], [88, 90], [98, 94], [184, 102], [86, 94], [84, 100], [88, 100], [88, 100], [88, 94], [84, 100], [88, 100], [88, 102], [86, 96], [84, 100], [88, 100], [88, 100], [88, 94], [86, 98], [88, 100], [88, 100], [88, 182], [186, 102], [292, 280], [88, 100], [88, 190], [186, 180], [188, 102], [86, 100], [88, 94], [84, 104], [84, 104], [84, 190], [88, 94], [94, 94], [184, 104], [84, 94], [84, 100], [88, 104], [84, 104], [84, 94], [86, 102], [86, 102], [86, 102], [88, 92], [86, 102], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 178], [190, 100], [384, 4920], [298, 276], [88, 104], [84, 190], [188, 182], [186, 102], [86, 102], [86, 92], [88, 100], [88, 100], [88, 186], [92, 90], [98, 90], [188, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 178], [190, 100], [294, 276], [92, 100], [88, 186], [190, 182], [186, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 188], [90, 92], [96, 92], [186, 102], [86, 92], [86, 102], [86, 100], [88, 100], [88, 92], [88, 100], [86, 102], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [86, 178], [190, 104], [290, 278], [90, 100], [88, 188], [188, 182], [186, 104], [84, 100], [88, 92], [86, 102], [86, 102], [88, 186], [90, 92], [96, 92], [186, 104], [84, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 100], [90, 98], [90, 90], [90, 98], [90, 98], [90, 98], [90, 176], [188, 104], [380, 0]]



# ONOFF 29C fan 3
irT_29_3_HEAT = [[294, 370], [186, 194], [184, 180], [186, 104], [84, 104], [84, 94], [86, 102], [86, 102], [84, 192], [88, 90], [98, 94], [184, 102], [84, 96], [84, 102], [86, 102], [86, 102], [84, 96], [84, 104], [86, 102], [84, 104], [84, 94], [86, 102], [86, 102], [86, 102], [86, 94], [84, 104], [84, 104], [84, 104], [84, 180], [188, 102], [292, 370], [186, 192], [184, 184], [184, 104], [84, 104], [84, 94], [86, 102], [84, 104], [84, 190], [88, 94], [94, 94], [184, 104], [84, 94], [84, 104], [86, 102], [86, 102], [86, 94], [84, 104], [84, 102], [86, 102], [86, 94], [84, 104], [84, 104], [86, 102], [84, 94], [86, 102], [86, 102], [86, 102], [84, 182], [186, 104], [292, 368], [186, 194], [184, 184], [184, 102], [86, 102], [84, 96], [84, 102], [86, 104], [84, 190], [88, 94], [94, 94], [184, 102], [86, 94], [84, 104], [84, 104], [84, 104], [84, 94], [84, 104], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 178], [188, 104], [380, 0]]


# 25C, fan auto, sun
ircoms = [
    [[296, 278], [88, 100], [88, 190], [186, 182], [96, 92], [186, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 190], [186, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 98], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [186, 180], [98, 90], [186, 102], [86, 92], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [86, 102], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [296, 280], [88, 100], [88, 188], [188, 180], [96, 92], [186, 100], [88, 92], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 100], [88, 182], [186, 100], [384, 6056], [294, 280], [86, 102], [86, 190], [186, 182], [98, 90], [188, 98], [88, 92], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [186, 182], [96, 92], [186, 100], [88, 90], [90, 98], [88, 100], [90, 188], [178, 190], [186, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [88, 190], [186, 180], [98, 90], [186, 102], [86, 92], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [86, 102], [86, 100], [88, 100], [90, 90], [86, 102], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 180], [186, 100], [384, 0]],
    [[294, 280], [88, 100], [88, 190], [186, 182], [96, 92], [186, 100], [88, 92], [88, 98], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [86, 190], [188, 180], [98, 90], [188, 100], [88, 90], [88, 100], [88, 100], [88, 190], [176, 192], [186, 100], [88, 90], [88, 100], [88, 100], [88, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 98], [88, 100], [90, 180], [186, 100], [294, 280], [88, 100], [88, 190], [188, 180], [96, 92], [186, 100], [88, 90], [90, 100], [86, 102], [86, 190], [178, 190], [186, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [384, 5508], [294, 278], [88, 100], [88, 190], [186, 182], [98, 90], [186, 100], [88, 92], [88, 100], [88, 100], [86, 192], [176, 190], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [186, 182], [96, 90], [188, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [296, 278], [88, 100], [88, 190], [188, 180], [96, 92], [186, 100], [88, 92], [88, 100], [88, 100], [88, 190], [178, 188], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [90, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 182], [186, 100], [384, 0]]
]

# 25C, fan 1, sun
ir_a = [[294, 280], [86, 102], [88, 190], [186, 90], [90, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [178, 188], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [90, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 102], [88, 98], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [186, 92], [86, 102], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 180], [188, 98], [294, 280], [88, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [86, 102], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [384, 6512], [294, 280], [88, 100], [88, 190], [186, 92], [86, 102], [86, 100], [90, 98], [90, 90], [88, 100], [88, 100], [88, 190], [176, 190], [188, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 180], [186, 100], [294, 280], [88, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [86, 102], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [294, 280], [86, 102], [86, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 100], [88, 192], [178, 188], [188, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [384, 0]]

# 25C, fan2, sun
ir_b = [[294, 280], [88, 100], [88, 188], [188, 90], [88, 190], [186, 100], [88, 92], [88, 100], [88, 100], [88, 190], [178, 188], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [188, 90], [88, 190], [186, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 278], [88, 100], [90, 188], [188, 90], [88, 190], [188, 98], [88, 92], [88, 100], [88, 100], [88, 190], [176, 190], [188, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 100], [86, 102], [86, 100], [90, 180], [186, 100], [384, 6360], [296, 278], [88, 100], [88, 190], [186, 92], [88, 190], [186, 100], [88, 92], [88, 100], [88, 98], [90, 188], [178, 190], [186, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 98], [90, 90], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [294, 280], [88, 100], [88, 190], [186, 90], [88, 190], [188, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 90], [88, 100], [88, 100], [90, 98], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 182], [186, 100], [296, 278], [88, 100], [88, 190], [188, 90], [88, 190], [186, 100], [88, 92], [88, 100], [86, 100], [90, 190], [176, 190], [188, 98], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [188, 98], [386, 0]]

# 25C, fan3, sun
ir_c = [[294, 278], [88, 100], [88, 190], [188, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [178, 188], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [90, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [90, 98], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [186, 180], [188, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [86, 102], [86, 190], [188, 180], [188, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [90, 98], [88, 100], [88, 182], [186, 100], [384, 6486], [294, 280], [88, 100], [88, 190], [186, 180], [188, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [86, 102], [88, 100], [88, 98], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [90, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 98], [88, 190], [186, 182], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 190], [186, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 102], [86, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [90, 180], [186, 100], [294, 280], [88, 100], [88, 190], [186, 182], [186, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [384, 0]]

# 16C, fan auto, mode "fan"
ircom = [[296, 280], [88, 188], [188, 188], [180, 98], [88, 100], [90, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 92], [86, 102], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [86, 192], [186, 190], [178, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 190], [186, 190], [178, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 100], [88, 98], [88, 92], [88, 100], [88, 190], [186, 90], [90, 100], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 102], [88, 100], [88, 180], [186, 100], [384, 1856], [296, 278], [88, 190], [186, 190], [178, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [88, 92], [88, 100], [88, 190], [186, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 100], [86, 102], [86, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [86, 190], [188, 190], [178, 100], [86, 100], [88, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [90, 90], [88, 100], [88, 100], [90, 98], [90, 88], [90, 98], [90, 98], [92, 96], [92, 178], [188, 98], [296, 278], [90, 188], [190, 186], [180, 98], [90, 98], [90, 98], [90, 88], [92, 96], [90, 98], [92, 96], [92, 88], [90, 98], [90, 186], [190, 88], [92, 96], [90, 98], [92, 96], [92, 88], [90, 98], [90, 98], [90, 98], [90, 88], [90, 98], [90, 98], [90, 98], [90, 88], [92, 98], [90, 98], [90, 96], [92, 178], [190, 96], [388, 0]]

ircom = [[294, 280], [86, 102], [86, 190], [188, 180], [98, 94], [182, 104], [84, 94], [86, 100], [88, 100], [88, 100], [88, 180], [98, 90], [98, 90], [186, 92], [88, 102], [86, 102], [86, 102], [86, 92], [86, 104], [84, 104], [84, 104], [84, 92], [88, 102], [86, 102], [86, 102], [86, 90], [88, 104], [84, 104], [84, 104], [84, 182], [186, 100], [294, 280], [88, 102], [86, 190], [186, 182], [96, 90], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [96, 92], [96, 90], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 102], [86, 182], [190, 96], [298, 276], [92, 96], [90, 188], [190, 178], [98, 90], [190, 96], [90, 88], [92, 98], [90, 98], [90, 98], [90, 178], [98, 90], [98, 90], [188, 90], [90, 98], [90, 98], [90, 98], [90, 90], [88, 98], [90, 98], [92, 96], [90, 92], [88, 96], [92, 96], [92, 96], [90, 92], [88, 98], [90, 98], [90, 98], [90, 178], [190, 96], [388, 1314], [298, 276], [90, 98], [90, 188], [190, 178], [98, 90], [188, 98], [90, 90], [90, 96], [92, 96], [92, 96], [92, 178], [98, 90], [98, 88], [190, 90], [90, 98], [88, 98], [92, 96], [92, 88], [90, 98], [90, 98], [90, 98], [90, 88], [92, 96], [92, 96], [90, 98], [90, 90], [90, 98], [90, 98], [90, 98], [90, 178], [190, 96], [298, 276], [92, 96], [92, 186], [190, 178], [100, 88], [190, 96], [92, 88], [90, 98], [90, 98], [90, 98], [90, 178], [100, 88], [100, 88], [188, 90], [90, 98], [90, 98], [90, 98], [90, 88], [92, 96], [90, 98], [90, 98], [90, 90], [90, 96], [92, 96], [92, 98], [90, 88], [90, 98], [90, 98], [90, 98], [90, 178], [190, 98], [296, 278], [90, 98], [90, 186], [190, 178], [100, 88], [190, 98], [90, 88], [90, 98], [90, 98], [90, 98], [92, 176], [100, 88], [100, 88], [190, 88], [90, 98], [90, 98], [90, 98], [92, 88], [90, 96], [92, 96], [92, 96], [90, 90], [90, 98], [90, 98], [90, 98], [90, 88], [92, 96], [90, 98], [90, 98], [90, 180], [188, 98], [386, 0]]


###
### differing operation modes
### 

# (24deg, cool,     fan3) 
ir_24_3_COOL = [[294, 280], [86, 102], [88, 100], [86, 190], [88, 92], [188, 98], [88, 100], [88, 92], [86, 102], [88, 100], [88, 188], [178, 102], [88, 188], [186, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 190], [88, 90], [188, 100], [86, 100], [90, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 188], [186, 92], [90, 98], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [90, 100], [86, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 190], [88, 90], [188, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [86, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 182], [186, 100], [384, 78], [296, 278], [88, 100], [88, 100], [88, 190], [88, 90], [188, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [90, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [86, 100], [90, 98], [88, 190], [88, 92], [186, 100], [88, 100], [88, 92], [86, 100], [88, 100], [90, 190], [176, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [86, 102], [88, 100], [88, 190], [86, 92], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 100], [90, 188], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 98], [90, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [384, 0]]

# (24deg, heat,     fan3) 
ir_24_3_HEAT = [[294, 280], [88, 100], [88, 190], [186, 182], [96, 90], [188, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 90], [88, 100], [88, 102], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 180], [188, 98], [296, 278], [88, 100], [88, 190], [188, 180], [96, 92], [186, 100], [88, 92], [86, 100], [90, 100], [88, 190], [176, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [90, 90], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [294, 280], [88, 100], [88, 190], [186, 180], [98, 90], [188, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [86, 192], [186, 92], [88, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 182], [186, 100], [384, 88], [294, 280], [88, 100], [88, 190], [186, 180], [98, 90], [188, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [86, 182], [186, 100], [296, 278], [88, 100], [88, 190], [188, 180], [96, 92], [186, 100], [88, 92], [88, 100], [86, 100], [90, 190], [176, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [186, 180], [98, 90], [186, 102], [86, 92], [88, 100], [88, 100], [88, 190], [178, 100], [86, 192], [186, 92], [86, 102], [86, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 182], [186, 100], [384, 0]]

# (24deg, fan,      fan3) 
ir_24_3_FAN = [[294, 280], [88, 190], [186, 190], [86, 92], [188, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 190], [178, 100], [86, 192], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 190], [186, 190], [88, 92], [186, 100], [88, 100], [88, 90], [88, 100], [88, 100], [90, 188], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [294, 280], [88, 188], [188, 190], [88, 90], [188, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 102], [88, 188], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 100], [86, 102], [86, 100], [90, 180], [186, 100], [384, 850], [296, 278], [88, 190], [186, 190], [88, 92], [186, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [294, 280], [88, 190], [186, 190], [88, 90], [188, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 102], [88, 188], [188, 90], [88, 100], [90, 98], [88, 100], [88, 92], [86, 102], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 100], [86, 102], [86, 100], [90, 180], [186, 100], [294, 280], [88, 190], [186, 190], [88, 92], [186, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 98], [386, 0]]

# (24deg, auto,     fan3) 
ir_24_3_AUTO = [[296, 278], [88, 100], [88, 190], [98, 90], [88, 92], [96, 92], [186, 100], [88, 90], [90, 100], [86, 100], [88, 190], [178, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [292, 282], [88, 100], [86, 190], [98, 90], [88, 92], [96, 92], [186, 100], [88, 92], [88, 100], [88, 100], [86, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [294, 280], [88, 100], [88, 190], [96, 90], [88, 92], [96, 92], [186, 100], [88, 92], [88, 100], [88, 100], [88, 188], [178, 102], [88, 188], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 102], [88, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [384, 52], [294, 278], [88, 102], [88, 188], [98, 90], [88, 92], [96, 92], [186, 100], [88, 92], [88, 100], [86, 102], [88, 188], [178, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [88, 190], [96, 90], [88, 92], [96, 92], [186, 100], [88, 92], [88, 100], [88, 100], [86, 192], [178, 100], [88, 188], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 190], [96, 92], [88, 90], [98, 90], [186, 102], [86, 92], [88, 100], [88, 100], [88, 190], [176, 102], [88, 188], [188, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [86, 102], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 100], [90, 180], [186, 100], [384, 0]]

# (24deg, dehum,    fan3) 
ir_24_3_DEHUM = [[294, 278], [88, 190], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 98], [90, 188], [178, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 188], [188, 100], [88, 90], [88, 100], [88, 100], [90, 98], [88, 92], [88, 100], [88, 100], [86, 190], [180, 98], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [90, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 190], [186, 100], [88, 90], [90, 100], [88, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 102], [88, 188], [188, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [86, 102], [88, 98], [90, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [90, 180], [186, 100], [384, 106], [294, 280], [86, 190], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [90, 100], [86, 190], [178, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 190], [186, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 100], [90, 188], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 190], [186, 100], [88, 92], [86, 100], [90, 98], [90, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 98], [90, 190], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 98], [88, 100], [88, 182], [186, 100], [386, 0]]

###
### clock setting - looks like it's all the same - no clock in the A/C unit?
###

# (24deg, cool, fan3) Clock set, 0:00 hours 
ir_t0000 = [[294, 282], [88, 98], [88, 100], [88, 100], [90, 180], [186, 100], [88, 100], [88, 92], [86, 100], [90, 98], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 98], [90, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [88, 100], [86, 100], [90, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 100], [90, 188], [186, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [90, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [90, 180], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [88, 100], [90, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 188], [188, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 100], [86, 100], [90, 180], [186, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 0:01 hours 
ir_t0001 = [[294, 280], [86, 102], [86, 100], [90, 100], [88, 180], [186, 100], [88, 100], [88, 92], [88, 100], [94, 94], [88, 190], [178, 98], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [90, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 102], [86, 192], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 98], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 182], [186, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 0:10 hours 
ir_t0010 = [[294, 280], [86, 100], [88, 100], [90, 100], [88, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 192], [176, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 100], [88, 192], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 102], [88, 100], [86, 182], [186, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 0:30 hours 
ir_t0030 = [[294, 280], [88, 100], [88, 100], [86, 102], [88, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 188], [178, 102], [88, 188], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 102], [88, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [86, 102], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 188], [188, 90], [88, 100], [90, 98], [88, 100], [88, 92], [88, 100], [86, 102], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 102], [88, 180], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 0:45 hours 
ir_t0045 = [[294, 278], [88, 100], [88, 100], [90, 100], [88, 180], [186, 100], [88, 100], [88, 90], [88, 100], [90, 100], [86, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 98], [90, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 98], [90, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 98], [88, 182], [186, 100], [384, 0]]

# short, no repeat
# (24deg, cool, fan3) Clock set, 1:00 hours 
ir_t0100 = [[294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 94], [86, 100], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [88, 180], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [88, 100], [88, 92], [86, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [294, 282], [88, 100], [88, 100], [86, 100], [88, 182], [186, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 188], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [90, 98], [90, 88], [90, 98], [92, 96], [90, 98], [90, 178], [190, 98], [386, 0]]
ir_t0100 = [[296, 278], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [86, 102], [88, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [294, 282], [88, 98], [88, 100], [88, 100], [88, 182], [186, 100], [88, 100], [88, 92], [86, 100], [90, 98], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 100], [90, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [86, 102], [86, 102], [88, 98], [88, 182], [186, 100], [88, 100], [88, 92], [88, 100], [86, 102], [86, 190], [178, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 2:00 hours 
ir_t0200 = [[294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [88, 102], [88, 90], [88, 100], [88, 100], [88, 190], [176, 100], [90, 190], [186, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 98], [88, 100], [88, 100], [90, 180], [186, 100], [296, 278], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 90], [88, 100], [90, 98], [90, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [90, 98], [88, 92], [88, 100], [88, 100], [86, 100], [90, 180], [186, 100], [296, 278], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [90, 98], [90, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 98], [386, 0]]


# (24deg, cool, fan3) Clock set, 4:00 hours 
ir_t0400 = [[294, 280], [86, 102], [88, 100], [88, 100], [86, 182], [188, 98], [88, 100], [88, 92], [88, 100], [88, 100], [88, 188], [178, 190], [188, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [86, 100], [90, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [86, 102], [86, 92], [88, 100], [88, 100], [88, 190], [176, 192], [186, 100], [88, 90], [88, 100], [90, 98], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [90, 100], [86, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [86, 102], [88, 90], [88, 100], [88, 100], [88, 190], [178, 190], [186, 100], [88, 92], [88, 100], [88, 100], [86, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [86, 182], [186, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 4:34 hours 
ir_t0434 = [[300, 274], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [90, 98], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [88, 180], [188, 98], [296, 278], [88, 100], [88, 100], [90, 98], [88, 182], [186, 100], [88, 100], [88, 92], [86, 102], [86, 100], [90, 188], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [90, 98], [88, 100], [88, 92], [86, 102], [88, 100], [88, 98], [88, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [86, 102], [88, 100], [86, 182], [186, 100], [90, 98], [88, 92], [88, 100], [86, 102], [88, 188], [178, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 100], [88, 100], [90, 98], [88, 92], [88, 100], [86, 102], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [384, 0]]

# (24deg, cool, fan3) Clock set, 23:31 hours 
ir_t2331 = [[294, 280], [88, 98], [88, 100], [94, 94], [88, 182], [186, 100], [88, 100], [88, 92], [88, 98], [88, 100], [88, 190], [178, 100], [88, 190], [186, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [86, 102], [88, 100], [88, 100], [86, 92], [88, 100], [88, 100], [88, 100], [88, 180], [188, 100], [294, 280], [88, 100], [86, 100], [90, 98], [90, 180], [186, 100], [88, 100], [88, 92], [88, 100], [86, 102], [86, 192], [176, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 100], [88, 90], [88, 100], [88, 100], [88, 100], [88, 182], [186, 100], [294, 280], [88, 100], [88, 100], [88, 100], [88, 180], [186, 100], [88, 100], [88, 92], [88, 100], [88, 100], [88, 190], [176, 100], [88, 190], [188, 90], [88, 100], [88, 100], [88, 100], [88, 92], [88, 100], [86, 100], [88, 102], [88, 90], [88, 100], [88, 100], [88, 100], [88, 90], [90, 100], [86, 100], [88, 100], [90, 180], [186, 100], [384, 0]]

