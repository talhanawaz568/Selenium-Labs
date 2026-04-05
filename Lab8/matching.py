import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options (Required for Ubuntu/Cloud environments)
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Driver using the Chromium setup you installed
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. Task 3: Opening the Web Page
    target_url = "https://www.python.org"
    print(f"Navigating to: {target_url}")
    driver.get(target_url)
    
    # Allow time for the page to load
    time.sleep(3)

    # 4. Task 4: Checking the Page Title
    page_title = driver.title
    expected_title = "Welcome to Python.org"
    
    print(f"Retrieved Page Title: {page_title}")
    
    # Validation using assert
    assert page_title == expected_title, f"Title mismatch! Expected: {expected_title}, but got: {page_title}"
    print("Verification Success: Page title matches.")

    # 5. Task 5: Locating Web Page Elements by Text
    # Updated Selenium 4 syntax for finding elements
    print("Locating 'Downloads' link...")
    element = driver.find_element(By.XPATH, "//a[text()='Downloads']")
    
    actual_text = element.text
    expected_text = "Downloads"
    
    # Validation of the element text
    assert actual_text == expected_text, f"Text mismatch! Expected: {expected_text}, but got: {actual_text}"
    print(f"Verification Success: Found element with text '{actual_text}'.")

    print("\n--- Lab 8 Completed Successfully ---")

except AssertionError as error:
    print(f"\n[!] Validation Failed: {error}")

except Exception as e:
    print(f"\n[!] An unexpected error occurred: {e}")

finally:
    # 6. Task 6: Closing the Web Browser
    driver.quit()
    print("Browser session closed.")
