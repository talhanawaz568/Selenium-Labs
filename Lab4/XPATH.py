from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options for your Cloud/Ubuntu environment
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Driver using webdriver-manager
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. Open the target website
    driver.get('https://practicetestautomation.com/')

    # 4. Locate element by XPATH (Updated for your specific path)
    # Replaced CSS_SELECTOR with XPATH
    element = driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a')

    # 5. Retrieve and print details
    print("\n--- Success! ---")
    print(f"XPath Location: //*[@id='menu-item-20']/a")
    print(f"Tag Name: {element.tag_name}")
    print(f"Link Text: {element.text}")
    print(f"Href Attribute: {element.get_attribute('href')}")
    print("----------------\n")

except Exception as e:
    print(f"Error: Could not locate the XPath. {e}")

finally:
    # 6. Close the browser
    driver.quit()
