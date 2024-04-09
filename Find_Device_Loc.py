from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import requests
import socket
import getpass
import paramiko
import platform

def get_node_hostnames(grid_url):
    try:
        response = requests.get(f'{grid_url}/status')
        if response.status_code == 200:  # Response code 200 means TRUE
            node_details = response.json()  #containg node deatsil in json format
            for node in node_details.get('value', {}).get('nodes', []):
                uri = node.get('uri', '')
                hostname = uri.split('//')[1].split(':')[0] if uri else ''
                if hostname:
                    print("Node URI:", uri)
                    print("Node Hostname:", hostname)
                    host_ip= hostname
                    username = 'Fnet'
                    pwd = 'Welcome@123'

                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                    try:
                        # Connect with a timeout of 30 seconds
                        ssh_client.connect(hostname=host_ip,username=username, password=pwd, timeout=30)
                        print('Connection successful')

                        stdin, stdout, stderr = ssh_client.exec_command('hostname')
                        output = stdout.read().decode('utf-8').strip()

                        # Print the output
                        print(f"Device Name : {output}")



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
        else:
            print("Failed to fetch node details")
    except requests.exceptions.RequestException as e:
        print("Error fetching node details:", e)

def Device_Location():

    grid_url = 'http://172.16.100.20:4444'  #change as per the hub 

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--headless=New")
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--window-size=1920,1080")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["platformName"] = "windows"
    # capabilities['node_ip']="172.16.100.26"
    
    driver = webdriver.Remote(
        command_executor=f'{grid_url}/wd/hub',
        options=chrome_options,

    )

    wait = WebDriverWait(driver, timeout=5)

    get_node_hostnames(grid_url)

    time.sleep(5)

    #web address we want to navigate into 
    driver.get("https://gps-coordinates.org/")

    time.sleep(5) #wait to till loading page


    try:

        latitude=wait.until(EC.visibility_of_element_located(("id","latitude"))).get_attribute("value")
        print("Current latitude : ",latitude)
        
        longitude=wait.until(EC.visibility_of_element_located(("id","longitude"))).get_attribute("value")
        print("Current longitude : ",longitude)

        print("Located address :")

        Address=wait.until(EC.visibility_of_element_located(("id","address"))).get_attribute("value")

        return Address

    except Exception as e:

        print(e)

    finally:

        # command="hostname"

        # output=subprocess.check_output(command,shell=True)

        # device_name=output.decode("utf-8").strip()
        
        # print(device_name)

        time.sleep(5)

        driver.quit()




# Call the function to get the current location details
print(Device_Location())
