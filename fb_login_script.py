from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
#assert "GitHub" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("nikhil@gmail.com")
elem.send_keys()
elem1 = driver.find_element_by_name("pass")
elem1.clear()
elem1.send_keys(" ur password ")
elem1.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
