from Page.HomePage import HomePage
from TestRailIntegration.Integration import Integration

class HomeSteps:
    def __init__(self):
        self.page = HomePage()

    def navigate_to_item1(self):
        self.page.click(self.page.CONTENT_ITEM1)

    def navigate_to_item2(self):
        self.page.click(self.page.CONTENT_ITEM2)

    def navigate_to_item3(self):
        self.page.click(self.page.CONTENT_SLIDER)

    def click_more_to_item(self, item_no):
        element = self.page.find_elements(self.page.FEATURED_ITEM_MORE_BTNs)[item_no]
        print(element)
        self.page.click_javascript_with_element(element)


    def close_page(self):
        self.page.close_current_page()

    def restart_pages(self):
        self.page.restart_webdriver()