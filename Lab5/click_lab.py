import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Standard Cloud Setup
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 2. Open your local HTML file
    # Ensure index.html is in the same folder
    file_path = os.path.abspath("index.html")
    driver.get(f"file://{file_path}")

    # 3. Locate the Button
    button = driver.find_element(By.ID, 'sampleButton')
    
    # 4. Perform the Action
    print("Clicking the button...")
    button.click()

    # 5. Validate the Result
    # We check if the page source changed (if your HTML has the script to add text)
    if "Button clicked!" in driver.page_source:
        print("Validation Successful: 'Button clicked!' text found in page source.")
    else:
        print("Action performed, but no text change detected.")

finally:
    driver.quit()
