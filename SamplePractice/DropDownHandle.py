from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.leafground.com/")
driver.find_element(By.XPATH, "//span[text()='Element']/preceding-sibling::i").click()
driver.find_element(By.XPATH, "//span[text()= 'Dropdown']").click()

#Select by visible test
dropdown1 = Select(driver.find_element(By.XPATH, "//select[@class='ui-selectonemenu']"))
for option in dropdown1.options:
    print(option.text)
dropdown1.select_by_visible_text("Selenium")

#First selected option
selected_option = dropdown1.first_selected_option
print("Selected Option is:", selected_option.text)


#Select by index
dropdown1.select_by_index(2)
selected_option = dropdown1.first_selected_option
print("Selected Option is:", selected_option.text)

#Select by sent keys
dropdown2 = driver.find_element(By.XPATH,"//div[contains(@class,'ui-autocomplete-multiple')]//input")
dropdown2.send_keys("JMeter")
dropdown2.send_keys(Keys.ENTER)

dropdown2.send_keys("ReactJS")
dropdown2.send_keys(Keys.ENTER)

dropdown2.send_keys("Appium")
dropdown2.send_keys(Keys.ENTER)

selected_options = driver.find_elements(By.XPATH,"//ul[contains(@class,'ui-autocomplete-multiple-container')]//li[contains(@class,'ui-autocomplete-token')]")
for option in selected_options:
    print("Selected Option:", option.text)


actions = ActionChains(driver)
dropdown3 = driver.find_element(By.XPATH, "(//span[@class='ui-icon ui-icon-triangle-1-s ui-c'])[1]")
actions.click(dropdown3).perform()
option = driver.find_element(By.XPATH, "//li[text()='Brazil']")
actions.click(option).perform()
selected_country = driver.find_element(
    By.XPATH,
    "(//label[contains(@class,'ui-dropdown-label')])[1]"
)
print("Selected Country:", selected_country.text)

actions.click(dropdown3).perform()
option = driver.find_element(By.XPATH, "//li[text()='Germany']")
actions.move_to_element(option).click().perform()
print("Selected Country:", selected_country.text)
actions.click(dropdown3)\
       .send_keys(Keys.ARROW_DOWN)\
       .send_keys(Keys.ARROW_DOWN)\
       .send_keys(Keys.ENTER)\
       .perform()
print("Selected Country:", selected_country.text)