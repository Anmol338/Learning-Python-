num = 0
num1 = 0
result = 0

# Function definition to check the maximum number
def check_max_num(a, b):    # Function name deifnition which accepts two arguments
    if a > b :
        return a
    else:
        return b

# Try exect to control the ValueError problem
try:
    num = int(input("Enter the first number : \n")) # Take first input from user
    num1 = int(input("Enter the second number : \n")) # Take second input from user
    result = check_max_num(num, num1)   # Calling function and passing the arguments to the function
    print("The max number between {} and {} is : {}".format(num, num1, result)) # Printing the greatest number.

except ValueError:      # To control the program error
    print("Enter the numbers only !!!")