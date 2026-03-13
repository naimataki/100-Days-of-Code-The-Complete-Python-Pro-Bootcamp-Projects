from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep edge browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

search_bar = driver.find_element(By.NAME, value="fName")
search_bar.send_keys("Naima")
search_bar = driver.find_element(By.NAME, value="lName")
search_bar.send_keys("Takiouti")
search_bar = driver.find_element(By.NAME, value="email")
search_bar.send_keys("naima101@gmail.com", Keys.ENTER)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")

#articles_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
#print(articles_number.text)
#articles_number.click()

#find element by Link Text
#all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

#search_bar = driver.find_element(By.NAME, value="search")
#search_bar.send_keys("Python", Keys.ENTER)
#driver.quit()

