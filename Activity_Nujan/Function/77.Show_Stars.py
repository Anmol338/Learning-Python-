##### ----- Program to show the stars ----- #####

input_row = 0 # Variable store the number of rows

# Function define to print the stars
def show_stars(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")

# Try except which prevent program form terminated when Value Error occurs
try:
    input_row = int(input("Enter the numbers of rows : \n"))
    show_stars(input_row)

except ValueError:
    print("Please enter the number of rows in number only !!!")