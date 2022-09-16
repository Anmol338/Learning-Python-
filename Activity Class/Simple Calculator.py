print("----- Calculator by Anmol Shrestha -----")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
check = int(input("Enter (1-4) numbers : 1 for '+' , 2 for '-' , 3 for '*' , 4 for '/' : \n"))

if check == 1 :
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif check == 2 :
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif check == 3 :
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif check == 4 :
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else :
    print("Invalid input")

print("----- Thanks for using my calculator !!! -----")

top = Tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
