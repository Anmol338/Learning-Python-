inp = 0
sum = 0

try:
    inp = int(input("Enter the natural number you want to find the sum of square of that number : \n"))
    for i in range(inp,0,-1):
        sum += i**2

    print("The sum of square of {} is : {}".format(inp,sum))

except ValueError:
    print("Please Input the number only !!!")