from selenium.webdriver.common.by import By

from pageOjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        # the * is needed to deserialize the tuple
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
