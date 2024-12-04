class Order:
    def __init__(self, orderId, orderDate, employee):
        self.__orderId = orderId
        self.__products = []
        self.__cashier = employee
        self.__orderDate = orderDate

    def createTable(self,cursor):
        sql = "CREATE TABLE orders (orderId VARCHAR(255), orderDate VARCHAR(255), cashier VARCHAR(255))"
        try:
            cursor.execute(sql)
            print("Table created")
        except Exception as e:
            print(e, "table not created")
            

        

    def insertIntoTable(self,cursor,db):
        sql = "insert into orders (orderId, orderDate, cashier) values(%s,%s,%s)"
        values = (self.__orderId, self.__orderDate, self.__cashier)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Order added")
        except Exception as e:
            print(e)
            

    def getFromTable(self,cursor):
        sql = "select * from orders where orderId = %s"
        values = (self.__orderId,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchone()
            print(result)
            return result
        except Exception as e:
            print(e)

      
    
    def deleteRecord(self,cursor,db):
        sql = "delete from orders where orderId = %s"
        values = (self.__orderId,)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Record deleted")
        except Exception as e:
            print(e)


    def addProduct(self, product):
        if product in self.__products:
            product.setQuantity(product.getQuantity() + 1)
            return
        self.__products.append(product)
        

    def removeProduct(self, product):
        if product not in self.__products:
            return
        if product.getQuantity() > 1:
            product.setQuantity(product.getQuantity() - 1)
            return
        self.__products.remove(product)

    def clearOrder(self):
        self.__products = []
        print("Order cleared")

    def viewOrder(self):
        print(f"cashier: {self.__cashier}")
        for product in self.__products:
            print(product)

    def totalPrice(self):
        total = 0
        for product in self.__products:
            total += product.getPrice()
        return total

    def confirmOrder(self, order, customer):
        customer.addOrder(order)

    
    # Getters 
    def getOrderId(self):
        return self.__orderId
    
    def getCashier(self):
        return self.__cashier

    def getOrderDate(self): 
        return self.__orderDate

    def getProducts(self):
        return self.__products

    # Setters
    def setOrderId(self, orderId):
        self.__orderId = orderId

    def setCashier(self, employee):
        self.__cashier = employee

    def setOrderDate(self, orderDate):
        self.__orderDate = orderDate

    def setProducts(self, products):
        self.__products = products


    

    def __str__(self) -> str:
        return f"Order ID: {self.__orderId}, Order Date: {self.__orderDate}"