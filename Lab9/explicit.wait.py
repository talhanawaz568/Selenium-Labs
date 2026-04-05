import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    # 3. Navigate to the Al Nafi sign-in page
    url = "https://alnafi.cloud/auth/signin"
    print(f"Navigating to: {url}")
    driver.get(url)

    # 4. Initialize WebDriverWait (Wait up to 10 seconds)
    wait = WebDriverWait(driver, 10)

    # 5. Wait for the specific Username/Email field to be CLICKABLE
    # We use the exact ID string: "Username/ Email"
    print("Waiting for 'Username/ Email' to be clickable...")
    username_field = wait.until(
        EC.element_to_be_clickable((By.ID, "Username/ Email"))
    )

    # 6. Perform the click and type action
    username_field.click()
    username_field.send_keys("testuser@example.com")
    print("Step 1: Successfully clicked and typed into the Username/Email field.")

    # 7. Final Confirmation
    print("\n--- Success! ---")
    print(f"Verified element was clickable on: {driver.current_url}")
    print("----------------\n")

except Exception as e:
    print(f"\n[!] Error during execution: {e}")

finally:
    # 8. Close the browser
    time.sleep(2)
    driver.quit()
    print("Browser closed.")
