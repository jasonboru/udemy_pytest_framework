from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pageOjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.CSS_SELECTOR, "[name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    # dropdown = (By.ID, "exampleFormControlSelect1")
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

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    # def getGender(self):
    #     return self.driver.find_element(*HomePage.gender)
    #
    # def submitForm(self):
    #     return self.driver.find_element(*HomePage.submit)

