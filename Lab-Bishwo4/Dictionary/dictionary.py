# # 119. Write a program to convert two lists into a dictionary.
# _list = [1, 2, 3, 4, 5]
# _list1 = [6, 7, 8, 9, 10]
# dictionary = dict(zip(_list, _list1))
# print(dictionary)

# # 120. Write a program to merge two Python dictionaries into one.
# _list = {1, 2, 3, 4, 5}
# _list1 = {6, 7, 8, 9, 10}
# _list.update(_list1)
# print(_list)

# # 121. Write a program to initialize a dictionary with default values
# dictionary = dict.fromkeys(['One', 'Two', 'Three'],0)
# print(dictionary)

# 122. Write a program to create a dictionary by extracting the keys from a given dictionary.
dictionary = {'one':1, 'two':2, 'three':3, 'four':4}
dictionary_keys = dict()
print(dictionary.keys())
print(type(dictionary_keys))
for i in dictionary.keys():
    dictionary_keys.