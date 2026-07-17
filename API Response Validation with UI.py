import requests
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

try:
    # Open Student List Page
    driver.get("https://YOUR_WEBSITE/students")

    # Wait for table to load
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
    )

    # Read student names from UI
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

    ui_students = []

    for row in rows:
        name = row.find_element(By.XPATH, "./td[2]").text
        ui_students.append(name)

    print("Students from UI:")
    print(ui_students)

    # Call API
    api_url = "https://YOUR_WEBSITE/api/students"

    response = requests.get(api_url)

    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()

    api_students = []

    for student in data:
        api_students.append(student["name"])

    print("\nStudents from API:")
    print(api_students)

    # Compare UI and API
    ui_students.sort()
    api_students.sort()

    assert ui_students == api_students

    print("\nPASS : UI matches API")

except Exception as e:
    print("\nTest Failed")
    print(e)

finally:
    time.sleep(5)
    driver.quit()