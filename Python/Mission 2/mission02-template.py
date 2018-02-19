#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, n):
    # Fill in code here
    if n == 1:
	    return pic
    else:
	    return beside(pic, stackn(2, fractal(pic, n-1)))
# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    output = pic
    for x in range(1,n):
        output = beside(pic, stackn(2, output))
    return output

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n ==1:
        return pic1
    else:
        return beside(pic1, stackn(2, dual_fractal(pic2, pic1, n-1)))

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
    count = 1
    if n % 2 == 0:
	    output = pic2
    else:
	    output = pic1
	    pic1, pic2 = pic2, pic1
    while count < n:
	    output = beside(pic1, stackn(2, output))
	    pic1, pic2 = pic2, pic1
	    count += 1
    return output

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
#########

def steps(p1, p2, p3, p4):
    layer1 = beside(blank_bb, stack(p1, blank_bb))
    layer2 = beside(blank_bb, stack(blank_bb, p2))
    layer3 = beside(stack(blank_bb, p3), blank_bb)
    layer4 = beside(stack(p4, blank_bb), blank_bb)
    return show(overlay(overlay(layer4, layer3), overlay(layer2, layer1)))

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
