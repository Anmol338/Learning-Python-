input_condition = None
input_num = 0
input_num1 = 0
sum = 0
result = None

# Function define to take input from user
def input_output():
    try:
        print("------- Main Menu -------")
        print("1. Add")
        print("0. Exit")
        print("-------------------------")
        return int(input("Enter your choice(0->exit):_"))
        print("-------------------------")

    except ValueError:
        print("Please input number 0 or 1 !!!")

def check_condition(condition):
    match(condition):
        case 1 :
            return True
        case 0 :
            return False

def total_sum():
    global input_num
    global input_num1
    global sum
    try:
        input_num = int(input("Enter first no :_"))
        input_num1 = int(input("Enter second no :_"))
        sum = input_num + input_num1
        print("Sum: {}".format(sum))

    except ValueError:
        print("Please input number only !!!")


# Function Calling
input_condition = input_output()
result = check_condition(input_condition)

# Condition check using if-else
while result == True :
    total_sum()
    input_condition = input_output()
    result = check_condition(input_condition)

print("Bye!")
# if result == True :
#     sum()
# else:
#     print("Bye!")