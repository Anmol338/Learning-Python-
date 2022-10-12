fact = 1

var = 0

try:
    var = int(input("Enter the number to print the factorial : \n"))

    for i in range(var,0,-1):
        fact *= i

    print("Factorial of {} = {}".format(var,fact))

except ValueError:
    print("Please Input number only !!!")