
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utilities.Selenium import Selenium
from TestRailIntegration.Integration import Integration
class BasePage():

    def __init__(self):
        tmp = Selenium.get_instance()
        self._driver = tmp.get_driver()
        self._wait = tmp.get_wait()
        self.HEADER_LOGO = (By.CSS_SELECTOR, "img.logo.img-responsive")


    def insert_text(self, element,text):
        ele = self.find_element(element)
        try:
            ele.send_keys(text)
            Integration.append_msg("Keys has been sent to {0}".format(element), True)
        except Exception as ex:
            Integration.append_msg("Keys cannot be sent to {0}".format(element),False)
        return ele

    def find_element(self,e):
        try:
            x =self._wait.until(EC.visibility_of_element_located(e))
            Integration.append_msg("{0} is found".format(e),True)
            return x
        except TimeoutException as ex:
            Integration.append_msg("{0} is not found".format(e),False)
            print(ex.msg)
            return None

    def find_present_element(self, e):
        try:
            return self._wait.until(EC.presence_of_element_located(e))
        except TimeoutException as ex:
            print(ex.msg)

    def find_elements(self,e):
        try:
            element = self._wait.until(EC.visibility_of_all_elements_located(e))
            print(element)
            return element
        except TimeoutException as ex:
            print(ex.msg)

    def is_element_clickable(self,element):
        try:
            return self._wait.until(EC.element_to_be_clickable(element))
        except TimeoutException as ex:
            print(ex.msg)

    def click(self,element):
        self.is_element_clickable(element).click()

    def click_javascript_with_element(self, element):
        self._driver.execute_script("arguments[0].click();",element)

    def navigate_to_homepage(self):
        self.click(self.HEADER_LOGO)

    def navigate_to(self,url):
        print("navigating to {0}......".format(url))
        self._driver.get(url)

    def select_from_dropdown(self,element, option):
        Select(self.find_present_element(element)).select_by_value(option)

    ##boolean check
    def element_is_visible_on_the_page(self,element):
        try:
            self._wait.until(EC.visibility_of_element_located(element))

            return True
        except NoSuchElementException:
            print("No element found")
            return False

    def close_current_page(self):
        self._driver.close()

    def restart_webdriver(self):
        self._driver.close()
        self._driver.quit()
        Selenium.remove_instance()