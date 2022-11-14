import mysql.connector as mc
mydb = mc.connect(host="localhost", user="root", passwd="")

try:
    print(mydb)

    if mydb:
        print("Connection successfully !!")
    else:
        print("Failed to connect with database !!")
except ConnectionRefusedError:
    print("Please turn on Xampp and turn MySql on.")