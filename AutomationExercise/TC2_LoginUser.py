from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com/")

homePage = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Automation']")
    )
)

if homePage.is_displayed():
    print("Home page is visibled")
else:
    print("Home page is not visible")

driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").click()

loginText = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Login to your account']")
    )
)

if loginText.is_displayed():
    print("Login to your account is visible")

driver.find_element(
    By.XPATH,
    "(//input[@name='email'])[1]"
).send_keys("admin_.123@gmail.com")

driver.find_element(
    By.XPATH,
    "//input[@name='password']"
).send_keys("Admin123")

driver.find_element(
    By.XPATH,
    "//button[@data-qa='login-button']"
).click()

try:
    welcomeUser = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Logged in as')]")
        )
    )

    assert "Admin" in welcomeUser.text
    print("User verified successfully")

except:
    try:
        error = driver.find_element(
            By.XPATH,
            "//p[contains(text(),'Your email or password is incorrect')]"
        )
        print("LOGIN FAILED:", error.text)
    except:
        print("Login failed - account may not exist")

    driver.quit()
    raise

driver.find_element(
    By.XPATH,
    "//a[text()=' Delete Account']"
).click()

print("Account deleted!")

accountDeleted = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[text()='Account Deleted!']")
    )
)

assert accountDeleted.is_displayed()
print("User account deleted successfully")

driver.quit()