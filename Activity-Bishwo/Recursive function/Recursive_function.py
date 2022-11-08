# Function Definition
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# Input from user
input_num = int(input("Enter any number you want to print the factorial of that number :\n"))

# Calling function and store the return value into result
result = factorial(input_num)

# Printing the value of
print(f"The factorial of {input_num} is {result}.")
