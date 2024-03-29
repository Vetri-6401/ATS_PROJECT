from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import requests
import reversegeo as loc
import socket

def get_node_hostnames(grid_url):
    try:
        response = requests.get(f'{grid_url}/status')
        if response.status_code == 200:
            node_details = response.json()
            for node in node_details.get('value', {}).get('nodes', []):
                uri = node.get('uri', '')
                hostname = uri.split('//')[1].split(':')[0] if uri else ''
                if hostname:
                    print("Node URI:", uri)
                    print("Node Hostname:", hostname)
                    try:
                        host_info = socket.gethostbyaddr(hostname)
                        print("Hostname Info:", host_info)
                    except socket.herror as e:
                        print("Error resolving hostname:", e)
        else:
            print("Failed to fetch node details")
    except requests.exceptions.RequestException as e:
        print("Error fetching node details:", e)

def get_current_location():

    grid_url = 'http://172.16.100.18:4444'
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    # options.add_argument("--headless") 
    # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["platformName"] = "windows"
    
    driver = webdriver.Remote(
        command_executor=f'{grid_url}/wd/hub',
        options=options,
    )

    wait = WebDriverWait(driver, timeout=5)

    driver.get("https://www.maps.ie/coordinates.html")
    driver.maximize_window()

    element = wait.until(EC.element_to_be_clickable(("id","find-loc")))
    element.click()

    time.sleep(3)

    try:

        latitude = wait.until(EC.visibility_of_element_located(("id","marker-lat"))).get_attribute("value")
        print("Current latitude : ", latitude)
        
        longitude = wait.until(EC.visibility_of_element_located(("id","marker-lng"))).get_attribute("value")
        print("Current longitude : ", longitude)

        print("located address :")

        Address=loc.address_details(latitude,longitude)

        return Address

    except Exception as e:
        print("Error:", e)
    finally:
        get_node_hostnames(grid_url)
        time.sleep(2)
        driver.close()

# Call the function to get the current location details
print(get_current_location())
