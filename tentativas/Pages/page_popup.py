from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PagePopUp():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver.instance, 10)
        
    def fechar_popUp(self):
        self.btnOK = self.wait.until(EC.element_to_be_clickable((By.ID, "btOK")))
        self.btnOK.click()

