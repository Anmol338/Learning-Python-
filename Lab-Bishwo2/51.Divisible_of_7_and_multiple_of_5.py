num = 1500

for num in range(1500,2701):
    if num % 7 == 0:
        print("{} is divisible of 7.".format(num))

    if num % 5 == 0:
        print("{} is multiple of 5.".format(num))

    num += 1