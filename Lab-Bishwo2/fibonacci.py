a = 0
b = 1
c = 0
inp = 0

try:
    inp = int(input("Enter the nth term to print the fibonacci series : \n"))

    print(a)
    print(b)
    for i in range(2,inp):
        c = a + b
        print(c)
        a = b
        b = c


except ValueError:
    print("Please input numbers only !!!")