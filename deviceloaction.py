from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

try:
    options = Options()
    options.add_argument('--headless')  # Uncomment to run Chrome in headless mode
    options.add_argument("--use--fake-ui-for-media-stream")

    driver = webdriver.Chrome(options=options)
    driver.get("https://maps.google.com")
    
    # Wait for the page to load
    time.sleep(2)
    
    # Find the search input element and enter coordinates
    search_box = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    coordinates = "12.979408,80.265216"  # Example coordinates for Chennai, India
    search_box.send_keys(coordinates)
    time.sleep(2)
    
    # Find and click the search button
    search_button = driver.find_element(By.ID, "searchbox-searchbutton")
    search_button.click()

    time.sleep(2)
    
    # Wait for the search results to load
    
    
    # Find the address element in the search results
    address_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[10]/div[2]/div[2]/span[2]/span')
    
    # Get the text of the address
    address = address_element.text
    
    # Print or use the retrieved address
    print("Address found:", address)
    
finally:
    # Close the browser
    driver.quit()
