num = 0
num1 = 0
num2 = 0
num3 = 0

try:
    num = int(input("Enter any number : \n"))

    if num > 0:
        num = num % 10
        num1 = num // 10

    else:
        print("Please input number greater than 0.")

    print("The last digit of your number is : {}".format(num))
    print("The remaining number is : {}".format(num1))

except ValueError:
    print("Invalid Value")
