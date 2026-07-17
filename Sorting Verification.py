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

# Open Demo Table
driver.get("https://the-internet.herokuapp.com/tables")

wait = WebDriverWait(driver, 10)

# Click the "Last Name" column (replace with Name column on your website)
name_column = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Last Name']"))
)
name_column.click()

# Read names after ascending sort
rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td[1]")

ascending_names = []
for row in rows:
    ascending_names.append(row.text)

print("Ascending Order:", ascending_names)

# Verify ascending order
expected_ascending = sorted(ascending_names)

assert ascending_names == expected_ascending, "Ascending sort failed!"

print("Ascending sort verified successfully.")

# Click again for descending order
name_column.click()
time.sleep(2)

rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td[1]")

descending_names = []
for row in rows:
    descending_names.append(row.text)

print("Descending Order:", descending_names)

# Verify descending order
expected_descending = sorted(descending_names, reverse=True)

assert descending_names == expected_descending, "Descending sort failed!"

print("Descending sort verified successfully.")

time.sleep(5)
driver.quit()