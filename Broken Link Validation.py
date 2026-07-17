import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.google.com")

time.sleep(3)

# Find all links
elements = driver.find_elements(By.TAG_NAME, "a")

# Store URLs only
urls = []

for element in elements:
    href = element.get_attribute("href")
    if href:
        urls.append(href)

print("Total Links Found:", len(urls))
print("-" * 50)

broken_links = []

# Check each URL
for url in urls:
    try:
        response = requests.get(url, timeout=10)
        print(url, "--->", response.status_code)

        if response.status_code >= 400:
            broken_links.append(url)

    except Exception as e:
        print(url, "---> ERROR:", e)

driver.quit()

print("\n========== RESULT ==========")

if broken_links:
    print("Broken Links Found:")
    for link in broken_links:
        print(link)
else:
    print("PASS: No Broken Links Found.")