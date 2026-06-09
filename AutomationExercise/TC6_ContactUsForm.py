from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//li/child::a[@href='/contact_us']"))).click()
wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("Demo")
driver.find_element(By.XPATH, "//div[@class='form-group col-md-6']/child::input[@type='email']").send_keys("demo.1@gmail.com")
driver.find_element(By.NAME, "subject").send_keys("Testing")
driver.find_element(By.ID, "message").send_keys("This is a test message")
submit=driver.find_element(By.XPATH, "//input[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.accept()
print("Alert is handled")
driver.quit()