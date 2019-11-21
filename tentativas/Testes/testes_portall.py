import unittest
from Driver.driver_local import Driver
from Pages.page_entrar_portall import Page_Login
from Pages.page_login_portall import Page_Inicial

class TestesPortall(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_entrar_portall(self):
        page_inicial = Page_Inicial(self.driver)
        page_inicial.clicar_em_entrar()

        page_login = Page_Login(self.driver)
        page_login.inserir_cpf("11927102405")
        page_login.inserir_senha("Teste123")

    def tearDown(self):
        self.driver.instance.quit()