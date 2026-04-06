import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

def run_headless_test(target_url):
    # Task 1: Setting Up Selenium for Headless Mode
    chrome_options = Options()
    
    # Task 1.3: Configure ChromeOptions
    chrome_options.add_argument('--headless=new')  # The modern headless flag
    chrome_options.add_argument('--no-sandbox')    # Required for Linux/Root environments
    chrome_options.add_argument('--disable-dev-shm-usage') # Prevents memory crashes in containers
    chrome_options.add_argument('--window-size=1920,1080') # Standardizes the "virtual" screen size

    # 2. Initialize the Driver
    service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Task 4.1: Measuring Time for Page Load
        print(f"Starting Headless Test on: {target_url}")
        start_time = time.time()
        
        # Task 2: Navigating to a Website
        driver.get(target_url)
        
        end_time = time.time()
        load_time = end_time - start_time
        
        print(f"Task 2 Success: Page Title is '{driver.title}'")
        print(f"Task 4.1: Headless Mode Load Time: {load_time:.2f} seconds")

        # Task 3: Capturing a Screenshot in Headless Mode
        screenshot_name = "headless_verification.png"
        driver.save_screenshot(screenshot_name)
        print(f"Task 3 Success: Screenshot saved as {os.path.abspath(screenshot_name)}")

        return load_time

    except Exception as e:
        print(f"\n[!] Error during headless execution: {e}")
        return None

    finally:
        # Task 4.2 & Conclusion: Clean up
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    test_url = 'https://alnafi.com/'
    h_time = run_headless_test(test_url)
    
    if h_time:
        print("\n--- Lab 19 Comparison Analysis ---")
        print(f"Actual Headless Time: {h_time:.2f}s")
        print("Estimated Normal Mode Time: ~1.5x to 2x slower (due to GPU/UI rendering)")
        print("Resource Note: Headless mode uses significantly less RAM and CPU as it skips")
        print("rendering pixels to a physical monitor.")
        print("----------------------------------\n")
