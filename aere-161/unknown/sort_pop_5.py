# create an empty list
list = []

# beg  user until we have enough
while len(list) < 5:
    list.append(int(input("Enter an integer: ")))

# remove the first and last item
list.pop(0)
list.pop(-1)

# print
print(list)
