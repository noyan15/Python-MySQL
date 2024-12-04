class Employee:
    def __init__(self, name, address, email, contactNo, jobTitle):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__contactNo = contactNo
        self.__jobTitle = jobTitle

    def createTable(self,cursor):
        sql = "CREATE TABLE employees (name VARCHAR(255), address VARCHAR(255), email VARCHAR(255), contactNo VARCHAR(255), jobTitle VARCHAR(255))"
        try:
            cursor.execute(sql)
            print("Table created")
        except Exception as e:    
            print(e)

    def insertIntoTable(self,cursor,db):
        sql = "insert into employees (name, address, email, contactNo, jobTitle) values(%s,%s,%s,%s,%s)"
        values = (self.__name, self.__address, self.__email, self.__contactNo, self.__jobTitle)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Employee added")
        except Exception as e:
            print(e)

    def getFromTable(self,cursor):
        sql = "select * from employees where name = %s"
        values = (self.__name,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchone()
            print(result)
            return result
        except Exception as e:
            print(e)
    
    def deleteRecord(self,cursor,db):
        sql = "delete from employees where name = %s"
        values = (self.__name,)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Record Deleted")
        except Exception as e:
            print(e)

    # Getters 
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def getContactNo(self):
        return self.__contactNo

    def getJobTitle(self):
        return self.__jobTitle
    
    # Setter 
    def setName(self, name):
        self.__name = name  

    def setAddress(self, address):
        self.__address = address

    def setEmail(self, email):
        self.__email = email

    def setContactNo(self, contactNo):
        self.__contactNo = contactNo

    def setJobTitle(self, jobTitle):
        self.__jobTitle = jobTitle


    def __str__(self) -> str:
        return f"Name: {self.__name}, Address: {self.__address}, Email: {self.__email}, Contact No: {self.__contactNo}, Job Title: {self.__jobTitle}"
