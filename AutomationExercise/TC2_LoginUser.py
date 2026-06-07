from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://automationexercise.com/")

# Verify Home Page
homePage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Automation']")))

if homePage.is_displayed():
    print("Home page is visible")

# Click Signup/Login
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()=' Signup / Login']"))).click()

# Verify Login Page
loginText = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))

if loginText.is_displayed():
    print("Login to your account is visible")

# Enter Credentials
wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='email'])[1]"))).send_keys("admin_.123@gmail.com")

driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Admin123")

# Click Login
driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()

# Verify Login Success
loggedIn = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))

print(loggedIn.text)

welcomeUser = loggedIn.text
assert "Admin" in welcomeUser, "Incorrect user logged in"

print("User verified successfully")

driver.quit()