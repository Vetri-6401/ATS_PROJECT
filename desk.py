import tkinter as tk
import tkinter.ttk as ttk
import random
import smtplib
from email.mime.text import MIMEText
from tkinter import Tcl
from datetime import datetime
from ldap3 import Server, Connection, ALL, NTLM,SUBTREE,MODIFY_REPLACE
from tkinter import messagebox
import time


class DesktopApp():
    def __init__(self, window):
        self.window = window
        window.title("Fnet Service",)
        window.configure(background='turquoise2')
        window.geometry("300x400")
        window.maxsize(800, 600)
        self.create_widgets()
        self.sessions = {}
        self.current_step = 'start'

    def create_widgets(self):
        # Welcome Label
        # self.welcome_label = tk.Label(self.window, text="Welcome to Fnet Service ! ",activebackground='red',activeforeground='white',background='green')
        # self.welcome_label.pack(pady=5)

        # Frame for Chat Messages
        self.chat_frame = tk.Frame(self.window)
        self.chat_frame.pack(expand=True, fill="both")

        # Frame to hold button and listbox
        chat_header_frame = tk.Frame(self.chat_frame,background='white')
        chat_header_frame.pack(side="top", fill="x")

        # Reset Citrix Password Button
        self.reset_button = tk.Button(chat_header_frame, text="Reset Citrix Password", command=self.reset_password,background='SpringGreen3')
        self.reset_button.pack(side='left', padx=5,pady=2)

        # Scrollbar for the chat frame
        self.scrollbar = tk.Scrollbar(self.chat_frame)
        self.scrollbar.pack(side="right", fill="y",padx=2)

        # Chat message listbox
        self.message_listbox = tk.Listbox(self.chat_frame,bd=2, relief=tk.FLAT, font=("Helvetica", 10), bg="white", yscrollcommand=self.scrollbar.set,background='black',foreground='white')
        self.message_listbox.pack(side="left", fill="both", expand=True,padx=5,pady=5)
        self.scrollbar.config(command=self.message_listbox.yview)

        # Input Field
        self.input_field = tk.Entry(self.window, bd=2, relief=tk.SUNKEN, font=("Helvetica", 14))
        self.input_field.pack(side="left", fill="x", padx=5, pady=5, expand=True)
        self.input_field.bind("<Return>", self.on_enter_press)

        # Send Button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side="left", padx=5, pady=5)

    def add_message(self, message, sender):
        time = datetime.now().strftime("%H:%M")
        if sender == "user":
            message = f"{time}: You: {message}"
           
        else:
            message = f"{time}: Bot: {message}"

        self.message_listbox.insert(tk.END, message)
        self.message_listbox.yview(tk.END)

    def on_send_click(self, msg):
        if msg:
            self.add_message(msg, sender="user")
            if self.current_step == "start":

                if msg.lower() == 'reset my citrix password':
                    self.add_message("Enter your username", sender="system")
                    self.current_step = "username"
                    self.ldap_user,self.ldap_mail=self.start_server()

                else:
                    self.add_message("Invalid request. Type 'reset my citrix password' to begin.", sender="system")


            elif self.current_step == "username":
                
                username_input = msg.strip()  # Remove leading/trailing whitespaces
                
                if username_input:

                    if username_input in self.ldap_user:
                        self.sessions['emp_id']=username_input

                        # Handle the username input, for example, validate it or proceed to the next step
                        self.add_message("user found...otp generated", sender="system")
                        self.current_step = "otp"
                        user_dn=self.ldap_user[username_input]
                        self.sessions['user_dn']=user_dn
                        
                        system_otp = self.generate_otp(self.ldap_mail[username_input])
                        self.sessions['emp_mail']=self.ldap_mail[username_input]
                        self.sessions['system_otp']=system_otp
                        print(system_otp)

                    elif username_input=='reset my citrix password':
                        result=messagebox.askyesno(title='confirm',message='Do u want to restart the session ?')

                        if not result:
                            self.add_message('Enter valid user name',sender='system')

                            self.current_step='username'
                        else:
                            self.add_message('process stopped...proceed to begin again')
                            self.current_step='start'    

                    else:
                        self.add_message('user not found...Enter valid user',sender="system")
                        self.current_step='username'

                else:
                    self.add_message("Please enter your username.", sender="system")

            elif self.current_step == 'otp':
                system_otp=self.sessions['system_otp']
                user_otp = msg.strip()

                if user_otp:

                    if user_otp == system_otp:
                        self.add_message("Valid OTP...Proceed to reset", sender='system')
                        self.current_step = 'new_password'

                    elif user_otp=='reset my citrix password':
                        result=messagebox.askyesno(title='confirm',message='Do u want to restart the session ?')

                        if not result:
                            self.add_message('Enter valid otp',sender='system')
                            self.current_step='otp'

                        else:
                            self.add_message('process stopped...proceed to begin again',sender='system')
                            self.current_step='start'

                    else:
                        self.add_message("Invalid OTP. Please enter the OTP again.", sender='system')
                        self.current_step=='otp'

                else:
                    self.add_message("Please enter your OTP.", sender='system')


            elif self.current_step == 'new_password':
                user_password = msg.strip()

                if user_password:

                    if user_password=='reset my citrix password':
                        result=messagebox.askyesno(title='confirm',message='Do u want to restart the session ?')

                        if not result:
                            self.add_message('Enter valid password',sender='system')
                            self.current_step='new_password'
                        else:
                            self.add_message('process stopped...proceed to begin again')
                            self.current_step='start'

                    else:
                       
                        self.add_message("Plesae confirm your password", sender='system')
                        self.current_step = 'confirm_password'
                        self.sessions['new_password']=user_password
                    
                else:
                    self.add_message("Please enter password plaese", sender='system')

            elif self.current_step == 'confirm_password':
                confirm_password = msg.strip()
                new_password=self.sessions['new_password']
                user_dn=self.sessions['user_dn']

                if confirm_password:
                        
                        if confirm_password==new_password:
                            result=messagebox.askyesno(title='confirm',message='Do u want to reset you password?')

                            if result:
                                x=self.reset_new_password(user_dn,new_password)
                                self.add_message(x,sender="system")
                                emp_id=self.sessions['emp_id']
                                emp_mail=self.sessions['emp_mail']
                                self.current_step ='start'

                            else:
                                self.add_message('password reset cancelled',sender='system')
                                self.current_step='start'

                        else:
                            self.add_message("password not matched..please reenter password and confirm",sender='system')
                            self.current_step='new_password'

                else:
                    self.add_message("Please enter your OTP.", sender='system')

        else:
            self.add_message("Please enter a message.", sender="system")



    def reset_password(self):
        self.on_send_click("reset my citrix password")

    def send_message(self):
        msg = self.input_field.get()
        self.on_send_click(msg)
        self.input_field.delete(0, tk.END)

    def on_enter_press(self, event):
        msg = self.input_field.get()
        self.on_send_click(msg)
        self.input_field.delete(0, tk.END)

    def start_server(self):

        try:
        # Define the AD server
            server = Server("", get_info=ALL)

        # Establish connection with NTLM authentication and password as bytes
            conn = Connection(server, user="", password="Welcome@123", authentication=NTLM)

            # Bind and print the result
            if conn.bind():
                print("connection sucessful")

                
                conn.search(search_base='ou=,dc=,dc=',
                        search_filter='(objectClass=user)',
                        search_scope=SUBTREE, 
                        attributes=['cn','sAMAccountName','mail'])
            
                response=conn.response

                ldap_users={}
                ldap_user_mail={}

                for i in response:
                    ldap_users[i['attributes']['sAMAccountName']]=i['attributes']['cn']
                    ldap_user_mail[i['attributes']['sAMAccountName']]=i['attributes']['mail']

            
                return ldap_users,ldap_user_mail
            
        except Exception as e:
            
            return e
        
        finally:
            conn.unbind()

    
    def reset_new_password(self,dn,newpassword):

        try:
        # Define the AD server
            user_dn=f'CN={dn},OU=BOT-TEST,DC=newgenkw,DC=local'
            server = Server("", get_info=ALL)

        # Establish connection with NTLM authentication and password as bytes
            conn = Connection(server, user="", password="", authentication=NTLM)

        # Bind and print the result
            if conn.bind():
                print("connection sucessful")

                conn.modify(user_dn,{'unicodePwd':[(MODIFY_REPLACE,[f'"{newpassword}"'.encode('utf-16-le')])]})

                if conn.result['result'] == 0:
                    return f"Password for {dn} changed successfully."
                                    
                else:
                    return f"Failed to change password for {dn}: {conn.result}"
                
        except Exception as error:
            return error
        
        finally:
            conn.unbind()

    def generate_otp(self,user_mail):
        """Generate a random OTP of the specified length using only numeric digits."""
        # Define the characters to use for OTP generation (only numeric digits)
        try:
            characters = "0123456789"
            # Generate OTP using random.choices
            otp = ''.join(random.choices(characters, k=4))
            print(user_mail)

            email_content=f'OTP for reset your citrix password : {otp} '
            sender = 'vetrivel.c@futurenet.in'
            recipients = user_mail
            subject = 'OTP for reset your citrix password'

            # Create the email message
            msg = MIMEText(email_content,'plain')
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipients

            # Connect to SMTP server and send the email
            smtp_server = 'webmail.futurenet.in'
            smtp_port = 587
            smtp_username = sender
            smtp_password = 'Welcome@123'
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipients, msg.as_string())
            print("otp has been sent successfully")
            server.quit()
        except Exception as e:
            print(e)

        return otp

if __name__ == "__main__":
    app = tk.Tk()
    window = DesktopApp(app)
    app.geometry("+750+550")
    app.mainloop()
   
