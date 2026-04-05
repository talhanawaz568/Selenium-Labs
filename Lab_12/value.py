import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Essential for dropdowns
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1. Setup Chrome Options for Ubuntu/Cloud
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. Open the local HTML page
    # os.path.abspath ensures we find 'dropdown.html' in your current folder
    file_path = os.path.abspath("dropdown.html")
    driver.get(f"file://{file_path}")
    print(f"Opened: {file_path}")

    # 4. Locate the Dropdown element (Task 2)
    # find_element_by_id is updated to find_element(By.ID, ...)
    dropdown_element = driver.find_element(By.ID, "dropdown-example")

    # 5. Use the Select class to manipulate the dropdown (Task 3)
    select_object = Select(dropdown_element)

    # Step: Select by visible text
    print("Selecting 'Option 2' by text...")
    select_object.select_by_visible_text("Option 2")
    time.sleep(1) # Small pause to simulate interaction

    # Step: Select by value attribute (e.g., <option value="3">)
    print("Selecting 'Option 3' by value '3'...")
    select_object.select_by_value("3")

    # 6. Retrieve and Print the Selected Option (Task 4)
    # .first_selected_option returns the currently active choice
    current_selection = select_object.first_selected_option
    print("\n--- Lab Result ---")
    print(f"Final Selected Option Text: {current_selection.text}")
    print(f"Final Selected Option Value: {current_selection.get_attribute('value')}")
    print("------------------\n")

except Exception as e:
    print(f"\n[!] Error: {e}")

finally:
    # 7. Clean Up (Task 5)
    driver.quit()
    print("Browser session closed.")
