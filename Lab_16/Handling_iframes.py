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
    # Task 1: Identify and Navigate
    url = "https://alnafi.cloud/auth/signin"
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(10)

    # Task 2: Switching Context to iFrames
    # On many modern sites, the login form or a 'Chat with us' widget is in a frame.
    # We will first count how many iframes are on the page.
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Total iFrames found on page: {len(iframes)}")

    if len(iframes) > 0:
        print("Step 2: Switching to the first iFrame (Index 0)...")
        # Switching by Index (Task 2)
        driver.switch_to.frame(0)

        # Task 3: Interacting with Elements Inside an iFrame
        # Note: We try to find any element inside this new context.
        # If there's a button or input inside the frame, we interact here.
        print("Context switched. Now searching for elements inside the frame...")
        
        # Example: if there was a button with id 'submitButton' inside the frame
        # button = driver.find_element(By.ID, "submitButton")
        # button.click()
        
        # Task 4: Returning to Main Page Context
        print("Step 4: Switching back to the main document context.")
        driver.switch_to.default_content()
    else:
        print("No iFrames detected on this specific load. Interacting with main content.")

    # Interaction with main page element (using your identified ID)
    username_field = driver.find_element(By.ID, "Username/ Email")
    username_field.send_keys("testuser@example.com")
    print("Success: Interacted with main page after frame check.")

    print("\n--- Lab 16 Completed Successfully ---")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # Task 5: Clean Up
    driver.quit()
    print("Browser closed.")
