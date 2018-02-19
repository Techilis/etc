#
# CS1010S --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# (a)
# unit_line_at_y : (Number) -> function
# Function that takes in one variable (t) which will be the x-value of make_point
# Meanwhile, the y-value of make_point will already be defined by unit_line_at_y

##def f(y):
##    return def d(t):
##        def make_point(t,y):
##            return def e(m):
##                if m == 0:
##                    return x
##                else:
##                    return y
            

# (b)
# a_line : (Number) -> Point
# The input for a_line will become the x-value of the point

# (c)
def vertical_line(pt,length):
    return lambda t: make_point(x_of(pt),y_of(pt)+t*length)
    

##draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))

# (d)
# vertical_line: (Point, Number) -> Function
# It takes in a point from make_point() and a number which is the length,
# it then return a function which takes in t (also known as time)

# (e)
# draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# Not sure what answer the question is looking for...
# Several methods
# 1) draw_connected(200, curve) and then draw_connected(200, rotate_90(curve))
# and compare the results by visual inspection
# 2) Ensure that the curve transformation returns the curve as a function which takes in t
# this is similiar to the curve by itself. This is to ensure it returns a function instead of a variable
# 3) Create a function that reverses the curve function
# In the case of rotate_90 (rotating it 90 degrees anti-cw), create the following function,
''' def rotate_back (curve):
	def rotated_curve (t):
		pt = curve (t)
		return make_point (y_of(pt), -x_of(pt))
	return rotated_curve'''
# draw_connected(200, rotate_back(rotate_90(curve))) should return the same curve
# 4) Define a function to check, in the case of rotate_90:
''' def check(curve1, curve2): #Where curve1 is the transformed curve or curve2, the if statement is based on the curve transformation function
	for x in range(1,10):
		pt1 = curve1(1/x)
		pt2 = curve2(1/x)
		if x_of(pt1) != -y_of(pt2) or y_of(pt1) !=  x_of(pt2):
			#print(x_of(pt1))
			#print(y_of(pt2))
			#print(y_of(pt1))
			#print(-x_of(pt2))
			return False
	return True'''

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))
    return reflected_curve
	
##draw_connected_scaled(200, arc)
##draw_connected_scaled(200, reflect_through_y_axis(arc))

