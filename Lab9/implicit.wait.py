import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options (Crucial for Ubuntu/Cloud)
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

    # 4. Set Implicit Wait (The browser will wait up to 10 seconds for elements to appear)
    driver.implicitly_wait(10)

    # 5. Locate the element using the ID you found
    # Using the modern Selenium 4 syntax
    print("Waiting for 'Username/ Email' field to appear...")
    username_field = driver.find_element(By.ID, "Username/ Email")

    # 6. Interact with the element
    username_field.send_keys("testuser@example.com")
    print("Step 1: Successfully located element and entered text.")

    # 7. Final Confirmation
    print("\n--- Success! ---")
    print(f"Verified element present on: {driver.current_url}")
    print("----------------\n")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # 8. Close the browser
    driver.quit()
    print("Browser closed.")

