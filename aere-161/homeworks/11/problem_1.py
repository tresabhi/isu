"""
Abhigyaan Deep AER E 161

Purpose:
Write a function, that accepts a list of integers as input and returns a new list
containing only the even numbers greater than 10 from the original list.
"""


# declare a function
def filter1(list):
    # declare an empty list
    filtered = []

    # loop through the list
    for n in list:
        # check if the number is greater than 10 and even
        if n > 10 and n % 2 == 0:
            # if so, append to the filtered list
            filtered.append(n)

    # return the filtered list
    return filtered


# declare a function
def filter2(list):
    # return the filtered list with same logic as above
    return [n for n in list if n > 10 and n % 2 == 0]


# ask for a list of integers
list = input("Enter a list of integers separated by spaces: ").split()
# convert the list to integers
list = [int(n) for n in list]

# print the results
print("Filter 1:", filter1(list))
print("Filter 2:", filter2(list))
