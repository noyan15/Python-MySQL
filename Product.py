class Product:
    def __init__(self, name, price, productId, quantity, notEdible=False):
        self.__name = name
        self.__price = (price * (17/100)) + price if notEdible else price
        self.__productId = productId
        self.__quantity = quantity

    
    def createTable(self,cursor):
        sql = "CREATE TABLE products (name VARCHAR(255), price DECIMAL(10,2), productId VARCHAR(255), quantity INT)"
        try:
            cursor.execute(sql)
            print("Table created")
        except Exception as e:
            print(e)

    def insertIntoTable(self,cursor,db):
        sql = "insert into products (name, price, productId, quantity) values(%s,%s,%s,%s)"
        values = (self.__name, float(self.__price), self.__productId, int(self.__quantity))
        print(values)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Product added")
        except Exception as e:
            print(e)
        print("Product added")

    def getFromTable(self,cursor):
        sql = "select * from products where name = %s"
        values = (self.__name,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchone()
            print(result)
            return result
        except Exception as e:
            print(e)
    
    def deleteRecord(self,cursor,db):
        sql = "delete from products where name = %s"
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

    def getPrice(self):
        return self.__price

    def getProductId(self):
        return self.__productId

    def getQuantity(self):
        return self.__quantity
    
    # Setters

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setProductId(self, productId):
        self.__productId = productId

    def setQuantity(self, quantity):
        self.__quantity = quantity



    def __str__(self) -> str:
        return f"Name: {self.__name}, Price: {self.__price}, Product ID: {self.__productId}, Quantity: {self.__quantity}"