input_speed = 0
temp = 0
hold = None
count = 0

# Function to check the spped of vehicle and return data according to the car speed
def speed_check(speed):
    count = 0   # Store the point received by car
    if speed <= 70 :        # Check if spped is less than or equal to 70 or not
        return  "Ok"
    elif speed > 70 :      # Check the speed is greater then 70 or not
        temp = round((speed - 70))  # Calculate the cross speed and round it to nearest and store in tem
        for i in range(1, temp+1, 5): # Calculate the cross speed in diff of 5 and assign the counter point
            count += 1
        if count >= 12:     # Check the counter point
            return "Licence suspended"
        else:
            return "Points : {}".format(count)

try:
    input_speed = int(input("Enter the speed of the car : "))   # Taking input the speed of the vehicle
    hold = speed_check(input_speed)     # Function calling and store the return value in hold
    print(hold)     # Printing the value of hold

except ValueError:      # Control the program from Error and throw the error message
    print("Please input number only !!!")