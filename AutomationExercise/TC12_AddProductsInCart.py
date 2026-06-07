import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = selenium.webdriver.Chrome()
driver.get("https://automationexercise.com/")
wait = WebDriverWait(driver,10)

actions = ActionChains(driver)

driver.maximize_window()

assert driver.title == "Automation Exercise"
print("Home page was launched")

product = driver.find_element(By.XPATH,"//a[text()=' Products']")
actions.click(product).perform()
productname=[]

actions.move_to_element(driver.find_element(By.XPATH,"(//div[@class='product-image-wrapper'])[1]")).perform()
productname.append((driver.find_element(By.XPATH,"(//div[@class='productinfo text-center']/child::p)[1]")).text)
actions.click(driver.find_element(By.XPATH,"(//a[@data-product-id='1'])[2]")).perform()

continue_btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='cartModal']//button[contains(text(),'Continue Shopping')]")))
continue_btn.click()
print("Clicked on Continue shopping")
time.sleep(2)

second_product = driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[3]")
actions.move_to_element(second_product).perform()
print("Moved to the second element")
time.sleep(2)
actions.click(driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[3]")).perform()
print("Clicked on add to cart")

time.sleep(2)
actions.click(driver.find_element(By.XPATH, "//u[contains(text(),'View Cart')]")).perform()
print("Clicked on View cart")

product_count = len(productname)
if productname == 2:
    print("True")
else:
    print("False")