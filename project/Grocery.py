
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image,ImageTk
import mysql.connector

class APP():
    def __init__(self,window):   #window=tk.TK()
        self.window=window #tk.TK()
        self.screen_width=self.window.winfo_screenwidth()
        self.screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        window.title("My Application")

        
        self.signup_bg_image=Image.open("D:/signup.jpg")
        self.new_size=(self.screen_width,self.screen_height)
        self.resized_image=self.signup_bg_image.resize(self.new_size)
        self.back_image=ImageTk.PhotoImage(self.resized_image)
        self.label1=tk.Label(self.window,image=self.back_image)
        self.label1.place(relwidth=1,relheight=1)

        self.Bg_image= Image.open('D:/newlogin.jpeg')
        self.resized_image1=self.Bg_image.resize(self.new_size)
        self.back_image1=ImageTk.PhotoImage(self.resized_image1)
        self.label2=tk.Label(self.window,image=self.back_image1)

        self.Signupframe()
        self.loginframe()
        self.data_base_connection()

    def Signupframe(self):

        self.Label3=tk.Label(self.label1,text="User_name",bg="royalblue",width="10",font=("times new roman",12))
        self.Label3.place(x=600,y=250)

        self.Label4=tk.Label(self.label1,text="password",bg="royalblue",width="10",font=("times new roman",12))
        self.Label4.place(x=600,y=300)

        self.Entry1=tk.Entry(self.label1,width="26")
        self.Entry1.place(x=696,y=250,height="25")

        self.Entry2=tk.Entry(self.label1,width="26")
        self.Entry2.place(x=696,y=300,height="25")

        self.Button1=tk.Button(self.label1,text="Create an account",bg="cyan",width="28",font=("times new roman",12),command=self.insertData)
        self.Button1.place(x=598,y=350)

        self.Label5=tk.Label(self.label1,text="Already have an account?",bg="firebrick",fg="white",width="20",font=("times new roman",12))
        self.Label5.place(x=598,y=420)

        self.Button2=tk.Button(self.label1,text="Login",bg="green",width="8",font=("times new roman",10),command=self.changeframe)
        self.Button2.place(x=785,y=420)

    def loginframe(self):

        self.Label6=tk.Label(self.label2,text="User_name",bg="lime",width="10",font=("times new roman",12))
        self.Label6.place(x=600,y=250)

        self.Label7=tk.Label(self.label2,text="password",bg="lime",width="10",font=("times new roman",12))
        self.Label7.place(x=600,y=300)

        self.Entry3=tk.Entry(self.label2,width="26")
        self.Entry3.place(x=696,y=250,height="25")

        self.Entry4=tk.Entry(self.label2,width="26")
        self.Entry4.place(x=696,y=300,height="25")

        self.Button3=tk.Button(self.label2,text="Login",bg="fuchsia",width="28",font=("times new roman",12),command=self.mainpage)
        self.Button3.place(x=598,y=350)

        self.Label8=tk.Label(self.label2,text="Don't have an account?",bg="salmon",width="20",height="1",font=("times new roman",12))
        self.Label8.place(x=598,y=420)

        self.Button2=tk.Button(self.label2,text="Signup",bg="red",width="8",font=("times new roman",10),command=self.changeframe1)
        self.Button2.place(x=785,y=420)
       

    def data_base_connection(self):
        self.connection =mysql.connector.connect(host="localhost", user="root",password="",database="grocery")
        self.my_cursor =self.connection.cursor()
        
    def insertData(self):
        name=self.Entry1.get()
        password=self.Entry2.get()
        sql=f"INSERT INTO users (user_id,user_name,user_password) VALUES (12,'{name}', '{password}')"
        self.my_cursor.execute(sql)
        self.connection.commit()
        self.my_cursor.close()
        self.connection.close()

        msg.showinfo(title="Info",message="You have registed successfully")

    def changeframe(self):
        self.label1.place_forget()
        self.label2.place(relwidth=1,relheight=1)
        
        # if hasattr(self,'label'):
        #     self.label.destroy()
        #     self.label2.place(relwidth=1,relheight=1)

    def changeframe1(self):
        self.label2.place_forget()
        self.label1.place(relwidth=1,relheight=1)

        # if hasattr(self,'label2',"label"):
        #     self.label2.place_forget()
        #     self.label.place(relwidth=1,relheight=1)
         

    def mainpage(self):

        # if hasattr(self,'label'):
        #     self.label.destroy()
        self.user_name=self.Entry3.get()
        self.password=self.Entry4.get()

        if self.user_name=="admin" and self.password=="admin@1234":

            self.label2.place_forget()
            self.Bg_image= Image.open('D:/database.jpg')
            self.new_size=(self.screen_width,self.screen_height)
            self.resized_image1=self.Bg_image.resize(self.new_size)
            self.back_image1=ImageTk.PhotoImage(self.resized_image1)
            self.label10=tk.Label(self.window,image=self.back_image1)
            self.label10.place(relwidth=1,relheight=1)

            self.Button3=tk.Button(self.label10,text="Admin profile",bg="lightblue",width="20",font=("times new roman",22))
            self.Button3.grid(row=0,column=0)

            self.Button4=tk.Button(self.label10,text="AccountDetails",bg="lightblue",width="20",font=("times new roman",22))
            self.Button4.grid(row=1,column=0)

            self.Button5=tk.Button(self.label10,text="Total Users",bg="lightblue",width="20",font=("times new roman",22))
            self.Button5.grid(row=2,column=0)

            self.Button6=tk.Button(self.label10,text="Deactivate user",bg="lightblue",width="20",font=("times new roman",22))
            self.Button6.grid(row=3,column=0)

            self.Button7=tk.Button(self.label10,text="Activate user",bg="lightblue",width="20",font=("times new roman",22))
            self.Button7.grid(row=4,column=0)
            
        else:  

            self.label2.place_forget()
            self.Bg_image= Image.open('D:/rack.jpg')
            self.new_size=(self.screen_width,self.screen_height)
            self.resized_image1=self.Bg_image.resize(self.new_size)
            self.back_image1=ImageTk.PhotoImage(self.resized_image1)
            self.label9=tk.Label(self.window,image=self.back_image1)
            self.label9.place(relwidth=1,relheight=1)

            self.Button3=tk.Button(self.label9,text="View Profile",bg="lightblue",width="20",font=("times new roman",22))
            self.Button3.grid(row=0,column=0)
            
            self.Button4=tk.Button(self.label9,text="Edit ptofile",bg="lightblue",width="20",font=("times new roman",22))
            self.Button4.grid(row=1,column=0)

            self.Button4=tk.Button(self.label9,text="Add Items",bg="lightblue",width="20",font=("times new roman",22))
            self.Button4.grid(row=2,column=0)

            self.Button4=tk.Button(self.label9,text="View cart",bg="lightblue",width="20",font=("times new roman",22))
            self.Button4.grid(row=3,column=0)

            self.Button4=tk.Button(self.label9,text="Categories",bg="lightblue",width="20",font=("times new roman",22))
            self.Button4.grid(row=4,column=0)

            self.Button5=tk.Button(self.label9,text="help",bg="lightblue",width="20",font=("times new roman",22))
            self.Button5.grid(row=5,column=0)

            self.Button6=tk.Button(self.label9,text="Decativate account",bg="red",width="20",font=("times new roman",22))
            self.Button6.grid(row=6,column=0)
            
             
if __name__=='__main__':
    app=tk.Tk()
    window=APP(app)
    app.mainloop()

