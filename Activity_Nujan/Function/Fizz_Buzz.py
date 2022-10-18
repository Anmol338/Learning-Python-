num = 0
result = None

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

try:
    num = int(input("Enter the number : \n"))
    result = fizz_buzz(num)
    print(result)

except ValueError:
    print("Please input only number !!!")