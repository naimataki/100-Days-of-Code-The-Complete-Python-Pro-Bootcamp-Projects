import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import time

load_dotenv()

ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]
GYM_URL = "https://appbrewery.github.io/gym/"

classes_booked = 0
wailists_joined = 0
already_booked = 0

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
password.clear()
password.send_keys(ACCOUNT_PASSWORD)

# Submit the form
submit_button = driver.find_element(By.ID, value="submit-button")
submit_button.click()

# Verify you're logged in by checking for the "Class Schedule" page
wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday or Thursday
    if "Tue" or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text == "Booked":
                print(f"✓ Already booked: {class_name} on {day_title}")
                already_booked += 1
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                already_booked += 1
            elif button.text == "Book Class":
                button.click()
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                classes_booked += 1
                # Wait a bit for the button state to update
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                button.click()
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                wailists_joined += 1
                # Wait a bit for the button state to update
                time.sleep(0.5)

print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {classes_booked}")
print(f"Waitlists joined: {wailists_joined}")
print(f"Already booked/waitlisted: {already_booked}")
print(f"Total Tuesday 6am classes processed: {classes_booked + wailists_joined + already_booked}")



#driver.quit()