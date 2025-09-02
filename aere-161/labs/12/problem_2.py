"""
Write a script that generates a list of random integers each in the range (-10,50). Perform
each of the following and print all results to the screen:
a) Find the number of negative elements in the list.
b) Find the sum of all positive elements in the list.
c) Find the smallest positive element in the list.
d) Find the second smallest positive element in your list.
"""

# import the random integer module
from random import randint

# generate a list of random integers
list = [randint(-10, 50) for i in range(10)]
print("random list", list)


# find the number of negative elements in the list
negative_count = 0
for i in list:
    if i < 0:
        negative_count += 1
print("negative count", negative_count)


# find the sum of all positive elements in the list
positive_sum = 0
for i in list:
    if i > 0:
        positive_sum += i
print("positive sum", positive_sum)


# find the smallest positive element in the list
smallest_positive = 0
for i in list:
    if i > 0 and i < smallest_positive or smallest_positive == 0:
        smallest_positive = i
print("smallest positive", smallest_positive)


# find the second smallest positive element in the list
second_smallest_positive = 0
for i in list:
    if (
        i > 0
        and i < smallest_positive
        and i < second_smallest_positive
        or second_smallest_positive == 0
    ):
        second_smallest_positive = i
print("second smallest positive", second_smallest_positive)
