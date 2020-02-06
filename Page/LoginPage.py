from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self):
        super(LoginPage,self).__init__()
        self.EMAIL_FIELD = (By.ID, "email")
        self.PASSWORD_FIELD = (By.ID, "passwd")
        self.SIGNIN_BTN = (By.XPATH, "//button[@name='SubmitLogin']")
        self.HOMEPAGE_LINK = (By.CSS_SELECTOR,"img.logo.img-responsive")




