from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time  
from selenium.webdriver.support import expected_conditions as EC
import reversegeo as loc


def get_current_location():

    #Enabling cababilities of a chrome

    options=Options()

    #Grant permission automatically by usng this commet use--fake-ui-for-media-stream byDefault
    options.add_argument("--use--fake-ui-for-media-stream")

    #select a webdriver chrome,firebox,etc...

    driver=webdriver.Chrome()
    wait=WebDriverWait(driver,timeout=20)

    #web address we want to navigate into 
    driver.get("https://www.maps.ie/coordinates.html")

    time.sleep(5) #wait to till loading page

    driver.find_element("id","find-loc").click()

    time.sleep(5)

    lat=driver.find_element("id","marker-lat")
    lat=driver.find_element("id","marker-lat")

    
    try:
        
        latitude=wait.until(EC.visibility_of_element_located(("id","marker-lat"))).get_attribute("value")
        print("Current latitude : ",latitude)
        

        longitude=wait.until(EC.visibility_of_element_located(("id","marker-lng"))).get_attribute("value")
        print("Current latitude : ",longitude)

        print("Located address :")

        Address=loc.address_details(latitude,longitude)
        return Address


    except Exception as e:
        
        print(e)

    driver.close()

print(get_current_location())
    




