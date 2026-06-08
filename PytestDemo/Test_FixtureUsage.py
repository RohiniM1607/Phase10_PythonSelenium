import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_validproduct(self):
        self.driver.find_element(By.NAME, value="search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_invalidproduct(self):
        self.driver.find_element(By.NAME, value="search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        excepted_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(excepted_text)