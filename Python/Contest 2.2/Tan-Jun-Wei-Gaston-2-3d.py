#
# CS1010S --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

# Entry 2 of 3
# ============
def ball():
    pic = circle_bb
    n = 50
    output = pic
    ratio = n - 1
    stack_ratio = 2
    for x in range(1,8):
	    output = overlay_frac(1/stack_ratio, scale(ratio/n, pic), output)
	    stack_ratio += 1
	    ratio -= 1
	    x -= 1
    #Supposed to ressemble a ball rolling back and forth
    return output
hollusion(ball())
# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
