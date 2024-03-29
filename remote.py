from selenium import webdriver
import socket
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
import time
import json
from json.decoder import JSONDecoder
import requests
import reversegeo as loc
import os
from bs4 import BeautifulSoup



def get_current_location():

    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    # options.add_argument("--headless") 
    # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["platformName"] = "windows"
    # display = Display(visible=0, size=(800, 600))
    # display.start()

    driver = webdriver.Remote(
        command_executor='http://172.16.100.18:4444/wd/hub',
        options=options,
        
    )

    
    wait = WebDriverWait(driver, timeout=5)

    driver.get("https://www.maps.ie/coordinates.html")
    driver.maximize_window()

    time.sleep(5) #wait to till loading page

    element=wait.until(EC.element_to_be_clickable(("id","find-loc")))
    element.click()

    time.sleep(5)

    try:

        
        latitude=wait.until(EC.visibility_of_element_located(("id","marker-lat"))).get_attribute("value")
        print("Current latitude : ",latitude)
        
        longitude=wait.until(EC.visibility_of_element_located(("id","marker-lng"))).get_attribute("value")
        print("Current longitude : ",longitude)

        print("Located address :")

        Address=loc.address_details(latitude,longitude)

        return Address

    except Exception as e:

        print(e)
    finally:
        driver.quit()
        # display.stop()
    

print(get_current_location())