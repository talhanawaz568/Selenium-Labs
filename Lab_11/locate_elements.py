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
    # 3. Navigate to the target website
    url = 'https://alnafi.cloud/auth/signin'
    print(f"Navigating to: {url}")
    driver.get(url)
    
    # 4. Wait for the page to load all elements
    time.sleep(5)

    # 5. Find all links (using updated Selenium 4 syntax)
    # find_elements (plural) returns a list of all <a> tags
    links = driver.find_elements(By.TAG_NAME, "a")

    print("\n--- Links Found ---")
    for link in links:
        text = link.text.strip()
        href = link.get_attribute('href')
        
        # Only print if there is actual text or a link
        if text or href:
            print(f"Text: {text if text else '[No Text]'} | URL: {href}")

    # 6. Print the summary count
    print("-------------------")
    print(f"Total number of links found: {len(links)}")
    print("-------------------\n")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # 7. Close the browser
    driver.quit()
    print("Browser closed.")
