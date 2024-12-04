from Customer import Customer
from Order import Order
from Product import Product
from Employee import Employee

from Password import Password


import mysql.connector


def taskWithDB():

    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = Password().getPassword(),
    database = "shop"
    )

    mycursor = mydb.cursor()

    customer1 = Customer("abc", "KUST", "abc@ku.edu", "123")
    employee = Employee("noOne", "KUST", "noOne@ku.edu", "420", "Cashier")
    order1 = Order('1', "2022-01-01", employee)
    product1 = Product("Milk", 20, '456', 4, False)
    # product2 = Product("Bread", 25, '789', 2, False)
    

    # customer1.createTable(mycursor)
    # customer1.insertIntoTable(mycursor, mydb)
    # customer1.getFromTable(mycursor)
    # customer1.deleteRecord(mycursor, mydb)

    # employee.createTable(mycursor)
    # employee.insertIntoTable(mycursor, mydb)
    # employee.getFromTable(mycursor)
    employee.deleteRecord(mycursor, mydb)

    # product1.createTable(mycursor)
    # product1.insertIntoTable(mycursor, mydb)
    # product1.getFromTable(mycursor)
    # product1.deleteRecord(mycursor, mydb)

    # order1.createTable(mycursor)
    # order1.insertIntoTable(mycursor, mydb)
    # order1.getFromTable(mycursor)
    # order1.deleteRecord(mycursor, mydb)

    
    # product2.insertIntoTable(mycursor, mydb)

    # print(product1.getFromTable(mycursor))

    # order1.createTable(mycursor)

    # order1.insertIntoTable(mycursor, mydb)

    # order1.addOrder(customer1)

    # order1.viewOrder(mycursor)





def main():
    
    
    customer1 = Customer("Ali zeb", "KUST", "alizeb@ku.edu", "123")
    customer2 = Customer("Abdul Rehman", "KUST", "abdulrehman@ku.edu", "321")

    employee = Employee("Hussain", "KUST", "hussain@ku.edu", "420", "Cashier")

    product1 = Product("Milk", 20, '456', False)
    product2 = Product("Bread", 25, '789', False)
    product3 = Product("Eggs", 30, '123', True)

    order1 = Order(1, "2022-01-01", employee)
    order2 = Order(2, "2022-01-02", employee)
    order3 = Order(3, "2022-01-03", employee)

    order1.addProduct(product1)
    order1.addProduct(product2)
    order1.addProduct(product3)

    order1.removeProduct(product1)

    order2.addProduct(product1)
    order2.addProduct(product2)
    
    order3.addProduct(product1)
    order3.addProduct(product2)
    order3.addProduct(product3)

    customer1.addOrder(order1)
    customer1.addOrder(order2)
    customer1.addOrder(order3)

    customer2.addOrder(order1)
    customer2.addOrder(order2)

    order3.confirmOrder(order3, customer1)

    customer1.viewOrder()
    customer2.viewOrder()

    

# main()

taskWithDB()