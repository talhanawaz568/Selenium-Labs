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
chrome_options.add_argument("--window-size=1920,1080")

# 2. Initialize the Driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Task 2: Navigate to alnafi.com
    url = "https://alnafi.com/"
    print(f"Navigating to: {url}")
    driver.get(url)
    time.sleep(5) # Give the main site time to load initial assets

    # Task 2: Scroll to the Bottom of the Page
    print("Scrolling to the bottom of the page...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) # Wait for the footer to render after scrolling

    # Task 3: Scroll Element into View
    # We will use XPath to find the 'Courses' link in the footer
    # Note: 'Courses' text is common, so we look specifically for the link
    print("Locating the 'Courses' link...")
    try:
        # This XPath looks for an <a> tag containing the text 'Courses'
        courses_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Courses')]")
        
        # Scroll specifically to THIS element to be safe
        driver.execute_script("arguments[0].scrollIntoView();", courses_link)
        print("Element scrolled into view.")

        # Task 4: Confirm Element Visibility
        if courses_link.is_displayed():
            print("Success: 'Courses' link is visible on the page.")
            
            # Action: Click it as per your lab goal
            # Sometimes footer links need a JavaScript click if they are overlapped
            driver.execute_script("arguments[0].click();", courses_link)
            print("Clicked the Courses link.")
            time.sleep(3)
            print(f"New URL: {driver.current_url}")
        else:
            print("Element found in code but is not displayed on screen.")

    except Exception as e:
        print(f"Could not find the 'Courses' link. Error: {e}")

    print("\n--- Lab 17 Completed Successfully ---")

except Exception as e:
    print(f"\n[!] Global Error: {e}")

finally:
    driver.quit()
    print("Browser closed.")
