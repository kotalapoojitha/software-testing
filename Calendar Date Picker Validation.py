from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open Demo Date Picker
driver.get("https://jqueryui.com/datepicker/")

wait = WebDriverWait(driver, 10)

# Switch to iframe (datepicker is inside an iframe)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))

# Open calendar
driver.find_element(By.ID, "datepicker").click()

# Get today's date
today = datetime.today()

# Tomorrow's date
tomorrow = today + timedelta(days=1)

# Yesterday's date
yesterday = today - timedelta(days=1)

# -----------------------------
# Verify yesterday is disabled
# -----------------------------
try:
    past_date = driver.find_element(
        By.XPATH,
        f"//a[text()='{yesterday.day}']"
    )

    if past_date.is_enabled():
        print("Past date is selectable.")
    else:
        print("Past date is disabled.")

except:
    print("Past date is not available (disabled).")

# -----------------------------
# Select tomorrow's date
# -----------------------------
future_date = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//a[text()='{tomorrow.day}']")
    )
)

future_date.click()

# Verify selected date
selected_date = driver.find_element(By.ID, "datepicker").get_attribute("value")

print("Selected Date:", selected_date)

time.sleep(10)
driver.quit()