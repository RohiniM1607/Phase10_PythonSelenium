import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
driver.implicitly_wait(15)
if driver.title == "Automation Exercise":
    print("Home page was launched")
else:
    print("Home page was not launched")
driver.find_element(By.XPATH,value="//a[text()=' Signup / Login']").click()
login_page = driver.find_element(By.XPATH,value="//div[@class='login-form']/child::h2").text
if login_page.__eq__("Login to your account"):
    print("Login section was displayed")
else:
    print("Login section was not displayed")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[2]").send_keys("admin.1@gmail.com")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[3]").send_keys("Admin123")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::button").click()
try:
    error_msg = driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']" )
    if error_msg.is_displayed():
        print("Login is unsuccessful, Your email or password is incorrect")

except NoSuchElementException:
    print("Login is successful")