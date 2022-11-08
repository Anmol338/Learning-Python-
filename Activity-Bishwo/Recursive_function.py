# Function Definition
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

input_num = int(input("Enter any number you want to print the factorial of that number :\n"))
result = factorial(input_num)
print(f"The factorial of {input_num} is {result}.")
