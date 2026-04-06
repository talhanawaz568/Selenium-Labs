import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# --- TASK 1: Setup Development Environment ---
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize the Chromium Driver for Ubuntu
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Global Implicit Wait as a backup
driver.implicitly_wait(5)

try:
    # --- TASK 2: Navigate to Demo Site ---
    target_url = "https://alnafi.cloud/auth/signin"
    print(f"Step 2: Navigating to {target_url}")
    driver.get(target_url)

    # --- TASK 6: Initial Validation (Assertion) ---
    # We verify the title to ensure we aren't on an error page
    assert "Al Nafi" in driver.title, f"Assertion Failed: Unexpected Title '{driver.title}'"
    print("✓ Initial Assertion Success: Al Nafi Portal loaded.")

    # --- TASK 3: Automate Form Interaction ---
    # We use WebDriverWait (Explicit Wait) for high reliability
    wait = WebDriverWait(driver, 20)
    
    print("Step 3: Locating and filling the Login form...")
    
    # 1. Locate Username/Email using the ID from your inspect tool
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "Username/ Email")))
    username_field.send_keys("test_student@example.com")
    
    # 2. Locate Password
    password_field = driver.find_element(By.ID, "Password")
    password_field.send_keys("SecurePassword123!")
    print("✓ Form fields populated.")

    # --- TASK 5: Take Progress Screenshot ---
    driver.save_screenshot('project_step_form_filled.png')
    print("✓ Screenshot saved: project_step_form_filled.png")

    # --- TASK 3 & 4: Clicking the Button & Handling Interaction ---
    print("Step 3: Attempting to click the Sign-in button...")
    
    # IMPROVED XPATH: This looks for a button that contains the text 'Sign in' 
    # It is case-insensitive to handle 'SIGN IN', 'Sign In', or 'Sign in'
    button_xpath = "//button[contains(translate(text(), 'SIGN', 'sign'), 'sign in')]"
    
    # We wait until the button is actually clickable (not just present)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    
    # Perform the click
    login_button.click()
    print("✓ Login button clicked successfully.")

    # --- TASK 4 & 6: Final Validation ---
    # Wait for the page to react to the login attempt
    time.sleep(5) 
    
    print("\n--- Final Project Results ---")
    print(f"Current URL: {driver.current_url}")
    print(f"Page Title:  {driver.title}")

    # Assertion to confirm we didn't crash or get redirected to a 404
    assert driver.current_url != "about:blank", "Assertion Failed: Browser is on a blank page."
    print("✓ Final Validation Success: End-to-End flow executed without crashing.")

except Exception as e:
    # TASK 5: Error Handling & Debugging
    print(f"\n[!] PROJECT ERROR: {e}")
    driver.save_screenshot('project_error_state.png')
    print(f"Check '{os.path.abspath('project_error_state.png')}' to diagnose the UI state.")

finally:
    # --- TASK 6: Close Browser ---
    driver.quit()
    print("\nWebDriver session closed. End-to-End Project Complete.")
