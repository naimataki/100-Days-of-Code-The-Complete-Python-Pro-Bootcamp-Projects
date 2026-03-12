from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
#driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get("https://www.python.org/")

#price_dolloar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#print(f"The price is {price_dolloar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="q")
#print(search_bar.tag_name)
#print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
#print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

#driver.find_elements(By.CSS_SELECTOR)

#driver.close()
driver.quit()
