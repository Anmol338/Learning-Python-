from array import array
from random import random, randrange

nums = array('i',[])  # Array declare
index_number = []       # List declaration
temp_value = 0
tmp = 0

int_store = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

for i in range(0,24):   # for loop initialize
    nums.append(randrange(17,28))       # Adding number in array using randrange function.

print(nums)

# for i in range(0,len(int_store)-1):
#     if tmp == int_store[i] :
#         tmp_final = int(tmp)
#     else :
#         print("Incorrect Entry !!")
#         break
try:
    tmp = int(input("Enter the number you want to check between (17 - 27) : "))  # Tmp variable to store the counting number
except ValueError:
    print("Invalid input")

number_count = nums.count(tmp)  # Counting the repetation of number in an array

if number_count > 0 :
    for i in range(0, len(nums) - 1):
        temp_value = nums[i]

        if(temp_value == tmp) :
            index_number.append(i)
    print("Total number of {} found in array is {} and their respective index is {} .".format(tmp, number_count, index_number))  # Printing the found result
