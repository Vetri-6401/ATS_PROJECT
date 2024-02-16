from tkinter import *
import mysql.connector
from tkinter import messagebox


class MainWindow():
    def __init__(self,window):
        self.data_base_connection()
        self.window = window
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.state("zoomed")
        self.window.title("Signup Window")

        # entry frame 
        self.entry_frame =Frame(self.window,bg="#94EF8E")
        self.entry_frame.pack(side="top",fill='x')
        
        # registeration components
        self.register_label = Label(self.entry_frame,text="Registeration Form",bg="#94EF8E",font=("comics sans",18))
        self.register_label.grid(row=0,column=5)

        self.userName_label = Label(self.entry_frame,text="User Name",bg="#94EF8E")
        self.userName_label.grid(row=1,column=0,padx=15,pady=20,sticky='w')

        self.userName_entry = Entry(self.entry_frame,width=30)
        self.userName_entry.grid(row=1,column=1,padx=15,pady=20)

        self.userPassword_label = Label(self.entry_frame,text="User Password",bg="#94EF8E")
        self.userPassword_label.grid(row=2,column=0,padx=15,pady=20,sticky='w')

        self.userPassword_entry = Entry(self.entry_frame,width=30)
        self.userPassword_entry.grid(row=2,column=1,padx=15,pady=20)    

        self.btn=Button(self.entry_frame,text="Register",command=self.insertData,width=15,relief='groove')
        self.btn.grid(row=3,column=1)
        self.btn=Button(self.entry_frame,text="login",command=self.des_entry,width=15,relief='raised')
        self.btn.grid(row=3,column=2,sticky='w')

    def data_base_connection(self):
         self.connection =mysql.connector.connect(host="localhost", user="root",password="",database="grocerystore")
         self.my_cursor = self.connection.cursor()
    def insertData(self):
        name=self.userName_entry.get()
        password=self.userPassword_entry.get()
        sql=f"INSERT INTO users (user_name,user_password) VALUES ('{name}', '{password}')"
        self.my_cursor.execute(sql)
        self.connection.commit()
        self.my_cursor.close()
        self.connection.close()
        messagebox.showinfo("Form submitted","Registered Successfully")
        self.entry_frame.destroy()
        self.loginFrame()


    # login  functionality



    # def getdata(self):
    #     self.data_base_connection()
    #     name=self.userName_entry.get()
    #     password=self.userPassword_entry.get()
    #     sql=f"select * from users where user_name='{name}' and user_password='{password}'"
    #     self.my_cursor.execute(sql)
    #     data=self.my_cursor.fetchone()
    #     self.my_cursor.close()
    #     self.connection.close
    #     self.userName_entry
    #     if not(data==None):
    #         messagebox.showinfo("User Verfied Status","Login Successfully")
    #     else:
    #         messagebox.showerror("User Verfied Status","Login failed")

    # to get all the datas 
    def getdata(self):
        self.data_base_connection()
        sql="select * from users"
        self.my_cursor.execute(sql)
        data=self.my_cursor.fetchall()
        print(data)
        if not(data==None):
            messagebox.showinfo("User Verfied Status","Login Successfully")
        else:
            messagebox.showerror("User Verfied Status","Login failed")
        self.my_cursor.close()
        self.connection.close()
    def des_entry(self):
        self.entry_frame.destroy()
        self.loginFrame()

    def loginFrame(self):
        self.login_frame =Frame(self.window,bg="#94EF8E")
        self.login_frame.pack(side="top",fill='x')
        # Login components
        self.register_label = Label(self.login_frame,text="Login Form",bg="#94EF8E",font=("comics sans",18))
        self.register_label.grid(row=0,column=5)

        self.userName_label = Label(self.login_frame,text="User Name",bg="#94EF8E")
        self.userName_label.grid(row=1,column=0,padx=15,pady=20,sticky='w')

        self.userName_entry = Entry(self.login_frame,width=30)
        self.userName_entry.grid(row=1,column=1,padx=15,pady=20)

        self.userPassword_label = Label(self.login_frame,text="User Password",bg="#94EF8E")
        self.userPassword_label.grid(row=2,column=0,padx=15,pady=20,sticky='w')

        self.userPassword_entry = Entry(self.login_frame,width=30)
        self.userPassword_entry.grid(row=2,column=1,padx=15,pady=20)    

        self.btn=Button(self.login_frame,text="Login",command=self.getdata)
        self.btn.grid(row=3,column=1,columnspan=2)

if __name__ == "__main__":
    window=Tk()
    my_obj = MainWindow(window)
    # my_obj.insertData("ram","ram@1234")


window.mainloop()