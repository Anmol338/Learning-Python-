from Calculator_Class import Calculator # import user-defined class

# Taking input from the user
num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

# Creating object of class and passing parameter to the class
obj = Calculator(100, 200)

# Calling methods with the help of object
result = obj.sum()
print(f"The sum of {num1} + {num2} = {result}")