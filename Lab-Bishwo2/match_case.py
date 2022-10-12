var = 0

try:
    var = int(input("Enter 1-7 number to print respective days : \n"))
    match(var):
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


except ValueError:
    print("Invalid number !!")