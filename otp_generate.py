import random
import smtplib
from email.mime.text import MIMEText

def generate_otp(user_mail):
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
        smtp_password = 'Vetri@6401'
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, recipients, msg.as_string())
        print("otp has been sent successfully")
        return otp
    except Exception as e:
        return  e

    