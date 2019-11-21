from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page_Login():
    def __init__(self, driver):
        self.driver = driver
        self.cpf_input = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "cadastroCpfTextInput")))
        self.avancarBtn = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "avancarBtn")))

    def inserir_cpf(self, cpf):
        self.cpf_input.send_keys(cpf)
        self.avancarBtn.click()

    def inserir_senha(self, senha):
        self.senha_input = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "senhaTextInput")))
        self.senha_input.send_keys(senha)
        self.avancarBtn.click()


