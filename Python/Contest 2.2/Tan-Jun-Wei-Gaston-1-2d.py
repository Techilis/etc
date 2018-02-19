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
def floating_alien_head():
    #1st layer = ears
    ears = beside(quarter_turn_left(heart_bb), quarter_turn_right(heart_bb))
    earss = translate(0, -0.08,scale_independent(6/10, 1/5, ears))
    layer1 = earss

    #2nd layer = body
    body = scale_independent(1/2, 6/8, circle_bb)
    layer2 = body

    #3rd layer = eye, eyebrown
    #eyebrown
    eyebrown = scale_independent(1/20, 1/2, black_bb)
    eyebrowns = quarter_turn_right(stackn(3, eyebrown))
    eyebrownss = scale_independent(1/10, 1, eyebrowns)
    brown = translate(0, 0.035,scale_independent(1/2, 1, beside(eyebrownss, eyebrownss)))
    botheye = translate(0, -0.1, scale_independent(1/2, 1, beside(scale_independent(1/2,1/6,circle_bb), scale_independent(1/2,1/6,circle_bb))))
    #eyebrown + eye
    layer3 = overlay_frac(1/999, brown, botheye)

    #4th layer = mouth
    #mouth
    n = 50
    npic = scale(2/10, circle_bb)
    l = 1/2 - 1/n
    degree = 2/n
    count = 1 #Used for number of iterations
    while count <= n/2:
	    x = math.cos(math.pi*degree) * l
	    y = math.sin(math.pi*degree) * l
	    layer = translate(-y, x, npic)
	    if count == 1:
		    mouth = layer
	    else:
		    mouth = overlay_frac(1/999, layer, mouth)
	    degree += 2/n
	    count += 1
    mouth = quarter_turn_left(mouth)
    layer4 = translate(0, 0.15, scale(1/5,mouth))

    #5th layer = hat, eyeball
    bot_hat = scale_independent(2/5, 1/20, black_bb)
    top_hat = scale_independent(2/10, 1/8, black_bb)
    hat = overlay_frac(1/999, translate(0, -0.45, top_hat), translate(0, -0.35, bot_hat))
    eyeball = translate(0, -0.1, scale_independent(1/2, 1, beside(scale_independent(1/4,1/12,circle_bb), scale_independent(1/4,1/12,circle_bb))))
    layer5 = overlay_frac(1/999, hat, eyeball)

    #1st and 2nd layer
    layer12 = overlay_frac(1/99, layer2, layer1)
    #combining 3rd layer
    layer123 = overlay_frac(7/10, layer3, layer12)
    #combining 4th layer
    layer1234 = overlay_frac(1/2, layer4, layer123)
    #combining 5th layer
    layer12345 = overlay_frac(1/2, layer5, layer1234)
    #finally add shadow
    total = stack_frac(9/10, layer12345, body)
    return total

show(floating_alien_head())

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.
'''def foo():
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

#show(foo())
# show(<your rune>)'''



# Entry 3 of 3
# ============
# Write your function here. It should return a rune.


# show(<your rune>)
