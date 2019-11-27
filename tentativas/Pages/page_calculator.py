from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Calculator():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver.instance, 10)
    


    def click_btn_one(self):
        self.btn_one = self.wait.until(EC.element_to_be_clickable((By.ID, "one")))
        self.btn_one.click()
        return self


    def click_btn_two(self):
        self.btn_two = self.wait.until(EC.element_to_be_clickable((By.ID, "two")))
        self.btn_two.click()
        return self

    def click_btn_plus(self):
        self.btn_plus = self.wait.until(EC.element_to_be_clickable((By.ID, "plus")))
        self.btn_plus.click()
        return self

    def click_btn_equal(self):
        self.btn_equal = self.wait.until(EC.element_to_be_clickable((By.ID, "equal")))
        self.btn_equal.click()
        return self

    def get_value_display(self):
        self.display = self.wait.until(EC.visibility_of_element_located((By.ID, "display")))
        self.display.get_value_display
        return self
