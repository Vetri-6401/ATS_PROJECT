from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
import time
import reversegeo as loc

def get_current_location():
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["platformName"] = "windows"
    capabilities["deviceName"] = "guhoij"

    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options,
        desired_capabilities=capabilities
    )
    wait = WebDriverWait(driver, timeout=10)

    driver.get("https://www.maps.ie/coordinates.html")

    latitude = wait.until(EC.visibility_of_element_located(("id", "marker-lat"))).get_attribute("value")
    longitude = wait.until(EC.visibility_of_element_located(("id", "marker-lng"))).get_attribute("value")

    print("Current latitude : ", latitude)
    print("Current longitude : ", longitude)

    print("Located address :")
    address = loc.address_details(latitude, longitude)
    
    driver.quit()
    display.stop()
    
    return address

print(get_current_location())
