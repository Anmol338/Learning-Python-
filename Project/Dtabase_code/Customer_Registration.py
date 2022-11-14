import mysql
import mysql.connector as conn
from mysql.connector import errorcode

try:
    mydb = conn.connect(host="localhost", user="root", passwd="")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
 mydb.close()

# class Database_Connection :
#     def __init__(self, mydb):
#         self.mydb = mydb
#
#     def message(self):
#         if self.mydb:
#             return "Successfully connected to the database !!!"
#         else:
#             return "Failed to connect with database !!!"
#
# result = Database_Connection(mydb)
# print(result.message())
#
# mydb.close()