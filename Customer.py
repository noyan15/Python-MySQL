class Customer:
    def __init__(self, name, address, email, idNo, order=None):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__idNo = idNo
        self.__order = order if order else []


    def addOrder(self, order):
        self.__order.append(order)

    def viewOrder(self):
        print(f"Name: {self.__name}, Address: {self.__address}, Email: {self.__email}, ID No: {self.__idNo}")
        for order in self.__order:
            print(order)

    def createTable(self,cursor):
        sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255), email VARCHAR(255), idNo VARCHAR(255))"
        try:
            cursor.execute(sql)
            print("Table created")
        except Exception as e:    
            print(e)

    def insertIntoTable(self,cursor,db):
        sql = "insert into customers (name, address, email, idNo) values(%s,%s,%s,%s)"
        values = (self.__name, self.__address, self.__email, self.__idNo)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Customer added")
        except Exception as e:
            print(e)

        # print("Customer added", sql)

    def getFromTable(self,cursor):
        sql = "select * from customers"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return result
        except Exception as e:
            print(e)

    
    def deleteRecord(self,cursor,db):
        sql = "delete from customers where name = %s"
        values = (self.__name,)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Record deleted")
        except Exception as e:
            print(e)


    # Getters 
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def getIdNo(self):
        return self.__idNo
    
    def getOrder(self):
        return self.__order
    
    # Setters    
    def setName(self, name):
        self.__name = name

        

    def setAddress(self, address):
        self.__address = address

    def setEmail(self, email):
        self.__email = email

    def setIdNo(self, idNo):
        self.__idNo = idNo


    def __str__(self) -> str:
        output = f"Name: {self.__name}, Address: {self.__address}, Email: {self.__email}, ID No: {self.__idNo}"
        return output