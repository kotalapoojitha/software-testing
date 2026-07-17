from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Login Function
def login(username, password):
    driver.get("https://example.com/login")

    wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    ).clear()

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "loginButton").click()


try:

    # ---------------------------------
    # Login as Admin
    # ---------------------------------
    login("admin", "admin123")

    # Open User Management Page
    driver.get("https://example.com/user-management")

    # Verify Admin Access
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    print("PASS : Admin can access User Management.")

    # Logout
    driver.find_element(By.ID, "logout").click()

    time.sleep(2)

    # ---------------------------------
    # Login as Student
    # ---------------------------------
    login("student", "student123")

    # Try to access User Management
    driver.get("https://example.com/user-management")

    time.sleep(2)

    current_url = driver.current_url

    # Check if redirected
    if "login" in current_url.lower() or "access-denied" in current_url.lower():
        print("PASS : Student redirected.")

    # Check Access Denied message
    elif "Access Denied" in driver.page_source:
        print("PASS : Access Denied message displayed.")

    else:
        print("FAIL : Student accessed restricted page.")

except Exception as e:
    print("Test Failed")
    print(e)

finally:
    time.sleep(5)
    driver.quit()