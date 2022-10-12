# ##### ----- Program to check Odd and even number ----- #####
# print("##### ----- Program to check weather number is odd or even ----- #####")
# num1 = input("Enter the number to check wheather it is odd or even : ")
# checked_num1 = 0
#
# try :
#     checked_num1 = int(num1)
#     if checked_num1 % 2 == 0 :
#         print("{} is an even number.".format(checked_num1))
#     else :
#         print("{} is an odd number.".format(checked_num1))
#
# except ValueError:
#     print("Please input numbers only.")



# ##### ----- Storage Check ----- #####
# storage = 1000
# filesize = 600
#
# if filesize < storage:
#     storage -= filesize
#     print("You have {} MB remaining.".format(storage))
# else :
#     print("You don't have enough storage.")



# ##### ----- Program to check the grading system ----- #####
# percentage_input = input("Enter the percentage you have received : ")
# percentage = 0
#
# try :
#     percentage = int(percentage_input)
#     if percentage >= 80 :
#         print("Distiction")
#     elif percentage >= 60 :
#         print("First Division")
#     elif percentage >= 50:
#         print("Second Division")
#     elif percentage >= 40 :
#         print("Third Division")
#     elif percentage < 60 :
#         print("Fail !!!")
#
# except ValueError:
#     print("Please input the percentage into number.")