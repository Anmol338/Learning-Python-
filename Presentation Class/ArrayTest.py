from array import array
#
# # declare
# nums = array('i',[5,6,2,8,9])
# print(nums)         # display all elements
# print(nums[0])      # access index +ve
# print(nums[-5])     # access index -ve
# print(id(nums[0]))  # address of element - 1st
# print(id(nums[1]))  # address of element - 2nd
#
# # methods/functions
# nums = array('i',[])            # declare
# nums.append(7)                  # Adding the element in array
# print(nums)                     # display all element of array
# nums.append(6)                  # Adding the element in array
# nums.append(10)                 # Adding the element in array
# print(nums)                     # display all element of array
# print(nums[0])                  # display index[0] element of array
# print(nums[1])                  # display index[1] element of array
# print(nums[-1])                 # display index[-1] element of array
# print(nums[-2])                 # display index[-2] element of array

user_view = ''
nums = array('i',[])
nums.append(int(input("Enter any number : ")))
print(nums)
user_view = input(" Do you want to continue (Y/N): ").lower()

while user_view == "y" :
    nums.append(int(input("Enter any number : ")))
    print(nums)
    user_view = input(" Do you want to continue (Y/N): ")

if user_view == "n":
    print(nums)
    print("Bye Bye !!")

tup1 = nums.buffer_info()
print(tup1)
print(type(tup1))
print(nums.byteswap())

n = nums.count(100)
print(n)

##### ----- Random NUmber ----- #####