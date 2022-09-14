# Logical Operators
# Basic logical operators :- and, or, not

num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))
num3 = int(input("Enter the third number: \n"))
num4 = int(input("Enter the fourth number: \n"))

answer = (num1==num2) and (num3==num4)
print("And Gate")
print(answer)

print("Not Gate")
print(not(answer))

print("Or Gate")
answer = (num1==num2) or (num3==num4)
print(answer)

print("Not Gate")
print(not(answer))