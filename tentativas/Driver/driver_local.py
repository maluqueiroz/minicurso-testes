from appium import webdriver

class Driver:
    def __init__(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Sony 8.0",
            "udid": "RQ3005LVP5",
            "app": "apps/portall.apk"
        }

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)