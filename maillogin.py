from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/")

# Set up WebDriverWait
wait = WebDriverWait(driver, 10)

# Enter email
email_input = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
email_input.send_keys("vetri.c641@gmail.com")
driver.find_element(By.ID, "identifierNext").click()

# Enter password
password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_input.send_keys("Vetri@01")
driver.find_element(By.ID, "passwordNext").click()

# Wait for login
wait.until(EC.url_contains("myaccount.google.com"))

# Close the browser
driver.quit()
