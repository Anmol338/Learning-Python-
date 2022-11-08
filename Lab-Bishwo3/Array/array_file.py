from array import array

##### ----- 80. Print element of a array. ----- #####
sum = 0
largest = 0
nums = array('i', [1, 5, 3, 6, 2, 4, 9, 7, 8])
odd = array('i', [])
even = array('i', [])

# Only print the value of respective index
# for i in range(len(nums)):
#     print(nums[i])

# for elem in nums:
#     print(elem)
#
# for idx, val in enumerate (nums):
#     print(idx, val)

##### ----- 81. Sum of the array ----- #####
# for elem in nums:
#     sum += elem
#
# print(sum)

# ##### ----- 82. Write a program to find the largest element in an array ----- #####
# for i in range(len(nums)):
#     if (nums[i] > largest):
#         largest = nums[i]
#
# print(f"The largest element in an array is {largest} .")



# ##### ----- 82. Write a program to find the smallest element in an array ----- #####
# smallest = nums[0]
# for i in range(len(nums)):
#     if (nums[i] < smallest):
#         smallest = nums[i]
#         print(smallest)
# print(f"The smallest element in an array is {smallest} .")

# ##### ----- 84. Write a program to sort an array ascending order ----- #####
#
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if(nums[i] > nums[j]):
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#
# print(nums)

# ##### ----- Ascending order ----- #####
# print(sorted(nums, reverse=True))
#


# ##### ----- 85. Write a program to sort an array descending order ----- #####
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if(nums[i] < nums[j]):
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#
# print(nums)
#
# ##### ----- Decending order ----- #####
# print(sorted(nums, reverse=False))

##### ----- 86. Write a program to print all the odd elements of an array. ----- #####
##### ----- 87. Write a program to print all the even elements of an array. ----- #####
for i in range(len(nums)):
    if nums[i] % 2 == 0 :
        even.append(nums[i])
    else:
        odd.append(nums[i])

print(even)
print(odd)


