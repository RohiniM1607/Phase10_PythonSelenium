import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.google.com"
driver.get(url)
print("Page Title: ", driver.title)
searchBox = driver.find_element(By.ID, value="APjFqb")
#print(searchBox)
if searchBox.is_enabled:
    print("Search Box Enabled")
else:
    print("Search box Not Enabled")
driver.find_element(By.ID, value="APjFqb").send_keys("Selenium")
searchBtn = driver.find_element(By.NAME, value="btnK")
if searchBtn.is_enabled():
    print("Search Button Enabled")
else:
    print("Search Button Not Enabled")
driver.find_element(By.NAME, value="btnK").click()
time.sleep(5)
print("Completed")