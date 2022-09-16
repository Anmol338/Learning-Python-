# Day printing

#input_value = int(input("Enter the value (1-7) : \n"))
dayvalue = int(input("Enter the value (1-7) : \n"))

#if input_value == 1 :
#	print("Sunday")
#elif input_value == 2 :
#	print("Monday")
#elif input_value == 3 :
#	print("Tuesday")
#elif input_value == 4 :
#	print("Wednesday")
#elif input_value == 5 :
#	print("Thursday")
#elif input_value == 6 :
#	print("Friday")
#elif input_value == 7 :
#	print("Saturday")
#else :
#	print("Out of range")

# Match-Case

if (dayvalue<=7) and (dayvalue>=1) :
	match dayvalue :
		case 1 :
			print("Sunday")
		case 2 :
			print("Monday")
		case 3 :
			print("Tuesday")
		case 4 :
			print("Wednesday")
		case 5 :
			print("Thursday")
		case 6 :
			print("Friday")
		case 7 :
			print("Saturday")
else :
	print("Out of range !!")
	