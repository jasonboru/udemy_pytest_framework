from selenium.webdriver.common.by import By

from pageOjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.CSS_SELECTOR, "[name='name']")
    # email =
    # password =
    # checkbox =
    # dropdown =
    # radiobutton =
    # DoB =
    # subbmit =

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        # the * is needed to deserialize the tuple
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)
