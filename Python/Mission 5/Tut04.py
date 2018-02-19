def make_point(x, y):
    #Your code here
    return (x,y)

def x_point(p):
    #Your code here
    return p[0]
    
def y_point(p):
    #Your code here
    return p[1]

#For running public test case, do not delete


def make_segment(p1, p2):
    #Your code here
    return (p1,p2)
    
def start_segment(s):
    #Your code here
    return p1

def end_segment(s):
    #Your code here
    return p2
    
#For reference:
# p1 = make_point(2, 3)
# p2 = make_point(5, 7)

def midpoint_segment(segment):
    x = (x_point(start_segment(segment)) + x_point(end_segment(segment))) / 2
    y = (y_point(start_segment(segment)) + y_point(end_segment(segment))) / 2
    return (x,y)

p1 = make_point(2, 3)
p2 = make_point(5, 7)
s = make_segment(p1, p2)
