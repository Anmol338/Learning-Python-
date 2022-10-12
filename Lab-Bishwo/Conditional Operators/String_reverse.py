# ##### ----- Program to reverse a string ----- #####
#
# str_input = input("Enter the string you want to reverse : ")
# temp_str = str_input[::-1]
#
# print(temp_str)




# ##### ----- Program to reverse a string ----- #####
# str_input = input("Enter the string you want to reverse : ") # Input string from user
# temp_str = ""
# str_len = len(str_input)+1
#
# for i in range (1, str_len) :
#     temp_str += str_input[-i]
#
# print(temp_str)




##### ----- Program to reverse a number ----- #####
num_input = input("Enter the number you want to reverse : ")            # Input string from user
num_checked = 0

try:
    num_checked = int(num_input)

except ValueError:
    print("Invalid Entry !!!")