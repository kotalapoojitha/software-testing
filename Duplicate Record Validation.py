from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    # Open Student Management System
    driver.get("YOUR_URL_HERE")

    # Add first student
    wait.until(EC.visibility_of_element_located((By.ID, "studentName"))).send_keys("Rahul")
    driver.find_element(By.ID, "studentUSN").send_keys("1BM22CS101")
    driver.find_element(By.ID, "department").send_keys("CSE")
    driver.find_element(By.ID, "addStudent").click()

    print("First student added successfully.")

    time.sleep(2)

    # Try adding duplicate student
    driver.find_element(By.ID, "studentName").clear()
    driver.find_element(By.ID, "studentUSN").clear()
    driver.find_element(By.ID, "department").clear()

    driver.find_element(By.ID, "studentName").send_keys("Rahul")
    driver.find_element(By.ID, "studentUSN").send_keys("1BM22CS101")
    driver.find_element(By.ID, "department").send_keys("CSE")
    driver.find_element(By.ID, "addStudent").click()

    # Validate duplicate error message
    error = wait.until(
        EC.visibility_of_element_located((By.ID, "errorMessage"))
    ).text

    assert "already exists" in error.lower()

    print("PASS: Duplicate student ID rejected.")
    print("Error Message:", error)

except Exception as e:
    print("Test Failed")
    print(e)

finally:
    time.sleep(5)
    driver.quit()