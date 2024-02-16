import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image,ImageTk
import mysql.connector
import tksheet

class APP():
    def __init__(self,window):   #window=tk.TK()
        self.window=window #tk.TK()
        self.screen_width=self.window.winfo_screenwidth()
        self.screen_height=self.window.winfo_screenheight()
        window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.state("zoomed")
        window.iconbitmap("icon.ico")
        window.title("grocery store management")

        
        self.signup_bg_image=Image.open("D:/kl.jpg")
        self.new_size=(self.screen_width,self.screen_height)
        self.resized_image=self.signup_bg_image.resize(self.new_size)
        self.back_image=ImageTk.PhotoImage(self.resized_image)
        self.label1=tk.Label(self.window,image=self.back_image)
        self.label1.place(relwidth=1,relheight=1)

        self.Bg_image= Image.open('D:/hj.jpg')
        self.resized_image1=self.Bg_image.resize(self.new_size)
        self.back_image1=ImageTk.PhotoImage(self.resized_image1)
        self.label2=tk.Label(self.window,image=self.back_image1)

        self.Signupframe()
        self.loginframe()
        self.data_base_connection()
       

    def Signupframe(self):

        #----------Labels and widgets that are are placed in signup frame-------------- 

        self.heading_Label2=tk.Label(self.label1,text="Sign Up Page",font=("timesnewroman",16),bg="orangered",bd=8,fg="white")
        self.heading_Label2.place(x=670,y=160)

        self.Label3=tk.Label(self.label1,text="Username",bg="Deeppink",fg="white",width="10",font=("times new roman",14))
        self.Label3.place(x=600,y=250)

        self.Label4=tk.Label(self.label1,text="password",bg="Deeppink",fg="white",width="10",font=("times new roman",14))
        self.Label4.place(x=600,y=310)

        self.Label5=tk.Label(self.label1,text="Email",bg="Deeppink",fg="white",width="10",font=("times new roman",14))
        self.Label5.place(x=600,y=370)

        self.Entry1=tk.Entry(self.label1,width="29",bg="deepskyblue")
        self.Entry1.place(x=707,y=250,height="28")

        self.Entry2=tk.Entry(self.label1,width="29",bg="deepskyblue")
        self.Entry2.place(x=707,y=310,height="28")

        self.Entry3=tk.Entry(self.label1,width="29",bg="deepskyblue")
        self.Entry3.place(x=707,y=370,height="28")

        self.Button1=tk.Button(self.label1,text="Create an account",
                               bg="DarkOrchid4",
                               fg="white",width="28",
                               font=("times new roman",14),
                               command=self.insertData)
        self.Button1.place(x=598,y=430)

        """The above Button --create an account will initiate the registration from the user"""

        self.Label6=tk.Label(self.label1,text="Already have an account?",bg="firebrick",fg="white",width="20",font=("times new roman",15))
        self.Label6.place(x=598,y=500)

        self.Button2=tk.Button(self.label1,text="Login",
                               bg="darkgreen",
                               height="1",
                               fg="white",
                               width="7",
                               font=("times new roman",11),
                               command=self.changeframe)
        self.Button2.place(x=825,y=499)

        ''' After clicking login button it will navigate to login frame '''

    def loginframe(self):

        self.heading_Label2=tk.Label(self.label2,text="Login page",font=("timesnewroman",14),bg="darkgreen",bd=8,fg="white")
        self.heading_Label2.place(x=670,y=160)

        self.Label7=tk.Label(self.label2,text="User_name",bg="#39FF14",width="10",font=("times new roman",14,"bold"))
        self.Label7.place(x=600,y=250)

        self.Label8=tk.Label(self.label2,text="password",bg="#39FF14",width="10",font=("times new roman",14,"bold"))
        self.Label8.place(x=600,y=310)

        self.Entry4=tk.Entry(self.label2,width="29")
        self.Entry4.place(x=707,y=250,height="28")

        self.Entry5=tk.Entry(self.label2,width="29")
        self.Entry5.place(x=707,y=310,height="28")

        self.Button3=tk.Button(self.label2,text="Login",
                               bg="#F535AA",width="25",
                               fg="white",font=("times new roman",14,'bold'),
                               command=self.mainpage)
        self.Button3.place(x=598,y=370)

        self.Label9=tk.Label(self.label2,text="Don't have an account?",
                             bg="green",fg="white",
                             width="20",height="1",
                             font=("times new roman",14))
        self.Label9.place(x=598,y=440)

        self.Button4=tk.Button(self.label2,text="Signup",bg="blue",width="9",font=("times new roman",11),fg="white",command=self.changeframe1)
        self.Button4.place(x=805,y=438)
       

    def data_base_connection(self):
        self.connection =mysql.connector.connect(host="localhost", user="root",password="",database="grocerystore")
        self.my_cursor =self.connection.cursor()

        '''you will have an active connection to the "grocerystore" 
        database, and you can use self.my_cursor 
        to execute SQL queries on this database.'''
 
    def insertData(self):

        try:

            name=self.Entry1.get()
            password=self.Entry2.get()
            mail=self.Entry3.get()
            # if name=="" or password=="":
            #     msg.showerror("info error","Please provide essential details")
          
            sql=f"INSERT INTO users (user_name,user_password,user_mail) VALUES ('{name}', '{password}','{mail}')"
            self.my_cursor.execute(sql)
            self.connection.commit()
            self.my_cursor.close()
            self.connection.close()

            msg.showinfo(title="Info",message="You have registed successfully")

            self.label1.place_forget()
            self.label2.place(relwidth=1,relheight=1)

            self.Entry1.delete(0,"end")
            self.Entry2.delete(0,"end")
            self.Entry3.delete(0,"end")
         
        except:

            msg.showerror("Warning","Username already Exist")


    def changeframe(self):
        self.label1.place_forget()
        self.label2.place(relwidth=1,relheight=1)
        
    def changeframe1(self):
        
        self.label2.place_forget()
        self.label1.place(relwidth=1,relheight=1)

    def mainpage(self):

        self.data_base_connection()
        user_name=self.Entry4.get()
        user_password=self.Entry5.get()
        sql=f"select * from users where user_name='{user_name}' and user_password='{user_password}'"
        self.my_cursor.execute(sql)
        data=self.my_cursor.fetchone()
        self.my_cursor.close()
        self.connection.close()

        if user_name=="Admin" and user_password=="Admin@1234":

            msg.showinfo("User Verfied Status","Login Successfully")

            self.label2.place_forget()
            self.Bg_image= Image.open('D:/database.jpg')    
            self.new_size=(self.screen_width,self.screen_height)
            self.resized_image1=self.Bg_image.resize(self.new_size)
            self.back_image1=ImageTk.PhotoImage(self.resized_image1)
            self.label10=tk.Label(self.window,image=self.back_image1)
            self.label10.place(relwidth=1,relheight=1)

            self.Button3=tk.Button(self.label10,text="Admin profile",bg="darkorange",width="20",font=("times new roman",22))
            self.Button3.grid(row=0,column=0)

            self.Button4=tk.Button(self.label10,text="AccountDetails",bg="darkorange",width="20",font=("times new roman",22))
            self.Button4.grid(row=1,column=0)

            self.Button5=tk.Button(self.label10,text="Total Users",bg="darkorange",width="20",font=("times new roman",22))
            self.Button5.grid(row=2,column=0)

            self.Button6=tk.Button(self.label10,text="Deactivate user",bg="darkorange",width="20",font=("times new roman",22))
            self.Button6.grid(row=3,column=0)

            self.Button7=tk.Button(self.label10,text="Activate user",bg="darkorange",width="20",font=("times new roman",22))
            self.Button7.grid(row=4,column=0)

            self.Entry3.delete(0,"end")
            self.Entry4.delete(0,"end")

        elif not(data==None):
             
            msg.showinfo("User Verfied Status","Login Successfully")

            self.label2.place_forget()

            self.frame1=tk.Frame(self.window,bg="lightsteelblue")
            self.frame1.pack(fill="both",expand=True)

            self.Button3=tk.Button(self.frame1,text="View Profile",bg="deepskyblue",width="20",fg="white",font=("times new roman",14,"bold"),anchor=tk.W)
            self.Button3.grid(row=0,column=0)
            
            self.Button4=tk.Button(self.frame1,text="Edit ptofile",bg="deepskyblue",width="20",fg="black",font=("times new roman",14,"bold"),anchor=tk.W)
            self.Button4.grid(row=1,column=0)

            self.Button4=tk.Button(self.frame1,text="Add Stocks",bg="deepskyblue",width="20",fg="black",
                                   font=("times new roman",14,"bold"),
                                   anchor=tk.W,
                                   command=self.add_items)
            self.Button4.grid(row=2,column=0)

            self.Button4=tk.Button(self.frame1,text="View_stock",bg="deepskyblue",width="20",fg="black",
                                   font=("times new roman",14,"bold"),
                                   anchor=tk.W,
                                   command=self.view_items)
            self.Button4.grid(row=3,column=0)

            self.Button4=tk.Button(self.frame1,text="update stock",bg="deepskyblue",width="20",fg="black",font=("times new roman",14,"bold"),anchor=tk.W,command=self.update_item_details)
            self.Button4.grid(row=4,column=0)

            self.Button5=tk.Button(self.frame1,text="help",bg="deepskyblue",width="20",fg="black",font=("times new roman",14,"bold"),anchor=tk.W)
            self.Button5.grid(row=5,column=0)

            self.Button6=tk.Button(self.frame1,text="Generate Bill",bg="deepskyblue",width="20",fg="black",font=("times new roman",14,"bold"),anchor=tk.W,command=self.invoice)
            self.Button6.grid(row=6,column=0)
            
            self.Button7=tk.Button(self.frame1,text="Logout",bg="red",width="20",fg="black",font=("times new roman",14,"bold"),anchor=tk.W,command=self.backframe)
            self.Button7.grid(row=7,column=0)

        else:
            msg.showerror("User Verfied Status","Login error ,Invalid credentials")


    def view_items(self): 

        self.data_base_connection()
        items = 'select * from items_stock'
        self.my_cursor.execute(items)
        Data1= self.my_cursor.fetchall()

        self.frame1.pack_forget()
        self.frame2=tk.Frame(self.window,bg="lightsteelblue")
        self.frame2.pack(fill="both",expand=True)

        self.Label15=ttk.Label(self.frame2,text="select Category")
        self.Label15.grid(row=0,column=1,columnspan=2)

        # Label2=ttk.Label(window,text="")
        # Label2.place(x=0,y=50)
        Category=["All","cooldrinks","dairy","personalcare"]

        self.combo_box=ttk.Combobox(self.frame2,values=Category)
        self.combo_box.set(Category[0])
        self.combo_box.grid(row=1,column=1)
        self.combo_box.bind('<<ComboboxSelected>>',lambda event:self.viewstock(event))

        self.tree=ttk.Treeview(self.frame2,height=30)
        self.tree["show"]="headings"

        self.style=ttk.Style(self.window)
        self.style.theme_use("clam")

        self.tree["columns"]=("Category","Item_name","price","amount","stock_available")

        self.tree.column("Category",width=100,minwidth=50,anchor=tk.W)  #cant resize smaller than 50
        self.tree.column("Item_name",width=100,minwidth=50,anchor=tk.W)
        self.tree.column("price",width=100,minwidth=50,anchor=tk.CENTER)
        self.tree.column("amount",width=100,minwidth=50,anchor=tk.CENTER)
        self.tree.column("stock_available",width=100,minwidth=50,anchor=tk.W)

        #assigning headings to columns

        self.tree.heading("Category",text="Category",anchor=tk.W)
        self.tree.heading("Item_name",text="Item_name",anchor=tk.W)
        self.tree.heading("price",text="price",anchor=tk.CENTER)
        self.tree.heading("amount",text="price",anchor=tk.CENTER)
        self.tree.heading("stock_available",text="stock_available",anchor=tk.W)

        i=0

        for row in Data1:
            self.tree.insert("",i,text="",values=(row[0],row[1],row[2],row[3],row[4])) #parent="",text=""
            i=i+1

        self.tree.grid(row=2,column=0)

        self.btn3=tk.Button(self.frame2,text="Back",bg="green",command=self.home)
        self.btn3.pack()

    def viewstock(self,event):

        selected_data=self.combo_box.get()
            # Label2.configure(text=f"You have selected :\n {selected_data}")

        print(selected_data)   


    def backframe(self):
        self.frame1.pack_forget()
        self.label2.place(relwidth=1,relheight=1)

    def home(self):
        self.frame2.pack_forget()
        self.frame1.pack(fill="both",expand=True)

    def homeagain(self):
        self.frame3.pack_forget()
        self.frame1.pack(fill="both",expand=True)

    def add_items(self): #popup window
        self.float1=Toplevel(self.window)
        self.float1.geometry("550x350")
        self.float1.resizable(False,False)
        self.float1.configure(bg="lightblue")
        self.float1.title("Add stocks")
        # self.float1.eval('tk::placewindow.center')

        self.Label11=tk.Label(self.float1,bg="#00C957",text="Add items",fg="white",font=("timenewroman",16,'bold'),relief=FLAT)
        self.Label11.grid(row=0,column=1)

        Category=["All","cooldrinks","dairy","personalcare","condiments&spices","Babyitems","Icecreams","canned items","oil"]
        self.combo_box=ttk.Combobox(self.float1,values=Category,font=("timesnewroman",16))
        self.combo_box.set(Category[0])
        

        self.Label13=tk.Label(self.float1,text="Item name",bg="lightgrey",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label13.grid(row=2,column=0)

        self.Entry6=tk.Entry(self.float1,width="29",font=("timesnewroman",14))
        self.Entry6.grid(row=2,column=1)
        

        self.Label14=tk.Label(self.float1,text="price",bg="lightgrey",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label14.grid(row=4,column=0)

        self.Entry7=tk.Entry(self.float1,width="29",font=("timesnewroman",14))
        self.Entry7.grid(row=4,column=1)
        
        self.Label15=tk.Label(self.float1,text="Quantity",bg="lightgrey",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label15.grid(row=6,column=0)

        self.Entry8=tk.Entry(self.float1,width="29",font=("timesnewroman",14))
        self.Entry8.grid(row=6,column=1)

        self.Label12=tk.Label(self.float1,bg="lightgrey",text="Category",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label12.grid(row=10,column=0)

        self.combo_box.grid(row=10,column=1)
      
        self.btn4=tk.Button(self.float1,text="Add to stock",bg="green",width="10",command=self.add_stock)
        self.btn4.grid(row=16,column=0)

        self.combo_box.bind('<<ComboboxSelected>>',self.addstock)


    def addstock(self,event=None):
        self.category=self.combo_box.get()
        print(self.category)

    def add_stock(self):
        self.data_base_connection()

       
        item_name=self.Entry6.get()
        price=self.Entry7.get()
        quantity=self.Entry8.get()
        
        item=f'insert into items_stock(category,item_name,price,amount,stock_available) values("{self.category}","{item_name}",{price},"rs",{quantity})'
        self.my_cursor.execute(item)
        self.connection.commit()
        
        self.my_cursor.close()
        self.connection.close()


        self.Entry6.delete(0,"end")
        self.Entry7.delete(0,"end")
        self.Entry8.delete(0,"end")
        msg.showinfo("info","Added successfully")

        self.add_items()

    def update_item_details(self):

        self.data_base_connection()
        items1= 'select * from items_stock'
        self.my_cursor.execute(items1)
        Data2= self.my_cursor.fetchall()
    
        self.frame1.pack_forget()
        self.frame3=tk.Frame(self.window,bg="lightsteelblue",width=self.screen_width,height=self.screen_height)
        self.frame3.pack(fill="both",expand=True)

        self.tree1=ttk.Treeview(self.frame3,height=30)
        self.tree1["show"]="headings"

        self.style=ttk.Style(self.frame3)
        self.style.theme_use("clam")

        self.tree1["columns"]=("Category","Item_name","price","amount","stock_available")

        self.tree1.column("Category",width=100,minwidth=50,anchor=tk.W)  #cant resize smaller than 50
        self.tree1.column("Item_name",width=100,minwidth=50,anchor=tk.W)
        self.tree1.column("price",width=100,minwidth=50,anchor=tk.CENTER)
        self.tree1.column("amount",width=100,minwidth=50,anchor=tk.CENTER)
        self.tree1.column("stock_available",width=100,minwidth=50,anchor=tk.W)

        #assigning headings to columns

        self.tree1.heading("Category",text="Category",anchor=tk.W)
        self.tree1.heading("Item_name",text="Item_name",anchor=tk.W)
        self.tree1.heading("price",text="price",anchor=tk.CENTER)
        self.tree1.heading("amount",text="price",anchor=tk.CENTER)
        self.tree1.heading("stock_available",text="stock_available",anchor=tk.W)

        i=0

        for row in Data2:
            self.tree1.insert("",i,text="",values=(row[0],row[1],row[2],row[3],row[4])) #parent="",text=""
            i=i+1

        self.tree1.grid(row=1,column=0)   

        self.btn4=tk.Button(self.frame3,text="SELECT",bg="green",width="10",command=self.selected_item)
        self.btn4.grid(row=20,column=0)

        self.frame4=tk.Frame(self.frame3)
        self.frame4.grid(row=1,column=20)
        
        self.Label16=tk.Label(self.frame4,text="Category",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label16.grid(row=0,column=0)

        self.Entry9=tk.Entry(self.frame4,width="29",font=("timesnewroman",13),bg="lightgrey")
        self.Entry9.grid(row=0,column=1)

        self.Label17=tk.Label(self.frame4,text="Item name",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label17.grid(row=1,column=0)

        self.Entry10=tk.Entry(self.frame4,width="29",font=("timesnewroman",13),bg="lightgrey")
        self.Entry10.grid(row=1,column=1)

        self.Label17=tk.Label(self.frame4,text="price",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label17.grid(row=2,column=0)

        self.Entry11=tk.Entry(self.frame4,width="29",font=("timesnewroman",13),bg="lightgrey")
        self.Entry11.grid(row=2,column=1)

        self.Label18=tk.Label(self.frame4,text="quantity",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label18.grid(row=3,column=0)

        self.Entry12=tk.Entry(self.frame4,width="29",font=("timesnewroman",13,),bg="lightgrey")
        self.Entry12.grid(row=3,column=1)

        self.btn4=tk.Button(self.frame4,text="UPDATE",bg="magenta2",width="10",height="1",command=self.update)
        self.btn4.grid(row=4,column=0)

        self.btn5=tk.Button(self.frame4,text="DELETE",bg="red",command=self.delete)
        self.btn5.grid(row=4,column=1,columnspan=2)

        self.btn3=tk.Button(self.frame3,text="Back",bg="orange",command=self.homeagain)
        self.btn3.grid(row=22,column=0)

        
    def invoice(self):
        self.frame2.pack_forget()

    def selected_item(self):

        selected_item=self.tree1.focus()
        details=self.tree1.item(selected_item,"values")

        print(details)

        self.Entry9.insert(0,details[0])
        self.Entry10.insert(0,details[1])
        self.Entry11.insert(0,details[2])
        self.Entry12.insert(0,details[4])

    def update(self):
        self.data_base_connection()

        category = self.Entry9.get()
        item_name = self.Entry10.get()
        price = self.Entry11.get()  # Corrected variable
        quantity = self.Entry12.get()  # Corrected variable

        query = f'UPDATE items_stock SET category = "{category}", price = {price}, stock_available = {quantity} WHERE item_name = "{item_name}"'

        try:
            self.my_cursor.execute(query)
            self.connection.commit()
            self.my_cursor.close()
            self.connection.close()
            msg.showinfo("update","details has been updated")
            self.Entry9.delete(0,"end")
            self.Entry10.delete(0,"end")
            self.Entry11.delete(0,"end")
            self.Entry12.delete(0,"end")
           
        except Exception as e:
            print(f"Error: {e}")

    def delete(self):
        self.data_base_connection()

        category = self.Entry9.get()
        item_name = self.Entry10.get()
        price = self.Entry11.get()  # Corrected variable
        quantity = self.Entry12.get()  # Corrected variable
    
        query1= f'delete from items_stock where item_name="{item_name}"'

        try:
            self.my_cursor.execute(query1)
            self.connection.commit()
            self.my_cursor.close()
            self.connection.close()
            msg.showinfo("delted","item deleted from stock")

            self.Entry9.delete(0,"end")
            self.Entry10.delete(0,"end")
            self.Entry11.delete(0,"end")
            self.Entry12.delete(0,"end")
           
        except Exception as e:
            print(f"Error: {e}")

            
if __name__=='__main__':
    app=tk.Tk()
    window=APP(app)
    app.mainloop()