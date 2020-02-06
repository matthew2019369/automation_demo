from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Selenium:
    __instance = None

    def __init__(self):
        if Selenium.__instance is None:

            print('__init__ method called')
        else:
            raise ValueError("An instantiation already exists!", self.get_instance())

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DriverAndWait()
        return cls.__instance

    @classmethod
    def remove_instance(cls):
        cls.__instance = None

class DriverAndWait:
    def __init__(self):
        self._driver = webdriver.Chrome()
        print("Webdriver is initiated")
        self._global_wait = WebDriverWait(self._driver, 10)
        print("Global wait is initiated")

    def get_driver(self):
        return self._driver

    def get_wait(self):
        return self._global_wait

    def close(self):
        self._driver.close()
        print("Browser is closed")

    def exit(self):
        self._driver.quit()
        print("Quited the browser")






