option = input("Enter A or B :\n").upper()
print(option)
match option:
    case 'A' :
        print('A')
    case 'B' :
        print('B')
    case default:
        print('Other than A and B.')