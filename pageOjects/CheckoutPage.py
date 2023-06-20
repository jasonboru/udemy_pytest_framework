from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    cartButton = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    checkoutButton = (By.CSS_SELECTOR, ".btn.btn-success")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def clickToCart(self):
        return self.driver.find_element(*CheckOutPage.cartButton)

    def checkoutCart(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)
