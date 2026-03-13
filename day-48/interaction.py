from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(articles_number.text)

driver.quit()

