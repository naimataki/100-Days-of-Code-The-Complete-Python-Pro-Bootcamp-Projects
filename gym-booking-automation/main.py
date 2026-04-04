import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import requests

load_dotenv()

ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]
GYM_URL = "https://appbrewery.github.io/gym/"

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# a directory in your project folder to store your Chrome Profile information with
user_data_dir = os.path.join(os.getcwd(), "gym-booking-automation/chrome_profile")
# Tell your Chrome Driver to use the directory you specified to store a "profile". 
# That way every time you quit Chrome and re-run your Selenium script, 
# it keeps all the preferences and settings from your profile.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, timeout=2)
# Click the login button
login_button = driver.find_element(By.ID, value="login-button")
login_button.click()

# Fill in your email and password
email = driver.find_element(By.ID, value="email-input")
email.clear()
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, value="password-input")
email.clear()
password.send_keys(ACCOUNT_PASSWORD)

# Submit the form
submit_button = driver.find_element(By.ID, value="submit-button")
submit_button.click()

# Verify you're logged in by checking for the "Class Schedule" page
wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-']")

for card in class_cards:
    #Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if it's a Tuesday:
    if "Tue" in day_title:
        #Check if it's a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-time-']").text



#driver.quit()