from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
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

driver.find_element(By.XPATH, value="(//input[@name='email'])[1]").send_keys("admmin_.123@gmail.com")
driver.find_element(By.XPATH, value="//input[@name='password']").send_keys("Admin123")
driver.find_element(By.XPATH, value="//button[@data-qa='login-button']").click()

wait = WebDriverWait(driver, timeout = 30, poll_frequency = 5, ignored_exceptions=[NoSuchElementException])
invalidText = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']")))
print(invalidText.text)