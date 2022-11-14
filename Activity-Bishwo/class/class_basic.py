# class <identifier> :
#     methods

import new_class

# Define class
class Calculator:
    pass

# Create object of Class Calculator
obj = Calculator()

# Printing the type of object
print(type(obj))

print(__name__)

if __name__ == '__main__':
    calc = Calculator()
    print(type(calc))

new_call = new_class.name_function()
print(new_call)