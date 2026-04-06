import os
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
    # --- PRE-TASK: Create a dummy file to upload ---
    dummy_file_path = os.path.abspath("lab_test_file.txt")
    with open(dummy_file_path, "w") as f:
        f.write("This is a test file for Lab 18.")
    print(f"Created dummy file at: {dummy_file_path}")

    # Task 2: Navigate to the HTML Page
    html_file_path = os.path.abspath("upload_test.html")
    driver.get(f"file://{html_file_path}")
    print(f"Navigating to: {html_file_path}")
    driver.implicitly_wait(5)

    # Task 3: Automate File Upload
    # Step 1: Locate the File Input Element
    print("Locating the file input field (ID: fileInput)...")
    file_input = driver.find_element(By.ID, "fileInput")

    # Step 2: Automate File Selection
    # CRITICAL: We do NOT click the button. We send the PATH to the input.
    file_input.send_keys(dummy_file_path)
    print("Step 2 Success: File path sent to the input element.")

    # Step 3: Submit the Form
    upload_button = driver.find_element(By.ID, "uploadBtn")
    upload_button.click()
    print("Step 3 Success: Upload button clicked.")

    # Task 4: Validation (Handling the Alert from our HTML)
    time.sleep(2)
    alert = driver.switch_to.alert
    print(f"Browser Alert Confirmation: {alert.text}")
    alert.accept()

    print("\n--- Lab 18 Completed Successfully ---")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # Task 5: Clean Up
    driver.quit()
    # Optional: Delete the dummy file after the test
    if os.path.exists(dummy_file_path):
        os.remove(dummy_file_path)
    print("Browser closed and temporary file removed.")
