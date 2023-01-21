from sys import *
from datetime import *
import mysql.connector

print("\tLIBRARY MANAGEMENT TOOL BY YASH RAJ")
print("\t*************************************\n")
try:
    connection=mysql.connector.connect(host="localhost",user="root",password="@chandrakishore123",database="yashdb")
    print("Database connected ")
    databaseObj=connection.cursor()
 
    databaseObj.execute("create table if not exists accountTable(name varchar(80),roll int primary key,course varchar(10),joiningDate date)")
    
    databaseObj.execute("create table if not exists student(rollOfStudent int,bookName varchar(80),authorName varchar(80),course varchar(10),addingDate date)")
    databaseObj.execute("Alter table student add foreign key(rollOfStudent) references accountTable(roll)")
except:
    print("Exception occur during database connection: ",exc_info()[1])    

class library:
    def openAccount(self):
        Name=input("Enter name of Student : ")
        self.roll=input("Enter roll : ")
        Roll=self.roll
        course=input("Enter course: ")
        self.CurrentDate=date.today()
        Date=self.CurrentDate
       
        try:
            insertData="insert into accountTable(name,roll,course,joiningDate) values(%s,%s,%s,%s)"
            x=(Name,Roll,course,Date)
            databaseObj.execute(insertData,x)
            connection.commit()
            print("data inserted successfully")
            print("Account created for ",Name ,"successfully.")
            print("Date of creation: ",self.CurrentDate)
        except:
            # print("Exception ocurred during insertion in account table: ",exc_info()[1])
            print("Account Already Exist")
            choice=int(input(print("If you want to create another account then press 1 else 0:")))
            
            if(choice==1):
                     Name=input("Enter name of Student : ")
                     self.roll=input("Enter roll : ")
                     Roll=self.roll
                     self.CurrentDate=date.today()
                     Date=self.CurrentDate
                     insertData="insert into accountTable(name,roll,         joiningDate) values(%s,%s,%s)"
                     x=(Name,Roll,Date)
                     databaseObj.execute(insertData,x)
                     connection.commit()
                     print("data inserted successfully")
                     print("Account created for ",Name,          "successfully.")
                     print("Date of creation: ",self.CurrentDate)
            else:
                pass       
            
        
        
    def addBook(self):
        Roll=input("Enter Roll no. of Student: ")
        bname=input("Enter Book name: ")
        aname=input("Enter Author Name: ")
        course=input("Enter course: ")
        adate=date.today()
 
        try:
             insert="insert into student(rollOfStudent,bookName,authorName,course,addingDate)  values(%s,%s,%s,%s,%s)"
             data=(Roll,bname,aname,course,adate)
             databaseObj.execute(insert,data)
             connection.commit()
             print("book detail inserted in dataTable   successfully")
        except:
            print("Student Account not created")
            print("CREATE NEW ACCOUNT")
            print("---------------------------------")
            self.openAccount()
            # Roll=input("Enter Roll no. of Student: ")
            bname=input("Enter Book name: ")
            aname=input("Enter Author Name: ")
            course=input("Enter course: ")
            adate=date.today()
            insert="insert into student(rollOfStudent,bookName,authorName,course,addingDate)  values(%s,%s,%s,%s,%s)"
            data=(Roll,bname,aname,course,adate)
            databaseObj.execute(insert,data)
            connection.commit()
            print("book detail inserted in dataTable  successfully")
            
        
        
        
    
    def deleteBook(self):
   
                print("Enter book name to delete :")
                book=input()
       
                try:
                    delete="delete from  student where bookName={}".format(book)
                    databaseObj.execute(delete)
                    connection.commit()
                    print("Book record deleted from table successfully")
                except:
                    print("Problem in deleting due to:",exc_info()[1]) 
                       
        
    def display(self):

                print("\tBook Table Records")
                print("\t****************")
                databaseObj.execute("select * from student")
                result=databaseObj.fetchall()
                for row in result:
                    print(row)          
        
           
obj=library()
while(True):
    print("\n\nMENU")
    print("*********\n")
    print("1.Create New Account")
    print("2.Display accounts data")
    print("3. Add Book")
    print("4. Display All Book Records")
    print("5.Display records According to Student")
    print("6. Delete all book Record")
    print("7. Delete All Records of a student")
    print("8. Exit")
    print("Enter choice: ")
    choice=int(input())
    if(choice==1):
        obj.openAccount()
    elif(choice==2):
        try:
                    print("\tAccount Table records ")
                    print("\t*******************")
                    databaseObj.execute("select * from accountTable")
                    result=databaseObj.fetchall()
                    for row in result:
                        print(str(row),sep=",")
        except:
            print(exc_info()[1])
            
    elif(choice==3):
        obj.addBook()
           
    elif(choice==4):
        obj.display() 
    
    elif(choice==5):
               roll=int(input("Enter roll of student: "))
               condition="select * from student where rollOfStudent = {} ".format(roll)
               databaseObj.execute(condition)
               print("\tBook Table Records of student(",roll,")")
               print("\t***********************")
               rows=databaseObj.fetchall()
               for i in rows:
                   print(i)
                   
    elif(choice==6):
        obj.deleteBook() 
    elif(choice==7):    
        try:
                roll=int(input("Enter roll of student to delete its         record: "))
                databaseObj.execute("delete from student where rollOfStudent ={}        ".format(roll))
                databaseObj.execute("delete from accountTable where roll={}".format(roll))
                print("All records of student having roll ",roll,"         deleted Successfully")
        except:
            print("Problem in deleting records due to:  ",exc_info()[0])
    else:
        databaseObj.close();
        connection.close();
        print("____THANK YOU FOR USING THE LIBRARY SERVICE___")
        exit() 
             
           
      