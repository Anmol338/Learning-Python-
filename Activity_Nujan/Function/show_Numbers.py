num = 0
numbers_type = []

# Function define
def showNumbers(limit):
    for i in range(limit+1):
        if i % 2 == 0:
            numbers_type.append("{} EVEN".format(i))
        else:
            numbers_type.append("{} ODD".format(i))

# try except to control the program from terminate while ValueError occurs
try:
    num = int(input("Enter the limit : \n"))
    showNumbers(num)

    for i in range(len(numbers_type)):
        print(numbers_type[i])

    # for i in numbers_type:
    #     print(i)

except ValueError:
    print("Please input the number only !!!")
