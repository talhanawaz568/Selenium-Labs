import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options (Required for Ubuntu/Cloud)
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Optional: Set window size to ensure the screenshot captures the full desktop view
chrome_options.add_argument("--window-size=1920,1080")

# 2. Initialize the Driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. Navigate to the website
    url = 'https://alnafi.cloud/auth/signin'
    print(f"Navigating to: {url}")
    driver.get(url)
    
    # 4. Wait for the page to render completely
    print("Waiting for page to load...")
    time.sleep(5)

    # 5. Capture the basic screenshot
    screenshot_file = "screenshot.png"
    driver.save_screenshot(screenshot_file)
    print(f"Basic screenshot saved as: {screenshot_file}")

    # 6. Capture a timestamped screenshot
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    timestamped_file = f"screenshot_{timestamp}.png"
    driver.save_screenshot(timestamped_file)
    print(f"Timestamped screenshot saved as: {timestamped_file}")

    print("\n--- Success! ---")
    print("Screenshots captured and saved in the current directory.")
    print("----------------\n")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # 7. Close the browser
    driver.quit()
    print("Browser closed.")
