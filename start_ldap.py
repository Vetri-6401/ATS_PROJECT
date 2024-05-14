from ldap3 import Server, Connection, ALL, NTLM,SUBTREE


def start_server():

    try:
    # Define the AD server
        server = Server("ldaps://10.4.10.10", get_info=ALL)

    # Establish connection with NTLM authentication and password as bytes
        conn = Connection(server, user="newgenkw.local\\botadmin", password="Welcome@123", authentication=NTLM)

        # Bind and print the result
        if conn.bind():
            print("connection sucessful")

            
            conn.search(search_base='ou=BOT-TEST,dc=newgenkw,dc=local',
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