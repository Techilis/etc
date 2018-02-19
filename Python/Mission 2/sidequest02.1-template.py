#
# CS1010S --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
import math

##########
# Task 1 #
##########

def tree(n, pic):
	x = n
	output = pic
	ratio = n - 1
	stack_ratio = 2
	while x > 1:
		print(ratio)
		output = overlay_frac(1/stack_ratio, scale(ratio/n, pic), output)
		stack_ratio += 1
		ratio -= 1
		x -= 1
	return output

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)
def helix(pic, n):
    npic = scale(2/n, pic)
    l = 1/2 - 1/n
    degree = 2/n
    count = 1 #Used for number of iterations and for ratio of layers
    while count <= n:
	    x = math.cos(math.pi*degree) * l
	    y = math.sin(math.pi*degree) * l
	    layer = translate(-y, x, npic)
	    if count == 1:
		    output = layer
	    else:
	        output = overlay_frac(1/(count), layer, output)
	    degree += 2/n
	    count += 1
    return output


# Test
#show(helix(make_cross(rcross_bb), 9))
