import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. Open the target website
    target_url = "https://alnafi.cloud/auth/signin"
    print(f"Navigating to: {target_url}")
    driver.get(target_url)
    
    # Wait for the page to load
    time.sleep(5)

    # 4. FIND THE ELEMENT (This was the missing line!)
    # We use the exact ID from your inspect tool: "Username/ Email"
    username_field = driver.find_element(By.ID, "Username/ Email")

    # 5. Send keys to the field
    username_field.send_keys("testuser@example.com")
    print("Step 1: Successfully typed into the Username/Email field.")

    # 6. Locate and Populate the Password field
    # Assuming the ID for password follows a similar pattern
    password_field = driver.find_element(By.ID, "Password")
    password_field.send_keys("securepassword123")
    print("Step 2: Successfully typed into the Password field.")

    # 7. Final Confirmation
    print("\n--- Success! ---")
    print("Form fields populated successfully.")
    print("----------------\n")

except Exception as e:
    print(f"\n[!] Error during execution: {e}")

finally:
    # 8. Close the browser
    time.sleep(2)
    driver.quit()
    print("Browser closed.")
