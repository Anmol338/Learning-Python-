input_num = 0
count_even = 0
count_odd = 0

try:
    input_num = int(input("Enter the nth term you want to count odd and even number : \n"))


    for i in range(1, input_num+1):
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print("The number of even number upto {} is : {}".format(input_num,count_even))
    print("The number of odd number upto {} is : {}".format(input_num, count_odd))

except ValueError:
    print("Please input number only !!!")