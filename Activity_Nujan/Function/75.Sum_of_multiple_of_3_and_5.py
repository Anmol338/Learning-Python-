user_input = 0
return_sum = 0

def sum_of_multiple(limit):
    sum = 0
    for i in range(1,limit+1):
        if i % 3 == 0 or i % 5 == 0 :
            sum += i
    return sum

try:
    user_input = int(input("Enter the limit number : \n"))
    return_sum = sum_of_multiple(user_input)
    print("The sum of multiple of 3 and 5 is : {}".format(return_sum))

except ValueError:
    print("Please input the number only !!!")