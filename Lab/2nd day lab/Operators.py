# Result processing

print("-------------------------------------------")

# input
student_id = input("Enter your SID : ")
student_name = input("Enter your NAME : ")
sub1 = int(input("Enter your marks in first subject : "))
sub2 = int(input("Enter your marks in second subject : "))
sub3 = int(input("Enter your marks in third subject : "))

# Processing
total = sub1 + sub2 + sub3
average = total/3

#Output
print("Total : {}".format(total))
print("Average : {}".format(average))

"""
if sub1>=40 and sub2>=40 and sub3>=40 :
	print("Result : Pass")
else :
	print("Result : Fail")
"""

"""
if sub1<40 or sub2<40 or sub3<40 :
	print("Result : Fail")
else :
	print("Result : Pass")
"""

if sub1>=40 :
	if sub2>=40 :
		if sub3>=40 :
			print("Result : 'PASS'")
else :
	print("Result : 'FAIL'")


print("-------------------------------------------")