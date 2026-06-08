import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("input_browser", ['chrome', 'firefox'])
@pytest.mark.parametrize("input_url", ['https://www.flipkart.com/', 'https://www.amazon.com/'])

def test_url(input_browser, input_url):
    if input_browser == 'chrome':
        Chrome_options = webdriver.ChromeOptions()
        Chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=Chrome_options)
        driver = webdriver.Chrome()
    if input_browser == 'firefox':
        Chrome_options = webdriver.ChromeOptions()
        Chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=Chrome_options)
        driver = webdriver.Firefox()

    driver.get(input_url)
    print(driver.title)
    time.sleep(5)