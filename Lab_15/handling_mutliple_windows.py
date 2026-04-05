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
    # Task 1: Open a New Tab or Window
    print("Step 1.1: Launching the main page...")
    driver.get("http://the-internet.herokuapp.com/windows")
    
    # Store the ID of the original window
    original_window = driver.current_window_handle
    print(f"Original Window Handle: {original_window}")

    print("Step 1.2: Clicking the link to open a new window...")
    # Updated Selenium 4 syntax
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    
    # Wait briefly for the new window to be registered by the browser
    time.sleep(2)

    # Task 2: List All Open Window Handles
    all_handles = driver.window_handles
    print(f"Total open windows/tabs: {len(all_handles)}")

    # Task 3 & 4: Switch Between Windows and Extract Information
    print("\n--- Iterating Through Windows ---")
    for handle in all_handles:
        # Switch focus to the specific handle
        driver.switch_to.window(handle)
        
        # Identify if it's the new or original window
        window_type = "Main" if handle == original_window else "New Tab/Window"
        
        print(f"[{window_type}]")
        print(f"  ID: {handle}")
        print(f"  Title: {driver.title}")
        print(f"  URL: {driver.current_url}")
        print("-" * 30)

    # Task 5: Switch back to the original window specifically
    driver.switch_to.window(original_window)
    print(f"\nFinal Focus: Switched back to Main Window. Current Title: {driver.title}")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # Terminate the WebDriver
    driver.quit()
    print("\nBrowser session closed.")
