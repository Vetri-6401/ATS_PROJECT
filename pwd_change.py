from ldap3 import Server, Connection, ALL, NTLM,SUBTREE,MODIFY_REPLACE



def reset_password(dn,newpassword):

    try:
    # Define the AD server
        user_dn=f'CN={dn},OU=BOT-TEST,DC=newgenkw,DC=local'
        server = Server("ldaps://10.4.10.10", get_info=ALL)

    # Establish connection with NTLM authentication and password as bytes
        conn = Connection(server, user="newgenkw.local\\botadmin", password="Welcome@123", authentication=NTLM)

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