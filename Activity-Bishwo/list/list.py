import copy

# extend
# elem_list1 = list()
# elem_list1.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(elem_list1)
# print(type(elem_list1))


# list with loopto print the year
# type_list = list(range(1900, 2023))
# print(type_list)
# print(type(type_list))

# Append
# list_coll = []
# print(type(list_coll))
# list_coll.append(9)
# list_coll.append("String")
# list_coll.append(90.99)
# print(list_coll)

# # Mutability
# first_list = [1, 2, 3, 4, 5]
# second_list = [2, 4, 5]
#
# print(id(first_list))
# print(first_list)
#
# first_list.extend(second_list)
# print(first_list)
# print(id(first_list))

# # Slicing
# list_coll = []
# list_coll.extend(["Python", "Programming", 56, "Random"])
#
# print(list_coll[:2])
# print(list_coll[:-3])
# print(list_coll[1:])
# print(list_coll[:])
# print(list_coll[:9])
# print(list_coll[9:])

# # Sorted
# list_coll = []
# list_coll.extend([9,5,4,7,8,6,3,1,2])
# list_coll.sort()
# print(list_coll)
# list_coll.sort(reverse=True)
# print(list_coll)

# # Shallow copy and Deep copy
# a = [1, 2, 3]
# b = a                   # Shallow Copy
# c = copy.deepcopy(a)    # Deep Copy
#
# a[0] = 4
# a[1] = 100
#
# print(a)
# print(b)
# print(c)

# # Clear
# a = [1, 2, 3, 4, 5]
# print(a)
# a.clear()
# print(a)

# Del
a = [1, 2, 3, 4, 5]

