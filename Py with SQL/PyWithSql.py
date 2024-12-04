import mysql.connector
from password import password

password1 = password()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = password1.getPassword(),
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")