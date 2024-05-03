from ldap3 import Server, Connection, ALL, NTLM,SUBTREE, MODIFY_REPLACE
from ldap3 import *
from otpgenerate import *

# Define the AD server
server = Server("server_IP", get_info=ALL)

# Define the connection
conn = Connection(server, user='domainname\\username', password='',authentication=NTLM )

# Perform the connection
conn.bind()

# Check if the connection is successful
if conn.bind():
    print("Successfully connected to AD")

    # user_to_change=input('Enter user for password change: ')
    conn.search(search_base='ou=,dc='',dc='',
                search_filter = '(objectClass=user)',
                search_scope=SUBTREE,
                attributes=['cn','sAMAccountName','mail'])
    # Retrieve the response
    response = conn.response
    # print(response)

    ldap_users={}
    ldap_user_mail={}
    

    for i in response:
        ldap_users[i['attributes']['sAMAccountName']]=i['attributes']['cn']
        ldap_user_mail[i['attributes']['sAMAccountName']]=i['attributes']['mail']

    print(ldap_users)
    print(ldap_user_mail)
    

    user_to_change=input('Enter user for password change: ')
   
    
    if user_to_change in ldap_users:
        

        print('user Found..proceed with password change: \n')

        generated_otp=generate_otp(ldap_user_mail[user_to_change])
        print(generated_otp)
        
        while True:
            Enter_OTP=input('Enter OTP: ')
            if Enter_OTP==generated_otp:
                print("OTP validated....proceed to create a new password...")
                user_dn_name=ldap_users[user_to_change]

                user_dn = f'CN={user_dn_name},OU=,DC=,DC='

                
                while True:
                    new_password=input('Enter new password : ')
                    confirm_password=input('Confirm new password : ')
                    if new_password==confirm_password:
                        print("Password Matched")
                        conn.modify(user_dn,
                                {'unicodePwd': [(MODIFY_REPLACE, [f'"{new_password}"'.encode('utf-16-le')])]})

                        if conn.result['result'] == 0:
                            print(f"Password for {user_to_change} changed successfully.")
                            
                        else:
                            print(f"Failed to change password for {user_to_change}: {conn.result}")
                        break
                    else:
                        print("password Not Matched, please Enter again")
                break
            else:
                print("OTP is incorrect...please enter valid otp: ")
    else:
        print('user not found , please enter valid user')


else:
    print("Failed to connect to AD:", conn.result)

conn.unbind()
