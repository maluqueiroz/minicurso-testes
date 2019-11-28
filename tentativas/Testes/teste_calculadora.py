from Pages.page_popup import PagePopUp
from Pages.page_calculator import Calculator
from Driver.driver_local import Driver
import unittest


class Testes(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_fechar_popUp(self):
        popUp = PagePopUp(self.driver)
        popUp.fechar_popUp()

        calculator = Calculator(self.driver)
        calculator.click_btn_two()
        calculator.click_btn_plus()
        calculator.click_btn_two()
        calculator.click_btn_equal()
        value = calculator.get_value_display
        
        assert(4, value)

    def tearDown(self):
        self.driver.instance.quit()	
