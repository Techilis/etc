#
# CS1010S --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########
##def unit_circle(t):
##    return make_point(sin(2*pi*t), cos(2*pi*t))
##
##def alternative_unit_circle(t):
##    return make_point(sin(2*pi*t*t), cos(2*pi*t*t))
##The difference is alternative_unit_circle has an extra *t
##Looking at the sin and cos graph against pi we can see that the curve responds\
##nicely towards unit_circle and produces all points that are equally spaced
##However, in the case of alternative_unit_circle, the distance between the points\
##from the start of the circle starts of small and progressively gets bigger towards\
##the end of the curve due to multiplying it with *t again.
##This is because t is between 0 and 1.
##For example:
##x = (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
##def foo(x):
##	for i in range(len(x)):
##		print(x[i]**2)
##foo(x)
##0.010000000000000002
##0.04000000000000001
##0.09
##0.16000000000000003
##0.25
##0.36
##0.48999999999999994
##0.6400000000000001
##0.81
##1.0
##This allows shows that since t cannot be greater than 1, the point will be more clustered\
##     at the begining and more spaced out at the end.
##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(sin(2*pi*t)*t, cos(2*pi*t)*t)

# draw_connected_scaled(1000, spiral)

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))
    return reflected_curve

def antispiral(t):
    return make_point(-sin(2*pi*t)*t, cos(2*pi*t)*t)

def heart(t):
    return connect_rigidly(spiral, reflect_through_y_axis(spiral))




# draw_connected_scaled(1000, heart)
