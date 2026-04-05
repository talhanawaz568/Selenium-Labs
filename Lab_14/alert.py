import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options (Required for Ubuntu/Cloud)
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Task 1: Navigate to the Test Web Page
    url = "http://the-internet.herokuapp.com/javascript_alerts"
    print(f"Navigating to: {url}")
    driver.get(url)
    time.sleep(2)

    # Task 2: Triggering and Switching to the Alert
    print("Step 2.1: Clicking the button to trigger JS Alert...")
    # Updated Selenium 4 syntax for XPath
    alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    alert_button.click()

    # Step 2.2: Switch to the Alert
    # Even in headless mode, Selenium "focuses" on the virtual pop-up
    alert = driver.switch_to.alert
    
    # Task 3: Interacting with the Alert
    # Step 3.3: Retrieve Alert Text (Do this before accepting!)
    alert_text = alert.text
    print(f"Task 3.3 Success! Alert text captured: '{alert_text}'")

    # Step 3.1: Accept the Alert
    alert.accept()
    print("Task 3.1 Success: Alert accepted (Clicked OK).")

    # Verification: Check the result message on the page
    result = driver.find_element(By.ID, "result")
    print(f"Page Result: {result.text}")

    print("\n--- Lab 14 Completed Successfully ---")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # Task 4: Close the Browser
    driver.quit()
    print("Browser session closed.")
