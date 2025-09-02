"""
Problem:
Write a script that generates a list of 10 random integers in the range (1,20). Rearrange the
elements into new list the following way: all even numbers first, then all odd numbers.
"""

# import the random integer module
from random import randint

# generate a list of random integers
list = [randint(1, 20) for i in range(10)]
print("random list", list)

# initialize the even and odd lists
even = []
odd = []

# loop through the random integers
for i in list:
    # check if it's even
    if i % 2 == 0:
        # if so, append to the even list
        even.append(i)
    else:
        # if not, append to the odd list
        odd.append(i)

# print the even and odd lists
print("even first then odds", even + odd)
