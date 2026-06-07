import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/")
homePage = driver.find_element(By.XPATH, value="//span[text()='Automation']")
if homePage.is_displayed():
    print("Home page is visibled")
else:
    print("Home page is not visible")

driver.find_element(By.XPATH, value="//a[text()=' Signup / Login']").click()


newUser = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))
print("New User Sign-up is visible")

driver.find_element(By.XPATH, value="//input[@name='name']").send_keys("Admin")
driver.find_element(By.XPATH, value="(//input[@name='email'])[2]").send_keys("admin_.123@gmail.com")
driver.find_element(By.XPATH, value="//button[@data-qa='signup-button']").click()

accountInfo = driver.find_element(By.XPATH, value="//b[text()='Enter Account Information']")
if accountInfo.is_displayed():
    print("Enter Account Information is displayed")

driver.find_element(By.XPATH, value="//input[@id='id_gender2']").click()
driver.find_element(By.XPATH, value="//input[@type='password']").send_keys("Admin123")


day = Select(driver.find_element(By.ID, "days"))
day.select_by_visible_text("3")
month = Select(driver.find_element(By.ID, "months"))
month.select_by_visible_text("April")
year = Select(driver.find_element(By.ID, "years"))
year.select_by_visible_text("2015")


driver.find_element(By.XPATH, value="(//input[@type='checkbox'])[1]").click()
driver.find_element(By.XPATH, value="(//input[@type='checkbox'])[2]").click()

driver.find_element(By.XPATH, value="//input[@id='first_name']").send_keys("Admin")
driver.find_element(By.XPATH, value="//input[@id='last_name']").send_keys("123")
driver.find_element(By.XPATH, value="//input[@id='company']").send_keys("SmartCliff")
driver.find_element(By.XPATH, value="//input[@id='address1']").send_keys("Thilagar Street")
driver.find_element(By.XPATH, value="//input[@id='address2']").send_keys("R.S Puram")
driver.find_element(By.XPATH, value="//input[@id='state']").send_keys("Tamil Nadu")
driver.find_element(By.XPATH, value="//input[@id='city']").send_keys("Coimbatore")
driver.find_element(By.XPATH, value="//input[@id='zipcode']").send_keys("689 543")
driver.find_element(By.XPATH, value="//input[@id='mobile_number']").send_keys("9876543210")
driver.find_element(By.XPATH, value="(//button[@type='submit'])[1]").click()


accountCreated = driver.find_element(By.XPATH, value="//b[text()='Account Created!']")
if accountCreated.is_displayed():
    print("Account created")
time.sleep(5)

driver.find_element(By.CLASS_NAME, "btn-primary").click()

User = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "fa-user")))
welcomeUser = driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").text
assert "Admin" in welcomeUser, "Incorrect user logged in"
print("User verified successfully")

driver.find_element(By.XPATH, "//a[text()=' Delete Account']").click()
accountDeleted = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
assert accountDeleted.is_displayed(), "Error in deleting the account"
print("User account deleted successfully")

driver.find_element(By.XPATH, "//a[text()='Continue']").click()