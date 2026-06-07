from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/")
homePage = driver.find_element(By.XPATH, value="//span[text()='Automation']")
if homePage.is_displayed():
    print("Home page is visibled")
else:
    print("Home page is not visible")

driver.find_element(By.XPATH, value="//a[text()=' Signup / Login']").click()


newUser = driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
if newUser.is_displayed():
    print("Login to your account is visible")

driver.find_element(By.XPATH, value="(//input[@name='email'])[1]").send_keys("admin_.123@gmail.com")
driver.find_element(By.XPATH, value="//input[@name='password']").send_keys("Admin123")
driver.find_element(By.XPATH, value="//button[@data-qa='login-button']").click()

User = driver.find_element(By.CLASS_NAME, "fa-user")
welcomeUser = driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").text
assert "Admin" in welcomeUser, "Incorrect user logged in"
print("User verified successfully")

driver.find_element(By.XPATH, "//a[text()=' Delete Account']").click()
accountDeleted = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
assert accountDeleted.is_displayed(), "Error in deleting the account"
print("User account deleted successfully")