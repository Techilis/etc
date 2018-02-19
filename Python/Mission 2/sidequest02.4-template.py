#
# CS1010S --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: 4^n

# n * 3^n
# Ans: 3^n

# 1000000000n^2
# Ans: n^2

# 2^n/1000000000
# Ans: 2^n

# n^n + n^2 + 1
# Ans: n^2

# 4^n + 2^n
# Ans:4^n

# 1^n
# Ans: 1

# n^2
# Ans: n^2

# Faster order of growth in each group:

# i. O(4^n * n^2)
# ii. O(2^n / 1000000000)
# iii. O(4^n + 2^n)
# iv. O(n^2)


##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########

# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n^2)

def improved_foo(n):
    #Sum of 1 to n integers = n*(n+1)/2
    #Sum of 1 to n^2 = n*(n+1)*(2n+1)/6
    #Find sum of 1^2/2 + 1/2 to n^2/2 + n/2
    return int(1/2 * ((n*(n+1))/2 + (n*(n+1)*(2*n+1))/6))

# Improved time complexity: O(1)
# Improved space complexity: O(1)
