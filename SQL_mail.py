import pyodbc
import smtplib
from email.mime.text import MIMEText

# Database connection settings
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# Query to check for failed jobs
query = "SELECT name FROM msdb.dbo.sysjobs INNER JOIN msdb.dbo.sysjobhistory ON msdb.dbo.sysjobs.job_id = msdb.dbo.sysjobhistory.job_id WHERE run_status = 0"

# Execute the query
cursor = conn.cursor()
cursor.execute(query)
failed_jobs = cursor.fetchall()

if failed_jobs:
    # Prepare email content
    email_content = "The following SQL Server jobs have failed:\n"
    for job in failed_jobs:
        email_content += job[0] + "\n"

    # Email settings
    sender = 'your_email@example.com'
    recipients = ['recipient1@example.com', 'recipient2@example.com']
    subject = 'SQL Server Job Failure Alert'

    # Create the email message
    msg = MIMEText(email_content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Connect to SMTP server and send the email
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'smtp_username'
    smtp_password = 'smtp_password'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()
