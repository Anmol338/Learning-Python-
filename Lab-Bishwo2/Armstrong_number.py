num = 0
arm = 0
temp = 0

print("----- Program to check Palindrome number -----")
try:
    num = int(input("Enter the number to check : "))
    temp = num
    while temp > 0:
        temp_rem = temp % 10
        arm += temp_rem ** 3
        temp = temp // 10

    if num == arm :
        print("{} is a armstrong number.".format(num))
    else:
        print("{} is not a armstrong number.".format(num))

except ValueError:
    print("Please input the number only !!!")
