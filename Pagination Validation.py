from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_open_google():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.google.com")

    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    assert "Google" in driver.title

    search_box.send_keys("Pagination Testing with Selenium")

    assert search_box.get_attribute("value") == "Pagination Testing with Selenium"

    print("Test Passed!")

    time.sleep(5)

    driver.quit()