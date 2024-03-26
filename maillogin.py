from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
import time

driver=webdriver.Chrome()

driver.get("https://accounts.google.com/")
wait=WebDriverWait(driver,timeout=10)

time.sleep(4)
driver.find_element(by="id",value="identifierId").send_keys("vetri.c641@gmail.com")
time.sleep(5)
driver.find_element(by="id",value="identifierNext").click()
time.sleep(5)
driver.find_element(by="name",value="password").send_keys("Vetri@01")
time.sleep(5)
driver.find_element(by="id",value="passwordNext").click()
time.sleep(3)