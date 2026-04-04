import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options - This is the critical part for Cloud/CLI environments
chrome_options = Options()
chrome_options.add_argument("--headless=new") # Runs browser in the background
chrome_options.add_argument("--no-sandbox")     # Required for many Linux environments
chrome_options.add_argument("--disable-dev-shm-usage") # Overcomes limited resource issues

# 2. Get the correct path for your local HTML file
# This assumes test_page.html is in the SAME folder as this script
file_path = os.path.abspath("test_page.html")
local_url = f"file://{file_path}"

# 3. Initialize the Driver using the Chromium packages you installed
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 4. Open the local file
    print(f"Opening: {local_url}")
    driver.get(local_url)

    # 5. Locate element by ID (Selenium 4 syntax)
    username_element = driver.find_element(By.ID, 'username')

    # 6. Print the result to your terminal
    print("\n--- Success! ---")
    print("Element found via ID 'username':")
    print(username_element.get_attribute('outerHTML'))
    print("----------------\n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 7. Always close the driver to save memory
    driver.quit()
