from array import array
# nums = array('i',[])
# print(nums)

# # insert (self, i, v, /)
# nums.insert(3,2)
# print(nums)

# pop(self, i=-1, /)
# nums = array('i', [4,5,6,7,8])
# print(nums)
# nums.pop()  # Remove index from last
# print(nums)
# nums.pop()  # Remove index from last
# print(nums)
# nums.pop()  # Remove index from last
# print(nums)
# nums.pop()  # Remove index from last
# print(nums)
# nums.pop()  # Remove index from last      ## Error : IndexError: pop from empty array
# print(nums)
# nums.pop()  # Remove index from last
# print(nums)

# remove(self, v, /)
# nums = array('i' , [4,5,6,7,8])
# print(nums)
# nums.remove(100)      # value remove       ## Error : ValueError: array.remove(x): x not in array
# print(nums)

# reverse(self, /)
# nums = array('i' , [4,5,6,7,8])
# print(nums)
# nums.reverse()  # Reverse the index
# print(nums)

############## ------- Homework ------ ###########

# Sorting array element (ASC/DESC)
nums = array('i', [4,5,1,2,6,0,-1])

##### ----- Ascending order ----- #####
# for i in range(0, len(nums)):
#     for j in range(0,len(nums)-1):
#         if nums[i] < nums[j]:
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#
# print(nums)
#
# ##### ----- Decending order ----- #####
# for i in range(0, len(nums)):
#     for j in range(0,len(nums)-1):
#         if nums[i] > nums[j]:
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#
# print(nums)