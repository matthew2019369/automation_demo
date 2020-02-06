import os, sys

Base_Dir = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(Base_Dir)

from Page.LoginPage import LoginPage
from TestRailIntegration.Integration import Integration


class LoginSteps():
    def __init__(self):
        self.page = LoginPage()

    def login(self, username, password):
        self.page.insert_text(self.page.EMAIL_FIELD,username)
        self.page.insert_text(self.page.PASSWORD_FIELD,password)
        self.page.click(self.page.SIGNIN_BTN)

    def navigate(self, url):
        self.page.navigate_to(url)

    def navigate_to_homepage(self):
        self.page.navigate_to_homepage()

    def can_find_page(self):
        try:
            self.page.find_element(self.page.EMAIL_FIELD)
            self.page.find_element(self.page.PASSWORD_FIELD)
            self.page.find_element(self.page.SIGNIN_BTN)
            Integration.append_msg("Login page is successfully loaded. ",True)
        except Exception as ex:
            Integration.append_msg("Login page is failed to load. ", False)
