import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options (Crucial for Cloud/Ubuntu instances)
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Dynamic File Path
# This assumes 'test_page.html' is in the same folder as this .py script
file_path = os.path.abspath("test_page.html")
local_url = f"file://{file_path}"

# 3. Initialize the Driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 4. Open the local file
    driver.get(local_url)

    # 5. Locate element by NAME (Updated Selenium 4 syntax)
    # find_element_by_name is now find_element(By.NAME, "...")
    password_element = driver.find_element(By.NAME, 'user_password')

    # 6. Retrieve and print result
    print("\n--- Success! ---")
    print("Element found via Name 'user_password':")
    print(password_element.get_attribute('outerHTML'))
    print("----------------\n")

except Exception as e:
    print(f"Error: Could not find element. {e}")

finally:
    # 7. Close the browser session
    driver.quit()

