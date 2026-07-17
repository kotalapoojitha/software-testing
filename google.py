import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(30)   # Keeps the browser open for 30 seconds

driver.quit()