# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 3 
x = 5
y = 1
y = ''
y = int()
print(x + y)

"""a = [1,5,6,7,1,3,4,5,8]
#a.sort()
print(a)
a.sort()
print(a)"""

def sorty(x):
    print(x)
    for j in range(len(x) - 1):
        for i in range(len(x)-1):
            if x[i+1] < x[i]:
                x[i], x[i+1] = x[i+1], x[i]
    print(x)
            
    
    

sorty([1,5,6,7,1,1,3,3,4,5,8])
       