import paramiko

hostname = '172.16.100.26'
username = 'Fnet'
pwd = 'Welcome@123'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect with a timeout of 30 seconds
    ssh_client.connect(hostname=hostname,username=username, password=pwd, timeout=30)
    print('Connection successful')

    # Do something with the connection


except paramiko.ssh_exception.AuthenticationException:
    print("Authentication failed, please check your credentials.")
except paramiko.ssh_exception.SSHException as e:
    print(f"SSH connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the connection, whether successful or not
    ssh_client.close()

