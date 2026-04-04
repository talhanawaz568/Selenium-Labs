from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without a GUI window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Driver 
# Using webdriver-manager ensures the driver matches your Chromium version
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. Execute the request
    driver.get("https://www.google.com")
    
    # 4. Print results
    print(f"Current URL: {driver.current_url}")
    print(f"Page Title: {driver.title}")

finally:
    # 5. Always close the driver
    driver.quit()
