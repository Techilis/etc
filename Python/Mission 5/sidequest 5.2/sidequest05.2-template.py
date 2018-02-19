#
# CS1010S --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########
def kochize(level):
    def koko(curve):
        scaled_curve = scale(1/3)(curve)
        curve1 = scaled_curve
        curve2 = rotate(pi/3)(scaled_curve)
        curve3 = rotate(-pi/3)(scaled_curve)
        return connect_ends(connect_ends(connect_ends(curve1,curve2),curve3),curve1)
    return repeated(koko,level)(unit_line)
def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))
    

#show_connected_koch(0, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    flake1 = kochize(5)
    flake2 = rotate(-2*pi/3)(kochize(5))
    flake3 = rotate(2*pi/3)(kochize(5))
    return connect_ends(connect_ends(flake1,flake2),flake3)

#draw_connected_scaled(10000, snowflake())
