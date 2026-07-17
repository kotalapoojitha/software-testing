from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    # Open Login Page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    # Verify Login Successful
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    print("Login Successful")

    # Simulate inactivity
    print("Waiting for 15 seconds...")
    time.sleep(15)

    # Perform an action
    driver.refresh()

    # Check whether user is still logged in
    current_url = driver.current_url

    if "logged-in-successfully" in current_url:
        print("Session is still active.")
    else:
        print("Session expired. Redirected to Login Page.")

    time.sleep(5)

finally:
    driver.quit()