import  random

guess_num = 0
user_input = 0

user_input = int(input("Guess a number between 1-20 : "))
guess_num = random.randint(1, 21)
print(guess_num)

while user_input != guess_num:
    user_input = int(input("Guess a number between 1-20 : "))

print("Generate number : {} , Your guess number : {}".format(guess_num, user_input))