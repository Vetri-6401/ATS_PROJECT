from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import socket
from pyvirtualdisplay import Display
import time  

def My_Location():

    #Enabling cababilities of a chrome

    display = Display(visible=0,size=(800,600))
    display.start()
    options=webdriver.ChromeOptions()

    #Grant permission automatically by usng this commet use--fake-ui-for-media-stream byDefault
    options.add_argument("--use--fake-ui-for-media-stream")
    
    #select a webdriver chrome,firebox,etc...
    driver=webdriver.Chrome() 
    wait=WebDriverWait(driver,timeout=10)

    #web address we want to navigate into 
    driver.get("https://gps-coordinates.org/")

    time.sleep(5) #wait to till loading page


    try:
        device_name=socket.gethostname()
        print("Device name :",device_name)
        
        latitude=wait.until(EC.visibility_of_element_located(("id","latitude"))).get_attribute("value")
        print("Current latitude : ",latitude)
        
        longitude=wait.until(EC.visibility_of_element_located(("id","longitude"))).get_attribute("value")
        print("Current longitude : ",longitude)

        print("Located address :")

        Address=wait.until(EC.visibility_of_element_located(("id","address"))).get_attribute("value")
        return Address

    except Exception as e:

        print(e)

    driver.close()
    display.stop()

print(My_Location())
    
