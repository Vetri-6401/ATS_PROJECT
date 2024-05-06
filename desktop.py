import tkinter as tk
from datetime import datetime
import otp_generate


class DesktopApp():
    def __init__(self, window):
        self.window = window
        window.title("Desktop App")
        window.minsize(300, 300)
        window.maxsize(800, 600)
        self.create_widgets()
        self.sessions = {}
        self.current_step = 'start'

    def create_widgets(self):
        # Welcome Label
        self.welcome_label = tk.Label(self.window, text="Welcome to Fnet Service ! ")
        self.welcome_label.pack(pady=5)

        # Frame for Chat Messages
        self.chat_frame = tk.Frame(self.window)
        self.chat_frame.pack(expand=True, fill="both")

        # Frame to hold button and listbox
        chat_header_frame = tk.Frame(self.chat_frame)
        chat_header_frame.pack(side="top", fill="x")

        # Reset Citrix Password Button
        self.reset_button = tk.Button(chat_header_frame, text="Reset Citrix Password", command=self.reset_password)
        self.reset_button.pack(side='left', pady=5)

        # Scrollbar for the chat frame
        self.scrollbar = tk.Scrollbar(self.chat_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Chat message listbox
        self.message_listbox = tk.Listbox(self.chat_frame, yscrollcommand=self.scrollbar.set)
        self.message_listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.message_listbox.yview)

        # Input Field
        self.input_field = tk.Entry(self.window)
        self.input_field.pack(side="left", fill="x", padx=5, pady=5, expand=True)
        self.input_field.bind("<Return>", self.on_enter_press)

        # Send Button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side="left", padx=5, pady=5)

    def add_message(self, message, sender):
        time = datetime.now().strftime("%H:%M")
        if sender == "user":
            message = f"[{time}] You: {message}"
        else:
            message = f"[{time}] Bot: {message}"
        self.message_listbox.insert(tk.END, message)
        self.message_listbox.yview(tk.END)

    def on_send_click(self, msg):
        if msg:
            self.add_message(msg, sender="user")
            if self.current_step == "start":
                if msg.lower() == 'reset my citrix password':
                    self.add_message("Enter your username", sender="system")
                    self.current_step = "username"
                else:
                    self.add_message("Invalid request. Type 'reset my citrix password' to begin.", sender="system")
            elif self.current_step == "username":
                username_input = msg.strip()  # Remove leading/trailing whitespaces
                if username_input:
                    # Handle the username input, for example, validate it or proceed to the next step
                    self.add_message("Validating username and generating OTP...", sender="system")
                    self.current_step = "otp"
                    system_otp = otp_generate.generate_otp()
                    self.sessions['system_otp']=system_otp
                    print(system_otp)
                else:
                    self.add_message("Please enter your username.", sender="system")
            elif self.current_step == 'otp':
                system_otp=self.sessions['system_otp']
                user_otp = msg.strip()
                if user_otp:
                    if user_otp == system_otp:
                        self.add_message("Valid OTP. Proceed to reset your password.", sender='system')
                        self.current_step = 'new_password'
                    else:
                        self.add_message("Invalid OTP. Please enter the OTP again.", sender='system')
                        self.current_step=='otp'
                else:
                    self.add_message("Please enter your OTP.", sender='system')
            elif self.current_step == 'new_password':
                user_password = msg.strip()
                if user_password:
                        self.add_message("Plesae confirm your password", sender='system')
                        self.current_step = 'confirm_password'
                        self.sessions['new_password']=user_password
                else:
                    self.add_message("Please enter password plaese", sender='system')
            elif self.current_step == 'confirm_password':
                confirm_password = msg.strip()
                new_password=self.sessions['new_password']
                if confirm_password:
                        if confirm_password==new_password:
                            self.add_message('Password Matched..changed sucessfully',sender="system")
                            self.current_step=='start'
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

if __name__ == "__main__":
    app = tk.Tk()
    window = DesktopApp(app)
    app.mainloop()
