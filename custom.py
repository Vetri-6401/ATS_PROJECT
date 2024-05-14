import customtkinter as ctk 
import datetime 
import CTkMessagebox
from CTkMessagebox import *
from datetime import datetime
import start_ldap
from otp_generate import generate_otp
from pwd_change import reset_password
import time

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("437x400+750+550")
        self.title("Fnet Services") 

        self.frame = ctk.CTkFrame(master=self) 
        self.frame.pack(pady=30, padx=30, fill='both', expand=True) 

        self.Login_Label=ctk.CTkLabel(master=self.frame,text='Login page',font=("",18),corner_radius=10)
        self.Login_Label.pack(pady=10,padx=10)

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text=" Enter Employee Id ",width=250,height=35,font=("",13)) 
        self.user_entry.pack(pady=12, padx=5) 

        self.user_pass = ctk.CTkEntry(master=self.frame, placeholder_text=" Enter OTP ", show="*",width=250,height=35,font=("",13)) 
        

        self.button_otp = ctk.CTkButton(master=self.frame, text=' Generate OTP ', command=self.generate_login_otp,width=250,height=35,font=("",13)) 
        self.button_otp.pack(pady=12,padx=5) 

        self.button_login = ctk.CTkButton(master=self.frame, text=' Login ', command=self.login,fg_color='green',width=250,height=35,font=("",13)) 
        try:
            self.user_id,self.user_mail=start_ldap.start_server()
        except Exception as e:
            CTkMessagebox(master=self,title='Error',message='Something Went Wrong',icon='cancel',width=200,height=100)
        
        self.current_step = 'login'
        self.sessions={}

    def generate_login_otp(self):
        self.Emp_id=self.user_entry.get()
        self.sessions['Emp_id']=self.Emp_id
        if self.Emp_id:
            if self.Emp_id in self.user_id.keys():
                self.button_otp.configure(text=' Resend  OTP ')
                self.user_dn_name=self.user_id[self.Emp_id]
                self.Emp_mail=self.user_mail[self.Emp_id]
                self.send_OTP()
                
            else:
                CTkMessagebox(master=self,title='Error',message='Emp Id Not Found',icon='cancel',width=200,height=100)
        else:
            CTkMessagebox(master=self,title="Invalid Input ", message="Please Enter Emp id",
                  icon="info",option_1='ok',width=250,height=150)
    
    def send_OTP(self):
        try:
            self.system_otp=generate_otp(self.Emp_mail)
            self.sessions['system_otp']=self.system_otp
            print(self.system_otp)
            self.user_entry.configure(state='disabled')
            self.button_otp.pack_forget()
            self.user_pass.pack(pady=12, padx=5) 
            self.button_otp.pack(pady=12,padx=5)
            self.button_login.pack(pady=12,padx=5) 
            CTkMessagebox(master=self,title='Info',message=f'OTP has been sent to {self.Emp_mail}',icon='info',width=210,height=100)
        except Exception as e:
            CTkMessagebox(master=self,title='Error occured',message='Please check ur mail configuration',icon='cancel',width=200,height=100,icon_size=15)
            print(e)


    def login(self):
        user_otp=self.user_pass.get()
        try:
            if user_otp:
                if user_otp==self.system_otp:
                    self.frame2_widget()
                    self.current_step = 'start'
                else:
                    CTkMessagebox(master=self,title='Info',message="Invalid OTP",icon='warning',width=200,height=100)
            else:
                CTkMessagebox(master=self,title='Info',message='Please Enter OTP',icon='info',width=200,height=100)
        except Exception as e:
            CTkMessagebox(master=self,title='error',message='Something went wrong',width=200,height=100)
            print(e)

    def frame2_widget(self):

        self.frame.pack_forget()
        self.time = datetime.now().strftime("%I:%M %p")

        # Create the reset button with green text color
        self.reset_button = ctk.CTkButton(master=self, text='Reset Citrix Password',command=self.reset_password ,width=150) 
        self.reset_button.pack(side='top', padx=5, pady=3, anchor='nw')

        self.chat_frame = ctk.CTkFrame(master=self, corner_radius=10)
        self.chat_frame.pack(side='top', fill='both', expand=True, padx=5, pady=3)

        self.Text_box = ctk.CTkTextbox(master=self.chat_frame,text_color='black', fg_color='#f2f2f2',font=("",13))
        self.Text_box.pack(fill='both', expand=True)

        self.add_message(f' Hi ! {self.user_dn_name} ,Please click appropriate button for action',sender='Bot') 

        self.text_input = ctk.CTkEntry(master=self.chat_frame,placeholder_text='Enter a message',corner_radius=5,width=270,height=35,font=("",14))
        self.text_input.pack(side='left')
        self.text_input.bind("<Return>", self.on_enter_press)

        self.send_button = ctk.CTkButton(master=self.chat_frame, text='Send',fg_color='green', width=40,height=35,command=self.send_message,font=("",13))
        self.send_button.pack(side='left', padx=5, pady=5,fill='x',expand=True)

    def add_message(self, message, sender):
       
        if self.current_step in('otp','new_password','confirm_passwod'):
        # Check if the sender is the user
            if sender == 'user':
                
                message = f"{self.time}: {self.Emp_id} : {self.hide_sensitive_info(message)}"
                self.Text_box.configure(state="normal")     
                
            else:
                
                message = f"{self.time}: {sender}: {message}"
                self.Text_box.configure(state="normal")
        else:
            message = f"{self.time}: {sender}: {message}"
            self.Text_box.configure(state="normal") 

        
       
        self.Text_box.insert(ctk.END, message + '\n')
        self.Text_box.yview(ctk.END)
        self.Text_box.configure(state="disabled")


    def hide_sensitive_info(self, message):

        return '*' * len(message)
      

    # def on_send_click(self,msg):
     
    #     if msg:
    #         self.add_message(msg,sender='user')
    #         self.text_input.delete(0,ctk.END)

    def on_send_click(self, msg):
        if msg:
            self.add_message(msg, sender='user')
            if self.current_step == "start":
                if msg== 'Reset my citrix password':
                    self.add_message(f"OTP has been sent to '{self.Emp_mail}'. \n Please Enter it", sender="Bot") 
                    self.system_otp = generate_otp(self.Emp_mail)
                    self.current_step = "otp"
                    self.sessions['system_otp']=self.system_otp
                    
                    
                    print(self.system_otp)

                else:
                #   self.add_message("Invalid request.click appropriate button for action from the top menu", sender="Bot")
                    CTkMessagebox(master=self,title='instruction',message='Invalid request, Please click appropriate button for action from the top menu',icon='info',width=200,height=100)

                self.update_input_field_show()

  

            elif self.current_step == 'otp':
                self.system_otp=self.sessions['system_otp']
                user_otp = msg.strip()

                if user_otp:        

                    if user_otp == self.system_otp:
                        self.add_message("Valid OTP...Please type your new password", sender='Bot')
                        self.open_password_window()


                    elif user_otp=='Reset my citrix password':

                        result=CTkMessagebox(master=self,title='Confirm',message='Do u want to restart \n the session?',icon='warning',option_1='no',option_2='yes')
                        print(result)


                        if result.get()=='no':
                            self.add_message('Enter valid otp',sender='Bot')
                            self.current_step='otp'

                        elif result.get()=='yes':
                            self.add_message('process stopped and restarted',sender='Bot')
                            self.current_step='start'

                    else:
                        self.add_message('Enter valid otp',sender='Bot')
                        CTkMessagebox(master=self,title='error',message='Incorrect OTP.Please Enter OTP again',width=200,height=100)
                        # self.add_message("Incorrect OTP. Please enter the OTP again.", sender='Bot')
                        self.current_step=='otp'
                    
                else:
                    CTkMessagebox(master=self,title='wrong input',message='Please Enter OTP',icon='warning',width=200,height=100)
                    # self.add_message("Please enter your OTP.", sender='Bot'
        elif not msg and self.current_step in('otp','new_password','confirm_password'):
            CTkMessagebox(master=self,title='warning',message='Please Enter OTP',icon='warning',width=200,height=100)
     
        else:
            CTkMessagebox(master=self,title='instruction',message='Invalid request, Please click appropriate button for action from the top menu',icon='info',width=200,height=100)

    def open_password_window(self):
        self.password_window = ctk.CTkToplevel(master=self)
        self.password_window._set_appearance_mode("dark-blue")
        self.password_window.geometry('250x250+830+630')
        self.password_window.protocol("WM_DELETE_WINDOW", self.confirm_cancel)

        self.Login_Label = ctk.CTkLabel(master=self.password_window, text='Password should contain \n atleast 8 characters. \n one minumimum capital letter \n and special character (@,$,&,!,#) \n for strong password', font=("", 10), corner_radius=10)
        self.Login_Label.pack(pady=10, padx=10)

        self.new_password_entry = ctk.CTkEntry(master=self.password_window, placeholder_text="Enter new password", width=200, height=35, font=("", 13),show='*')
        self.new_password_entry.pack(pady=12, padx=5)

        self.confirm_password_entry = ctk.CTkEntry(master=self.password_window, placeholder_text="Confirm new password", width=200, height=35, font=("", 13),show='*')
        self.confirm_password_entry.pack(pady=12, padx=5)

        self.submit_button = ctk.CTkButton(master=self.password_window, text='Submit',fg_color='green' ,height=35, command=self.password_reset, font=("", 13))
        self.submit_button.pack(side='left', padx=5, fill='x', expand=True)

        self.cancel_button = ctk.CTkButton(master=self.password_window, text='Cancel',fg_color='red3', width=50, height=35, command=self.confirm_cancel, font=("", 13))
        self.cancel_button.pack(side='left', padx=5, pady=5, fill='x', expand=True)

        self.current_step = 'new_password'

    def password_reset(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password and confirm_password:
            if new_password == confirm_password:
                try:
                    x = reset_password(self.user_dn_name, new_password)
                    self.add_message(x, sender="Bot")
                    CTkMessagebox(master=self.password_window, title='success', message=x, icon='check', width=40, height=40)
                    self.current_step = 'start'
                    self.password_window.withdraw()
                except Exception as e:
                    CTkMessagebox(master=self.password_window, title='warning', message='something went wrong', icon='warning', width=40, height=40)
            else:
                CTkMessagebox(master=self.password_window, title='Error', message='password not matched..please check', icon='cancel', width=40, height=40)
        else:
            CTkMessagebox(master=self.password_window, title='Warning', message='Please fill both fields', icon='warning', width=40, height=40)

    def confirm_cancel(self):
        result= CTkMessagebox(master=self.password_window, title='Confirm Cancel', message='Are you sure you want to cancel password reset?', icon='warning', width=40, height=40, option_1='no',option_2='yes')
        
        if result.get().lower() == 'yes':
            self.password_window.withdraw()
            self.add_message('Enter OTP again.If u want to restart the process click appropriate button from the top menu',sender='Bot')
            self.current_step = 'start'
        elif result.get().lower()=='no':
            self.current_step='otp'
            result.destroy()

    def on_enter_press(self, event):
        msg = self.text_input.get()
        self.on_send_click(msg)
        self.text_input.delete(0, ctk.END)

    def send_message(self):
        msg = self.text_input.get()
        self.on_send_click(msg)
        self.text_input.delete(0,ctk.END)
    

    def reset_password(self):
        self.on_send_click("Reset my citrix password")


    def update_input_field_show(self):

        if self.current_step in ('otp', 'new_password', 'confirm_password'):
            self.text_input.configure(show="*",font=("",14))
        else:
            self.text_input.configure(show="")  # Show raw characters


    def set_theme_dark(self):
        ctk.set_appearance_mode("dark")

    def set_theme_light(self):
        ctk.set_appearance_mode("light")

    def set_theme_system(self):
        ctk.set_appearance_mode("system")

    def set_color_theme_blue(self):
        ctk.set_default_color_theme("blue")

    def set_color_theme_green(self):
        ctk.set_default_color_theme("green")

    def set_color_theme_dark_blue(self):
        ctk.set_default_color_theme("dark-blue")

if __name__ == "__main__":
    app = LoginPage()
    app.set_theme_dark()
    app.mainloop()
