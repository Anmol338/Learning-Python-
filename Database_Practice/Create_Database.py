import mysql.connector as mc

mydb = mc.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()

print(mydb)

if mydb:
    print("Connected to the database successfully !!!")

else:
    print("Failed to connect with the database !!!")

mycursor.execute("CREATE DATABASE IF NOT EXISTS anmol_python")
mycursor.execute("Show databases")

for db in mycursor:
    print(db)

mycursor.execute("Use anmol_python")

db = mycursor.execute("Show tables")

print(db)



# mycursor.execute("Drop database anmol_python")
#
# print("##### ----- New Line ----- #####")
#
# mycursor.execute("Show databases")
#
# for db in mycursor:
#     print(db)