from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        super(HomePage,self).__init__()
        self.CONTENT_ITEM1 = (By.CSS_SELECTOR, "li.htmlcontent-item-1.col-xs-4")
        self.CONTENT_ITEM2 = (By.CSS_SELECTOR, "li.htmlcontent-item-2.col-xs-4")
        self.CONTENT_SLIDER = (By.ID, "homepage-slider")
        self.BEST_SELLING_TAB = (By.CSS_SELECTOR, "a.blockbestsellers")


        # region-featured products
        self.FEATURED_TAB = (By.CSS_SELECTOR, "a.homefeatured")
        self.FEATURED_ITEM_IMGs = (By.CSS_SELECTOR, "ul#homefeatured * a.product_img_link")
        self.FEATURED_ITEM_PRICEs = (By.CSS_SELECTOR, "ul#homefeatured .right-block span.price.product-price")
        self.FEATURED_ITEM_ADD_CART_BTNs = (By.CSS_SELECTOR,
                                           "ul#homefeatured a.button.ajax_add_to_cart_button.btn.btn-default")
        self.FEATURED_ITEM_MORE_BTNs = (By.CSS_SELECTOR, "ul#homefeatured a.button.lnk_view.btn.btn-default")
        self.FEATURED_ITEM_NAME = (By.CSS_SELECTOR, "ul#homefeatured a.product-name")
        self.FEATURED_ITEM_QUICKVIEW = (By.CSS_SELECTOR, "ul#homefeatured a.quick-view")
        self.FEATURED_ITEM_IMG_PRICE = (By.CSS_SELECTOR, "ul#homefeatured .left-block .content_price")
        # region-best selling products
