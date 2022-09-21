from array import array

"""
nums = array('i', [])
print(nums)

"""

"""
# append element on array
# append(self, v, /)
nums.append(8)
print(nums)
tmp = input("Enter any number: ")
tmp = int(tmp)
nums.append(tmp)
print(nums)
str1 = '23'
nums.append(int(str1))
print(nums)

# buffer_info(self, /)
print(nums.buffer_info())
# byteswap(self, /)
print(nums.byteswap())
"""

"""
# count(self, v, /)
nums = array('i', [3, 5, 6, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1])
result = nums.count(1)
print(result)

# extend(self, bb, /)
arr1 =array('i', [2, 3, 4, 5, 6])
arr2 = array('i', [8, 5, 6, 2, 1])
arr1.extend(arr2)
print(arr1)
"""

# index(self, v, start=0, stop=9223372036854775807)
# nums = array('i',[3,4,3,1,2,6,7,8,2,10])
# tmp = 1000
# result = nums.index(tmp, 0, len(nums))      # If value is absent ValueError: array.index(x): x not in array
# print(result)

nums = array('i', [5,6,7,8,9,2,3,1,2])
tmp = 20
result = nums.count(tmp)
if result > 0 :
    result2 = nums.index(tmp, 0, len(nums))
    print("{} found at {}".format(tmp, result2))
else :
    print("{} not found in array.".format(tmp))