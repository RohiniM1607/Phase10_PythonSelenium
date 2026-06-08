from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--password-store=basic")
options.add_argument("--disable-save-password-bubble")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)

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

driver.find_element(By.XPATH, value="(//input[@name='email'])[1]").send_keys("demo.1@gmail.com")
driver.find_element(By.XPATH, value="//input[@name='password']").send_keys("Demo123")
driver.find_element(By.XPATH, value="//button[@data-qa='login-button']").click()

User = driver.find_element(By.CLASS_NAME, "fa-user")
welcomeUser = driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").text
assert "Demo" in welcomeUser, "Incorrect user logged in"
print("User verified successfully")

# driver.find_element(By.XPATH, "//a[text()=' Delete Account']").click()
# accountDeleted = driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
# assert accountDeleted.is_displayed(), "Error in deleting the account"
# print("User account deleted successfully")