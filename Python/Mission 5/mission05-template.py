#
# CS1010S --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    curve3 = translate(x_of(curve2(0)),y_of(curve2(0)))(curve1)
    curve4 = translate(x_of(curve1(1)),y_of(curve1(1)))(curve2)
    return translate(-x_of(curve2(0)),-y_of(curve2(0)))(connect_rigidly(curve3, curve4))

##########
# Task 2 #
##########
def show_points_gosper(level, num_points, initial_curve):
    def gosper_any_curve(level):
        return repeated(gosperize, level)(initial_curve)
    squeezed_curve = squeeze_curve_to_rect(-0.5,-0.5,1.5,1.5)\
                     (gosper_any_curve(level))
    draw_points(num_points,squeezed_curve)

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),rotate(-theta)(curve_fn)))
    return inner_gosperize

# testing
# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
