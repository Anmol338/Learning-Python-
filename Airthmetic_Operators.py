# Airthmetic Operators
# +, -, *, **, /, //, %
num1 = input("Enter the first number: \n")
num2 = input("Enter the second number: \n")

# + operator
sum = int(num1)+int(num2)
print("The sum of "+str(num1)+" + "+str(num2)+" = "+str(sum)+".")

# - operator
diff = int(num1)-int(num2)
print("The difference of "+str(num1)+" - "+str(num2)+" = "+str(diff)+".")

# * operator
pro = int(num1)*int(num2)
print("The product of "+str(num1)+" * "+str(num2)+" = "+str(pro)+".")

# ** operator
power = int(num1)**int(num2)
print("The power of "+str(num1)+" ^ "+str(num2)+" = "+str(power)+".")

# / operator
div = int(num1)/int(num2)
print("The float division of "+str(num1)+" / "+str(num2)+" = "+str(div)+".")

# // operator
div_int = int(num1)//int(num2)
print("The integer division of "+str(num1)+" // "+str(num2)+" = "+str(div_int)+".")

# % operator
mod = int(num1)%int(num2)
print("The remainder of "+str(num1)+" % "+str(num2)+" = "+str(mod)+".")