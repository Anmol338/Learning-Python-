
# ##### ----- Program to check the user is eligible for voting or not ----- #####
# print("##### ----- Program to check the user is eligible for voting or not ----- #####")
# input_age = input("Enter your age : ")
# age = 0
#
# try :
#     age = int(input_age)
#     if age >= 18 :
#         print("You are eligible for voting.")
#     else :
#         print("You are not eligible for voting.")
#
# except ValueError:
#     print("Please input your age in numnber.")




# ##### ----- Program to check value is odd or even ----- #####
# print("##### ----- Program to check value is odd or even ----- #####")
# input_value = input("Enter the number you want to check weather it is odd or even : ")
# value = 0
#
# try :
#     value = int(input_value)
#     if value % 2 == 0 :
#         print("{} is an even number.".format(value))
#     else :
#         print("{} is a odd number.".format(value))
#
# except ValueError:
#     print("Invalid input .")


# ##### ----- Program to check value is divisible by 7 or not ----- #####
# print("##### ----- Program to check value is divisible by 7 or not ----- #####")
# input_value = input("Enter the number  : ")
# value = 0
#
# try :
#     value = int(input_value)
#     if value % 7 == 0 :
#         print("{} is divisible by 7.".format(value))
#     else :
#         print("{} is not divisible by 7.".format(value))
#
# except ValueError:
#     print("Invalid input .")


# ##### ----- Program to check value is multiple of 5 or not ----- #####
# print("##### ----- Program to check value is multiple of 5 or not ----- #####")
# input_value = input("Enter the number : ")
# value = 0
#
# try :
#     value = int(input_value)
#     if value % 5 == 0 :
#         print("Hello")
#     else:
#         print("Bye")
#
# except ValueError:
#     print("Invalid input .")



# ##### ----- Program to check last digit of number ----- #####
# print("##### ----- Program to check last digit of number ----- #####")
# input_value = input("Enter the number : ")
# temp_value = 0
# check = 0
# value = 0
#
# try :
#     temp_value = int(input_value)
#     check = len(input_value)-1
#     value = input_value[check]
#     print(value)
#
# except ValueError:
#     print("Invalid input .")


# ##### ----- Program to check last digit of number ----- #####
# input_value = input("Enter the number : ")
# value = 0
# tmp_value = 0
#
# try :
#     value = int(input_value)
#     temp_value = value % 10
#     print("{} is a last digit of number.".format(temp_value))
#
# except ValueError:
#     print("Invalid Entry")


# ##### ----- Program to check last digit of number ----- #####
# print("##### ----- Program to check last digit of number ----- #####")
# input_value = input("Enter the number : ")
# temp_value = 0
# check = 0
# value = 0
#
# try :
#     temp_value = int(input_value)
#     check = len(input_value)-1
#     value = input_value[check]
#     temp_value = int(value)
#     if temp_value % 3 == 0 :
#         print("{} is divisible by 3.".format(temp_value))
#     else:
#         print("{} is not divisible by 3.".format(print("{} is divisible by 3.".format(value))))
#
# except ValueError:
#     print("Invalid input .")




# ##### ----- Program to check weather it is leep year or not ----- #####
# input_value = input("Enter the year you want to check : ")
# value = 0
#
# try :
#     value = int(input_value)
#     if value % 4 == 0 :
#         if value % 100 == 0 :
#             if value % 400 == 0 :
#                 print("Leap Year")
#             else:
#                 print("Not a leap year.")
#         else:
#             print("Leap Year.")
#     else:
#         print("Not a leap year.")
#
# except ValueError:
#     print("Invalid entry.")




# #### ----- Program to check weather it is leep year or not ----- #####
# input_value = input("Enter the year you want to check : ")
# value = 0
#
# try :
#     value = int(input_value)
#     if value % 4 == 0 :
#         if value % 100 == 0 :
#             if value % 400 == 0 :
#                 print("Leap Year")
#             else:
#                 print("Not a leap year.")
#         else:
#             print("Leap Year.")
#     else:
#         print("Not a leap year.")
#
# except ValueError:
#     print("Invalid entry.")




# ##### ----- program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 7 for Saturday ----- #####
# print("##### ----- Program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 7 for Saturday ----- #####")
# input_value = input("Enter the number (1 - 7) to check corresponding days : ")
# value = 0
#
# try :
#     value = int(input_value)
#     if value == 1 :
#         print("Sunday")
#     elif value == 2 :
#         print("Monday")
#     elif value == 3:
#         print("Tuesday")
#     elif value == 4:
#         print("Wednesday")
#     elif value == 5:
#         print("Thursday")
#     elif value == 6:
#         print("Friday")
#     elif value == 7:
#         print("Saturday")
#     else :
#         print("Invalid Entry.")
#
# except ValueError:
#     print("Invalid entry.")






##### ----- Program to accept a number from 1 to 12 and display the name of the month and days in that month like 1 for Jan and number of days 31 and so on. ----- #####
input_value = input("Enter the number (1 - 12) to check corresponding months : ")
value = 0

try :
    value = int(input_value)
    if value == 1 :
        print("Month = January and number of days = 31")
    elif value == 2 :
        print("February")
    elif value == 3:
        print("March")
    elif value == 4:
        print("April")
    elif value == 5:
        print("May")
    elif value == 6:
        print("June")
    elif value == 7:
        print("July")
    elif value == 8 :
        print("August")
    elif value == 9 :
        print("September")
    elif value == 10 :
        print("October")
    elif value == 11 :
        print("November")
    elif value == 12 :
        print("December")
    else :
        print("Invalid Entry")

except ValueError:
    print("Invalid entry.")
