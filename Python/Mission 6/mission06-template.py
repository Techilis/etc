#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:




# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below
def gosperize(curve):
    scaled_curve = scale(sqrt(2)/2)(curve)
    left_curve = rotate(pi/4)(scaled_curve)
    right_curve = translate(0.5,0.5)(rotate(-pi/4)(scaled_curve))

    return connect_rigidly(left_curve, right_curve)

def gosper_curve(level):
    return repeated(gosperize, level)(unit_line)
# <...replace this line of comment with your function call...>

# Time measurements
#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below
def gosperize_with_angle(theta):
    def inner_gosperize(curve):
        scale_factor = (1 / cos(theta)) / 2
        scaled_curve = scale(scale_factor)(curve)
        left_curve = rotate(theta)(scaled_curve)
        right_curve = translate(0.5,sin(theta)*scale_factor)(rotate(-theta)(scaled_curve))
        return connect_rigidly(left_curve, right_curve)
    return inner_gosperize

def gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        angle = angle_at_level(level)
        return gosperize_with_angle(angle)(gosper_curve_with_angle(level-1, angle_at_level))
# <...replace this line of comment with your function call...>

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below
def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),rotate(-theta)(curve_fn)))
    return inner_gosperize

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))



# <...replace this line of comment with your function call...>

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>


# Conclusion:
#  <...your conclusion here...>

##########
# Task 2 #
##########

#  1) your explanation here


#  2) your explanation here

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <...>         <...>
#                      2         <...>         <...>
#                      3         <...>         <...>
#                      4         <...>         <...>
#                      5         <...>         <...>
#
#  Evidence of exponential growth in joe_rotate.

