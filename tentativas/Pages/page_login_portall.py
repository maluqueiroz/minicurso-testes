from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

class Page_Inicial():
    def __init__(self, driver):
        self.driver = driver
        self.entrar_btn = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "entrarBtn")))
        self.gerar_boleto = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "gerarBoletoBtn")))

    def clicar_em_entrar(self):
        self.entrar_btn.click()

    def clicar_em_gerar_boleto(self):
        self.gerar_boleto.click()
