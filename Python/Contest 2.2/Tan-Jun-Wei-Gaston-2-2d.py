#
# CS1010S --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.


# Entry 2 of 3
# ============
# Write your function here. It should return a rune.
def foo():
    face = black_bb
    npic = scale(1/8, make_cross(rcross_bb))
    degree = 1/20
    for i in range(1,20):
	    x = math.cos(math.pi*degree) * (1/2 - 1/20)
	    y = math.sin(math.pi*degree) * (1/2 - 1/20)
	    layer = translate(-y, x, npic)
	    if i == 1:
		    output = layer
	    else:
		    output = overlay_frac(1/999, layer, output)
	    degree += 1/20
    smile = quarter_turn_left(output)
    eyes = overlay_frac(1/999, translate(-0.25, -0.25, scale(1/4,ribbon_bb)),\
                        translate(0.25, -0.25, scale(1/4,ribbon_bb)))
    nose = flip_vert(scale(1/3, heart_bb))
    return overlay_frac(1/5, eyes, overlay_frac(1/999, nose, overlay(smile, face)))

show(foo())
# show(<your rune>)



# Entry 3 of 3
# ============
# Write your function here. It should return a rune.


# show(<your rune>)
