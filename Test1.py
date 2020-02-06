import unittest
from Config.ConfigReader import ConfigReader
from Step.LoginSteps import LoginSteps
from Step.HomeSteps import HomeSteps
from Utilities.Selenium import Selenium
from TestRailIntegration.Integration import Integration
class Test1(unittest.TestCase):

    def test_to_add_single_item(self):
        print('this is test 1')
        login = LoginSteps()
        login.navigate(ConfigReader.get_url())
        login.can_find_page()
        login.login(ConfigReader.get_name(), ConfigReader.get_password())
        login.navigate_to_homepage()
        home = HomeSteps()
        home.click_more_to_item(2)
        Integration.append_msg("this is test1....hhhhhh",True)
        Integration.send_msg(1,1)

        HomeSteps().restart_pages()
        print('end of test 1')

    def test_to_add_single_item2(self):
        print('this is test 1')
        login = LoginSteps()
        login.navigate(ConfigReader.get_url())
        login.can_find_page()
        login.login(ConfigReader.get_name(), ConfigReader.get_password())
        login.navigate_to_homepage()
        home = HomeSteps()
        home.click_more_to_item(2)
        Integration.append_msg("this is test2....hhhhhh", True)
        Integration.send_msg(1,1)
        HomeSteps().restart_pages()
        print('end of test 1')

    #
    # def tearDown(self):
    #     print('Tearing down the test')
    #     self.selenium.close()
    #     self.selenium.exit()
    #     print('test case is closed and quited')



if __name__ == '__main__':
    unittest.main()