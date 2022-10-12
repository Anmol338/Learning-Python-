num = 1  # Declaring a int type variable and assigned the value
flag = False  # Declaring a bol type variable and assigned the value

while num <= 10:  # While loop used to run upto 10
    if num > 1:  # if condition to check weather the num is greater than 1 or not
        for i in range(2, num):  # for loop
            if (num % i) == 0:  # if the statement return 0 it change the flag value true
                flag = True

    if flag:
        print("{} is not a prime number.".format(num))
    else:
        print("{} is a prime number.".format(num))

    num += 1
    flag = False
