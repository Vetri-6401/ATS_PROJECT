import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image,ImageTk
import pymysql
import tksheet
import webbrowser


#initializing Graphical user iterface

class APP():
    def __init__(self,window):   
        self.window=window 
        self.screen_width=self.window.winfo_screenwidth()
        self.screen_height=self.window.winfo_screenheight()

        #setting up window properties

        window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.state("zoomed")
        window.iconbitmap("icon.ico")
        window.title("grocery store management")

        #Bacground image for signup frame

        self.signup_bg_image=Image.open("D:/kl.jpg")
        self.new_size=(self.screen_width,self.screen_height)
        self.resized_image=self.signup_bg_image.resize(self.new_size)
        self.back_image=ImageTk.PhotoImage(self.resized_image)
        self.label1=tk.Label(self.window,image=self.back_image)
        self.label1.place(relwidth=1,relheight=1)

        #Bacground image login frame

        self.Bg_image= Image.open('D:/hj.jpg')
        self.resized_image1=self.Bg_image.resize(self.new_size)
        self.back_image1=ImageTk.PhotoImage(self.resized_image1)
        self.label2=tk.Label(self.window,image=self.back_image1)

        #initializing the signup frame when initialize the window itself

        self.Signupframe()
        self.loginframe()
        self.data_base_connection()

    def Signupframe(self):

        #----------Labels and widgets that are are placed in signup frame-------------- 

        self.heading_Label1=tk.Label(self.label1,text="Sign Up Page",font=("timesnewroman",16),bg="orangered",bd=8,fg="white")
        self.heading_Label1.place(x=670,y=160)

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

        ''' The above Button --create an account will initiate the registration from the user '''

        self.Label6=tk.Label(self.label1,text="Already have an account?",bg="firebrick",fg="white",width="20",font=("times new roman",15))
        self.Label6.place(x=598,y=500)

        self.Button2=tk.Button(self.label1,text="Login",
                                bg="darkgreen",
                                height="1",
                                fg="white",
                                width="7",
                                font=("times new roman",11),
                                command=self.change_to_login_frame)
        self.Button2.place(x=825,y=499)

        ''' After clicking login button it will navigate to login frame '''

    def loginframe(self):

         #----------Labels and widgets that are are placed in Login Frame-------------- 

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
                               command=self.Validate_user_details)
        self.Button3.place(x=598,y=370)

        '''This login Button will navigate the user to their Main Dashboard page'''

        self.Label9=tk.Label(self.label2,text="Don't have an account?",
                             bg="green",fg="white",
                             width="20",height="1",
                             font=("times new roman",14))
        self.Label9.place(x=598,y=440)

        self.Button4=tk.Button(self.label2,text="Signup",bg="blue",
                               width="9",font=("times new roman",11),
                               fg="white",command=self.change_to_signupframe)
        self.Button4.place(x=805,y=438)

        '''After clicking this button login frame will disappear and navigate you to signup frame again'''

    def data_base_connection(self):

        self.connection =pymysql.connect(host="localhost", user="root",password="",database="grocerystore")
        self.my_cursor =self.connection.cursor()
        print("Database connected successfully")

        '''This method will help us to have an active connection to the "grocerystore" 
        database, we cancan use self.my_cursor 
        to execute SQL queries on this database.'''

    def Dashboard_Frame(self):

         #----------Labels and widgets that are are placed in User_Dahboard_Frame-------------- 

        self.frame1=tk.Frame(self.window,bg="lightsteelblue")
        self.frame1.pack(fill="both",expand=True)

        self.Button5=tk.Button(self.frame1,text="View Profile",bg="deepskyblue",width="20",fg="black",
                               font=("times new roman",14,"bold"),anchor=tk.W)
        self.Button5.grid(row=0,column=0)
            
        self.Button6=tk.Button(self.frame1,text="Edit ptofile",bg="deepskyblue",width="20",fg="black",
                               font=("times new roman",14,"bold"),anchor=tk.W)
        self.Button6.grid(row=1,column=0)

        self.Button7=tk.Button(self.frame1,text="View Stocks",bg="deepskyblue",width="20",fg="black",
                               font=("times new roman",14,"bold"),anchor=tk.W,
                                command=self.view_stocks)
        self.Button7.grid(row=2,column=0)

        '''After clicking add stocks button there will be floating window will appear to add items to the stock'''

        self.Button8=tk.Button(self.frame1,text="Add stock",bg="deepskyblue",width="20",fg="black",
                               font=("times new roman",14,"bold"),anchor=tk.W,
                               command=self.add_items)
        self.Button8.grid(row=3,column=0)

        '''After clicking View stocks button it will navigate to another frame which display the stocks available'''

        self.Button9=tk.Button(self.frame1,text="update/delete stock",bg="deepskyblue",width="20",fg="black",
                               font=("times new roman",14,"bold"),anchor=tk.W,
                               command=self.update_stocks_Frame)
        self.Button9.grid(row=4,column=0)

        '''After clicking View stocks button it will navigate to another frame where we can update and delete the stock details'''

        self.Button10=tk.Button(self.frame1,text="Generate Bill",bg="deepskyblue",width="20",fg="black",font=("times new roman",14,"bold"),anchor=tk.W)
        self.Button10.grid(row=5,column=0)

        self.Button11=tk.Button(self.frame1,text="help",bg="deepskyblue",width="20",fg="black",
                                font=("times new roman",14,"bold"),
                                anchor=tk.W,command=self.help)
        self.Button11.grid(row=6,column=0)
            
        self.Button12=tk.Button(self.frame1,text="Logout",bg="red",width="20",fg="black",
                                font=("times new roman",14,"bold"),anchor=tk.W,
                                command=self.Back_to_login_frame)
        self.Button12.grid(row=7,column=0) 

        '''Logout button will navigate the user to the LOGin page again'''  

        
    
    def Admin_page(self):

        self.frame2=tk.Frame(self.window,bg="lightsteelblue")
        self.frame2.pack(fill="both",expand=True)

        self.Button13=tk.Button(self.frame2,text="Admin profile",bg="deepskyblue",width="20",font=("times new roman",14,'bold'))
        self.Button3.grid(row=0,column=0)

        self.Button14=tk.Button(self.frame2,text="AccountDetails",bg="deepskyblue",width="20",font=("times new roman",14,'bold'))
        self.Button14.grid(row=1,column=0)

        self.Button15=tk.Button(self.frame2,text="Total Users",bg="deepskyblue",width="20",font=("times new roman",14,'bold'))
        self.Button15.grid(row=2,column=0)

        self.Button16=tk.Button(self.frame2,text="Deactivate user",bg="deepskyblue",width="20",font=("times new roman",14,'bold'))
        self.Button6.grid(row=3,column=0)

        self.Button17=tk.Button(self.frame2,text="Activate user",bg="deepskyblue",width="20",font=("times new roman",14,'bold'))
        self.Button7.grid(row=4,column=0)

        self.Entry4.delete(0,"end")
        self.Entry5.delete(0,"end")

    def insertData(self):
        try:
            name = self.Entry1.get()
            password = self.Entry2.get()
            mail = self.Entry3.get()


            query = f"SELECT user_name,user_mail FROM users"
            self.my_cursor.execute(query)
            data = self.my_cursor.fetchall()
            print(data)
            self.connection.commit()
            # self.my_cursor.close()
            # self.connection.close()

            # checking whether input details already exist in the database
            

            if name == "" or password == "":
                msg.showerror("Info error", "Please provide essential details")
            elif any(row[0].lower()== name.lower() for row in data):
                msg.showerror("Error", "Username already exists")
            elif any(row[1].lower() == mail.lower() for row in data):
                    msg.showerror("Error", "Email already exists")
            else:

                #if the entered details are not in the data base it will be added 

                query1 = f"INSERT INTO users (user_name, user_password, user_mail) VALUES ('{name}', '{password}', '{mail}')"
                self.my_cursor.execute(query1)
                self.connection.commit()
                msg.showinfo(title="Info", message="You have registered successfully")
                self.change_to_login_frame()

                self.Entry1.delete(0, "end")
                self.Entry2.delete(0, "end")
                self.Entry3.delete(0, "end")


        except:
            msg.showerror("Warning", "username or Email already exists")


    def change_to_login_frame(self):

        #Changing frame from signup to login

        self.label1.place_forget()
        self.label2.place(relwidth=1,relheight=1)

    def change_to_signupframe(self):

        #Changing frame from signup to login

        self.label2.place_forget()
        self.label1.place(relwidth=1,relheight=1)

    def Back_to_login_frame(self):

        #changing frame from dashboard to login

        self.frame1.pack_forget()
        self.label2.place(relwidth=1,relheight=1)

    def Validate_user_details(self):

        #login validation

        self.data_base_connection()
         
        #Getting the input from user then validate from the database

        username=self.Entry4.get()
        userpassword=self.Entry5.get()
        query2=f"SELECT user_password FROM users WHERE BINARY user_name='{username}'"
        self.my_cursor.execute(query2)
        result=self.my_cursor.fetchone()
        print(result)
        self.connection.commit()
        self.my_cursor.close()
        self.connection.close()

        '''SQL Query: The way you construct your SQL query can also impact whether the 
        search is case-sensitive. By default, SQL comparisons are usually case-insensitive, 
        but you can make them case-sensitive by using the BINARY keyword in your query.'''
        

        if result:
            user_db_password = result[0]
            print(user_db_password)    
            
            '''Assuming the password is stored in the first column of the result'''
           
            # Compare the provided password with the stored password
            if userpassword == user_db_password:
                msg.showinfo("Info","Login successful")
                self.Dashboard_Frame()
                self.Entry4.delete(0, "end")
                self.Entry5.delete(0, "end")
                
            else:
                msg.showerror("error","Invalid password")

        else:
            msg.showerror("error","Invalid user")

    def view_stocks(self):

        #initiate database_connection

        self.data_base_connection()
        items = 'select * from items_stock'
        self.my_cursor.execute(items)
        Data1= self.my_cursor.fetchall()

        self.frame1.pack_forget()
        self.frame2=tk.Frame(self.window,bg="lightsteelblue")
        self.frame2.pack(fill="both",expand=True)

        self.Label15=ttk.Label(self.frame2,text="select Category",background="lightgreen",font=("timesnewroman",12,"bold"))
        self.Label15.grid(row=0,column=1,columnspan=2)

        self.Category=["All","cereal product","cooldrinks","dairy","personalcare","BabyItems","petcare","condiments&spices","icecreams","vegetable"]

        #creating a dropdown list for categories

        self.combo_box=ttk.Combobox(self.frame2,values=self.Category)
        self.combo_box.set(self.Category[0])
        self.combo_box.grid(row=2,column=1,columnspan=2)
        self.combo_box.bind('<<ComboboxSelected>>',lambda event:self.viewstock(event))

        self.style=ttk.Style()

        #pick a theme

        self.style.theme_use("clam")
    
        #Creating a table view using treeview

        self.tree=ttk.Treeview(self.frame2,height=30)
        self.tree["show"]="headings"


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

        self.tree.grid(row=4,column=0)

        self.btn1=tk.Button(self.frame2,text="Back",bg="green",font=("timesnewroman",14),command=self.Back_to_Dashboard)
        self.btn1.grid(row=25,column=0)

        '''This above button will call the back to dashboard navigate the dashboard page again'''
        
    def viewstock(self, event):

        #Filtering the categories based on the selected list

        selected_category = self.combo_box.get()
        items = 'SELECT * FROM items_stock'
        
        if selected_category != 'All':
            items = f' select * FROM items_stock WHERE Category = "{selected_category}"'
        
        self.my_cursor.execute(items)
        data2= self.my_cursor.fetchall()
        
        # Clear existing data in the Treeview

        for item in self.tree.get_children():
            self.tree.delete(item)
        
        i = 0
        for row in data2:
            self.tree.insert("", i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
            i += 1
    
    def Back_to_Dashboard(self):
        
        #changing frame to dashboard from view stock frame

        self.frame2.pack_forget()
        self.frame1.pack(fill="both",expand=True)

    def add_items(self): 

        #floating window for upadting details 

        self.float1=Toplevel(self.window)
        self.float1.geometry("550x350")
        self.float1.resizable(False,False)
        self.float1.configure(bg="lightblue")
        self.float1.title("Add stocks")

        #label and widgets containing in float window to add items
        

        self.Label10=tk.Label(self.float1,bg="#00C957",text="Add items",fg="white",font=("timenewroman",16,'bold'),relief=FLAT)
        self.Label10.grid(row=0,column=1)

        self.Category1=["All","cereal product","cooldrinks","dairy","personalcare","BabyItems","petcare","condiments&spices","icecreams","vegetable"]
        self.combo_box1=ttk.Combobox(self.float1,values=self.Category1,font=("timesnewroman",16))
        self.combo_box1.set(self.Category1[0])

        self.Label11=tk.Label(self.float1,text="Item name",bg="lightgrey",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label11.grid(row=2,column=0)

        self.Entry6=tk.Entry(self.float1,width="29",font=("timesnewroman",14))
        self.Entry6.grid(row=2,column=1)

        self.Label12=tk.Label(self.float1,text="price",bg="lightgrey",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label12.grid(row=4,column=0)

        self.Entry7=tk.Entry(self.float1,width="29",font=("timesnewroman",14))
        self.Entry7.grid(row=4,column=1)
        
        self.Label13=tk.Label(self.float1,text="Quantity",bg="lightgrey",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label13.grid(row=6,column=0)

        self.Entry8=tk.Entry(self.float1,width="29",font=("timesnewroman",14))
        self.Entry8.grid(row=6,column=1)

        self.Label14=tk.Label(self.float1,bg="lightgrey",text="Category",width="15",font=("timenewroman",14),relief=GROOVE,anchor=W)
        self.Label14.grid(row=10,column=0)

        self.combo_box1.grid(row=10,column=1)
      
        self.btn2=tk.Button(self.float1,text="Add to stock",bg="green",width="10",command=self.add_stock)
        self.btn2.grid(row=16,column=0)

        self.combo_box1.bind('<<ComboboxSelected>>',self.addstock)


    def addstock(self,event=None):

        '''will be called when user user select the category in folating window'''

        #getting the value of selected category

        self.Category1=self.combo_box1.get()
        print(self.Category1)

    def add_stock(self):

        '''This method will be called when user click the add_to_stock_button the floating window'''


        #New stock details will be added to the database

        self.data_base_connection()
        item_name=self.Entry6.get()
        price=self.Entry7.get()
        quantity=self.Entry8.get()
        
        item=f'insert into items_stock(category,item_name,price,amount,stock_available) values("{self.Category1}","{item_name}",{price},"rs",{quantity})'
        self.my_cursor.execute(item)
        self.connection.commit()
        
        self.my_cursor.close()
        self.connection.close()


        self.Entry6.delete(0,"end")
        self.Entry7.delete(0,"end")
        self.Entry8.delete(0,"end")
        msg.showinfo("info","Added successfully")

        self.add_items()

    def update_stocks_Frame(self):

        #The required table and widgets are placed inside the frame3

        self.data_base_connection()
        items = 'select * from items_stock'
        self.my_cursor.execute(items)
        Data1= self.my_cursor.fetchall()

        self.frame1.pack_forget()
        self.frame3=tk.Frame(self.window,bg="lightsteelblue")
        self.frame3.pack(fill="both",expand=True)

        self.Label15=ttk.Label(self.frame3,text="select Category",background="lightgreen",font=("timesnewroman",12,"bold"))
        self.Label15.grid(row=0,column=1,columnspan=2)

        # Label2=ttk.Label(window,text="")
        # Label2.place(x=0,y=50)
        self.Category2=["All","cooldrinks","dairy","personalcare","BabyItems","petcare","condiments&spices","icecreams","vegetable"]

        self.combo_box2=ttk.Combobox(self.frame3,values=self.Category2)
        self.combo_box2.set(self.Category2[0])
        self.combo_box2.grid(row=1,column=1,columnspan=2)
        self.combo_box2.bind('<<ComboboxSelected>>',lambda event:self.update_stock_filter(event))

        self.style=ttk.Style()

        #pick a theme
        self.style.theme_use("clam")
    
        self.tree1=ttk.Treeview(self.frame3,height=30)
        self.tree1["show"]="headings"


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

        #adding the data to the table view(treeview)
        
        for row in Data1:
            self.tree1.insert("",i,text="",values=(row[0],row[1],row[2],row[3],row[4])) #parent="",text=""
            i=i+1

        self.tree1.grid(row=2,column=0)

        self.btn3=tk.Button(self.frame3,text="SELECT",bg="green",font=("timenewroman",12),width="10",command=self.selected_item)
        self.btn3.grid(row=20,column=0)

        self.frame4=tk.Frame(self.frame3)
        self.frame4.grid(row=2,column=20)
        
        self.Label16=tk.Label(self.frame4,text="Category",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label16.grid(row=0,column=0)

        self.Entry9=tk.Entry(self.frame4,width="25",font=("timesnewroman",13),bg="lightgrey")
        self.Entry9.grid(row=0,column=1)

        self.Label17=tk.Label(self.frame4,text="Item name",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label17.grid(row=1,column=0)

        self.Entry10=tk.Entry(self.frame4,width="25",font=("timesnewroman",13),bg="lightgrey")
        self.Entry10.grid(row=1,column=1)

        self.Label17=tk.Label(self.frame4,text="price",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label17.grid(row=2,column=0)

        self.Entry11=tk.Entry(self.frame4,width="25",font=("timesnewroman",13),bg="lightgrey")
        self.Entry11.grid(row=2,column=1)

        self.Label18=tk.Label(self.frame4,text="quantity",bg="lightgrey",width="15",font=("timenewroman",13),relief=GROOVE,anchor=W)
        self.Label18.grid(row=3,column=0)

        self.Entry12=tk.Entry(self.frame4,width="25",font=("timesnewroman",13),bg="lightgrey")
        self.Entry12.grid(row=3,column=1)

        self.btn4=tk.Button(self.frame4,text="UPDATE",bg="magenta2",width="10",height="1",command=self.update_stock)
        self.btn4.grid(row=6,column=0)

        '''The above update button will call the update_stock methods that process the updation of the selected data'''

        self.btn5=tk.Button(self.frame4,text="DELETE",bg="red",command=self.delete_stock)
        self.btn5.grid(row=6,column=1)

        '''This delete button will call the delete_stock method that remove the selected data from the database'''

        self.btn6=tk.Button(self.frame4,text="RESET",bg="blue",command=self.reset_details)
        self.btn6.grid(row=6,column=2,columnspan=2)

        self.btn7=tk.Button(self.frame3,text="Back",bg="orange",font=("timesnewroman",12),command=self.Back_to_Dashboard1)
        self.btn7.grid(row=22,column=0)
        
    def update_stock_filter(self, event):
        selected_category = self.combo_box2.get()
        items = 'SELECT * FROM items_stock'
        
        if selected_category != 'All':
            items = f' select * FROM items_stock WHERE Category = "{selected_category}"'
        
        self.my_cursor.execute(items)
        data2= self.my_cursor.fetchall()
        
        # Clear existing data in the Treeview
        for item in self.tree1.get_children():
            self.tree1.delete(item)
        
        i = 0
        for row in data2:
            self.tree1.insert("", i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
            i += 1

    def selected_item(self):

        '''select the data from the tree view for update/delete'''

        selected_item=self.tree1.focus()
        details=self.tree1.item(selected_item,"values")

        print(details)

        self.Entry9.insert(0,details[0])
        self.Entry10.insert(0,details[1])
        self.Entry11.insert(0,details[2])
        self.Entry12.insert(0,details[4])

    def update_stock(self):

        #modified details will be updated using this method

        self.data_base_connection()

        category = self.Entry9.get()
        item_name = self.Entry10.get()
        price = self.Entry11.get()  # Corrected variable
        quantity = self.Entry12.get()  # Corrected variable

        query = f'UPDATE items_stock SET category = "{category}", price = {price}, stock_available = {quantity} WHERE item_name = "{item_name}"'

        try:
            self.my_cursor.execute(query)
            self.connection.commit()
            # self.my_cursor.close()
            # self.connection.close()
            msg.showinfo("update","details has been updated")
            self.Entry9.delete(0,"end")
            self.Entry10.delete(0,"end")
            self.Entry11.delete(0,"end")
            self.Entry12.delete(0,"end")
           
        except Exception as e:
            print(f"Error: {e}")    

    def delete_stock(self):

        #selected data will be deleted from the database

        self.data_base_connection()

        category = self.Entry9.get()
        item_name = self.Entry10.get()
        price = self.Entry11.get()  # Corrected variable
        quantity = self.Entry12.get()  # Corrected variable
    
        query1= f'delete from items_stock where item_name="{item_name}"'

        try:
            
            self.my_cursor.execute(query1)
            self.connection.commit()
            # self.my_cursor.close()
            # self.connection.close()
            msg.showinfo("delted","item deleted from stock")

            self.Entry9.delete(0,"end")
            self.Entry10.delete(0,"end")
            self.Entry11.delete(0,"end")
            self.Entry12.delete(0,"end")
           
        except Exception as e:
            print(f"Error: {e}")  
    
    def reset_details(self):

        #clear the current details  if user want to select other data

        self.Entry9.delete(0,"end")
        self.Entry10.delete(0,"end")
        self.Entry11.delete(0,"end")
        self.Entry12.delete(0,"end")

       
    def Back_to_Dashboard1(self):

        #Frame will changes from update/delete details frame to dashboard frame

        self.frame3.pack_forget()
        self.frame1.pack(fill="both",expand=True)

    
    def help (self):

        '''This floating window has the developer details and ccode and functionality of the grocery app '''

        self.float2=Toplevel(self.window)
        self.float2.geometry("250x250")
        self.float2.resizable(False,False)
        self.float2.configure(bg="lightblue")
        self.float2.title("help")

        self.label1_help=tk.Label(self.float2,text="Developer name: Vetrivel C ")
        self.label2_help=tk.Label(self.float2,text="Skills: Python , SQL ")
        self.label3_help=tk.Label(self.float2,text="Email: vetrivel6401@gmail.com ")
        self.label4_help=tk.Label(self.float2,text="phone: XXXXXXXX4806  ")

        self.label1_help.pack(padx="10",pady="10",anchor=W)
        self.label2_help.pack(padx="10",pady="10",anchor=W)
        self.label3_help.pack(padx="10",pady="10",anchor=W)
        self.label4_help.pack(padx="10",pady="10",anchor=W)

        self.button_help = tk.Button(self.float2, text="Open help file",bg="green", command=self.open_google_drive_link)
        self.button_help.pack(padx="10",pady="10")


    # Function to open the Google Drive link in a web browser
    
    def open_google_drive_link(self):

        self.url = "https://drive.google.com/file/d/1tkcvQ6jJXKhpza1X3UwLZQj6yI_ofBN7/view?usp=drive_link"
        webbrowser.open_new(self.url)


if __name__=='__main__':
    app=tk.Tk()
    window=APP(app)
    app.mainloop()