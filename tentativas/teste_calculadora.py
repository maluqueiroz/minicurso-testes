from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "deviceName": "Sony 8.0",
    "platformName": "Android",
    "version": "8.0",
    "app": "apps/sample.apk",
    "realDevice": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

inputA = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
)
inputA.send_keys("10")

inputB = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
)
inputB.send_keys("5")

sum = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "sum"))
)

if sum!=None and sum.text=="15":
  assert True
else:
  assert False

driver.quit()