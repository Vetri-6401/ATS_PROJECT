import mysql.connector
from mysql.connector import Error

def ldap_reset_details(emp_id,email_id,status):
    # Establish the connection
    try:
        connection = mysql.connector.connect(
            user='chat',
            password='chatindia',
            host='',
            port='3306',
            database='chatbot'  # Specify your database name here
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Insert data into the table
            insert_query = f"INSERT INTO ldap_pwd_reset_logs (emp_id, emp_mail, status) VALUES (%s, %s, %s)"
            record_to_insert = (emp_id, email_id, status)
            cursor.execute(insert_query, record_to_insert)

            # Commit changes
            connection.commit()
            print("Record inserted successfully")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
