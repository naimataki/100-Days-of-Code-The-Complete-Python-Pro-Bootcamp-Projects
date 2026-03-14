from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

sleep(3)

print("looking for language selection...")
try:
    language = driver.find_element(By.ID, value="langSelect-EN")
    language.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

sleep(2)

cookie = driver.find_element(By.ID, value="bigCookie")
#cookie.click()

#get all store items (products 0-17)
item_ids = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60*5

while True:
    cookie.click()

    if time() > timeout:
        pass