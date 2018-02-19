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
def shaking_alien_head():
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

    output = total
    x = 4
    n = 10
    ratio = n - 1
    stack_ratio = 1.1
    while x > 1:
	    total = overlay_frac(1/stack_ratio, scale(ratio/n, output), total)
	    stack_ratio += 1
	    ratio -= 1
	    x -= 1
    return total


#hollusion(shaking_alien_head())
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
    return output
# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
