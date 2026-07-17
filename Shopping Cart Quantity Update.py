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
    # Open Shopping Website
    driver.get("https://example.com/shop")

    # Click Add to Cart
    wait.until(
        EC.element_to_be_clickable((By.ID, "addToCart"))
    ).click()

    print("Product Added to Cart")

    # Open Cart
    driver.find_element(By.ID, "cart").click()

    # Change Quantity from 1 to 4
    qty = wait.until(
        EC.presence_of_element_located((By.ID, "quantity"))
    )

    qty.clear()
    qty.send_keys("4")

    # Click Update Cart
    driver.find_element(By.ID, "updateCart").click()

    # Wait for total to update
    time.sleep(3)

    # Read values from UI
    subtotal = driver.find_element(By.ID, "subtotal").text
    tax = driver.find_element(By.ID, "tax").text
    grand_total = driver.find_element(By.ID, "grandTotal").text

    print("Subtotal :", subtotal)
    print("Tax :", tax)
    print("Grand Total :", grand_total)

    # Remove ₹ symbol and commas
    subtotal_value = float(subtotal.replace("₹", "").replace(",", ""))

    # Verify subtotal
    expected_subtotal = 500 * 4

    assert subtotal_value == expected_subtotal

    print("PASS : Subtotal updated correctly.")

    # Verify tax exists
    assert tax != ""

    print("PASS : Tax updated.")

    # Verify grand total exists
    assert grand_total != ""

    print("PASS : Grand Total updated.")

except Exception as e:
    print("Test Failed")
    print(e)

finally:
    time.sleep(5)
    driver.quit()