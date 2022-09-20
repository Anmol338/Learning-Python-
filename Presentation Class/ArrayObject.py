import array
import sys

# Declare an array
nums = array.array('i', [6, 7, 2, 8, 9])
print(type(nums))
print(id(nums))
print(sys.getsizeof(nums))
print(len(nums))

# Index of array
print(nums[3])
print(nums[0])
print(nums[4])

# Update the element
nums[2] = 5
print(nums[2])

# Remove the element
del nums[4]
print(nums)

# Adding the element
nums.append(11)
print(nums)

print(nums[-1])

print(nums[-4])

# print(nums[-6]) # Out of range

### ----- Slicing ----- ###
print(nums[0:10])
print(nums[0:10:2])
print(nums[10:0:-1])
print(nums[::])
print(nums[:5])
print(nums[::2])

# print(dir(array.array))
print(help(array.array))

# ### ----- Array Index out of Range ----- ###
# # Declare an array
# nums = array.array('i', [])
# print(type(nums))
# print(id(nums))
# print(sys.getsizeof(nums))
# print(len(nums))
#
# # Index of array
# print(nums[3])
# print(nums[0])
# print(nums[4])
#
# # Update the element
# nums[2] = 5
# print(nums[2])
#
# # Remove the element
# del nums[4]
# print(nums)
#
# # Adding the element
# nums.append(11)
# print(nums)
# print(nums[-6])