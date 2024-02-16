import sqlite3

class Database:
    def __init__(self):
        self.connection =sqlite3.connect("signup_users.db")
        self.cursor = self.connection.cursor()
        sql="""
            create table if not exists users(
            id int,
            name text,
            passwords text
            )
            """
        self.cursor.execute(sql)
        self.connection.commit()
        


    def insertData(self,name,password):
        sql=f"insert into users values(NULL,'{name}','{password}')"
        self.cursor.execute(sql)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

if __name__ =="__main__":
    my_obj=Database()
    name=input("enter name")
    password=input("enter password")
    my_obj.insertData(name,password)