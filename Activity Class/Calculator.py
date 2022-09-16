print("-----Calculator By Anmol Shrestha-----")

num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n"))
operator = input("Enter symbol '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division, '**' for power, '//' for integer division, '%' for remainder :\n")

if operator == "+" or operator == "-" or operator == "*" or operator == "/"  or operator == "**"  or operator == "//"  or operator == "%" :
    match operator :
        case "+" :
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "/":
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        case "**":
            result = num1 ** num2
            print(f"{num1} ^ {num2} = {result}")
        case "//":
            result = num1 // num2
            print(f"{num1} // {num2} = {result}")
        case "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
else :
    print("Invalid operators !!")

print("----- Thank for using my calculator -----")


