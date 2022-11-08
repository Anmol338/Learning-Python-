# Define set
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# print(type(a))

# # Write a program to add a single element in a set.
# a.add(10)
# print(a)

# Write a program to add a list of elements to a set.
# a.update(b)
# print(a)

# # Write a program to return a new set of identical items from two sets
# # temp = a.intersection(b)
# # print(temp)
# temp = a & b
# print(temp)

# Write a program to get Only unique items from two sets.
# # temp = a.union(b)
# # print(temp)
# temp = a | b
# print(temp)

# Write a program to update the first set with items that don’t exist in the second set.
# a = a | b
# print(a)

# Write a program to remove items from the set at once.
# print(a)
# try:
#  a.remove()
# except TypeError:
#     print("Value removed using remove funtion !!")

# Write a program to return a set of elements present in Set A or B, but not both.
# # temp = a.symmetric_difference(b)
# # print(temp)
# temp = (a-b) | (b-a)
# print(temp)

# Write a program to check if two sets have any elements in common. If yes, display the common elements.
# if(a.intersection(b)):
#     print(a.intersection(b))

# Write a program to update set1 by adding items from set2, except common items.
# print(a)
# print(b)
# temp = a.intersection(b)
# print(temp)
# temp1 = a-b
# print(temp1)
# temp2 = b-a
# print(temp2)
# temp3 = temp1.union(temp2)
# print(temp3)

# Write a program to remove items from set1 that are not common to both set1 and set2.
# print(a)
# print(b)
# temp = a-b
# print(temp)
# temp1 = b-a
# print(temp1)
# print(b-temp1)


# 117. Write a program which can apply the following set operations
# a. Intersection
# x = {1, 3, 7, 2, 4, 6, 5}
# y = {7, 6, 9, 8, 10, 12, 13, 11, 15, 14}
# print(x.intersection(y))
# # b. Union
# print(x.union(y))
# # c. Difference
# print(x.difference(y))
# print(y.difference(x))
# # d. Symmetric difference
# print(x.symmetric_difference(y))
# print(y.symmetric_difference(x))
