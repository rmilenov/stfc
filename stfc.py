from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Konfiguration
EMAIL = "EMAIL"
PW = "PASSWORD"  # Insert Credentials
URL = "https://id.scopely.com/oauth2/default/v1/authorize?response_type=code&response_mode=query&scope=address+openid+email+profile+phone+offline_access&redirect_uri=https://home.startrekfleetcommand.com/&client_id=0oa1496nmx8OcY8eI5d7&prompt=login&state=eyJwbGF5Z2FtaVRyYWNraW5nQmFzZVN0ZXBDb3VudGVyIjowLCJ0cmFja2luZ0lkIjoiODhmMDJlNzItZGE0Mi00NjJiLWJhMDUtMjJiMWE2OGZmMWM4Iiwib3BlcmF0aW9uIjoibG9naW4ifQ==_xlho2x8of0f_eyJjdHgiOnsiaW5zdGFsbCI6IjA3MmI5MDNiLTcyYzAtNGVlNy1iYzNiLTYwNmY4MjA5NmJjYyIsInRlbmFudCI6InIxNGQ2ZjcwNmE1MDQ4ZDg4ODNjNzhkMDhhNzRkNTUyIn0sImNsaWVudElkIjoiOTEzZDYyYzEtNTdiOC00OThlLTliNTYtZjlkNTVlZmE3ZDQyIiwic2V0dGluZ3MiOnsiYXBpS2V5IjoiNGFmN2MyMGItNzY0Ni00ZmI3LWI2NGYtYWUwYThjNTFjMWYxIiwiYnVpbGRUeXBlIjoxLCJkZWJ1ZyI6ZmFsc2UsInByZXZpZXciOmZhbHNlLCJmbHVzaEludGVydmFsTWlsbGlzIjo1MDAwLCJidWlsZFRhcmdldCI6IndlYiIsImRpc3RyaWJ1dGlvbkNoYW5uZWwiOiJ3ZWJwb3J0YWwiLCJzdG9yZSI6IiIsImV2ZW50U291cmNlIjoid2ViX3BvcnRhbCJ9fQ=="

# Webdriver-Setup (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # In order to see the browser comment this line out
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # Maximize browser window
wait = WebDriverWait(driver, 3)

# Öffne die URL
driver.get(URL)


def check_and_decline_cookies():
    """Überprüft und lehnt Cookie-Popup ab, falls vorhanden"""
    try:
        decline_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
        decline_button.click()
        print("Cookies rejected.")
    except Exception:
        pass
# Refuse all cookies


try:
    decline_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    decline_button.click()
    print("Cookies rejected.")
except Exception:
    pass
# Insert e-mail and click continue
try:
    email_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-input")))
    email_field.send_keys(EMAIL)
    print("E-Mail input")
    check_and_decline_cookies()
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submitButtonEnabled ")))
    continue_button.click()
    print("Continue button clicked.")
except Exception as e:
    print(f"Error on e-mail input: {e}")
check_and_decline_cookies()
# Click on password input and insert password
try:
    new_text_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-input.css-1wazalj")))
    new_text_field.click()
    new_text_field.send_keys(PW)
    print("Password input")
except Exception as e:
    print(f"Error on password input: {e}")
check_and_decline_cookies()
# Click login button
try:
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                          "submitButtonEnabled ")))
    login_button.click()
    print("Login button clicked")
except Exception as e:
    print(f"Error on login button click: {e}")
check_and_decline_cookies()
# Navigate to Store
try:
    store_link = wait.until(EC.element_to_be_clickable((By.ID, "navigation-item-to-store")))
    store_link.click()
    print("Navigating to Store")
except Exception as e:
    print(f"Error on navigating to Store: {e}")
check_and_decline_cookies()
# Navigate to Gift section
try:
    gift_tab = wait.until(EC.element_to_be_clickable((By.ID, "store-web-gift-tab-button")))
    gift_tab.click()
    print("Web gift tab clicked")
except Exception as e:
    print(f"Error on click web gift tab: {e}")
check_and_decline_cookies()
# Click on Shop
try:
    shop_element = wait.until(EC.element_to_be_clickable((By.ID, "navigation-item-to-store")))
    shop_element.click()
    print("Shop clicked")
except Exception as e:
    print(f"Error on clicking shop: {e}")
# Click on Web gift
try:
    gift_element = wait.until(EC.element_to_be_clickable((By.ID,"store-web-gift-tab-button")))
    gift_element.click()
    print("Web gift tab clicked.")
except Exception as e:
    print(f"Error on clicking Web gift: {e}")

try:
    counter = 0
    print(driver.find_element(By.CSS_SELECTOR, 'div[name=web-gift-item-div] button:not([disabled])'))
    while driver.find_element(By.CSS_SELECTOR, 'div[name=web-gift-item-div] button:not([disabled])'):
        driver.find_element(By.CSS_SELECTOR, 'div[name=web-gift-item-div] button:not([disabled])').click()
        wait.until(EC.element_to_be_clickable((By.ID, "modal-close-button")))
        driver.find_element(By.ID, "modal-close-button").click()
        counter += 1
        print(str(counter) + " Buttons clicked")
        time.sleep(2)
except Exception as e:
    print(f"Error on clicking gift: {e}")
# Close browser
driver.quit()
