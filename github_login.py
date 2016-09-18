from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://github.com/login")
assert "GitHub" in driver.title
elem = driver.find_element_by_name("login")
elem.clear()
elem.send_keys("nikh@gmail.com")
elem.send_keys()
elem1 = driver.find_element_by_name("password")
elem1.clear()
elem1.send_keys(" my password ")
elem1.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
