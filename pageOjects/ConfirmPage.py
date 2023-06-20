from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, 'country')
    india = (By.LINK_TEXT, "India")
    TC = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    finalP = (By.XPATH, "//input[@value='Purchase']")
    confirmS = (By.CSS_SELECTOR, ".alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def pickIndia(self):
        return self.driver.find_element(*ConfirmPage.india)

    def agreeTC(self):
        return self.driver.find_element(*ConfirmPage.TC)

    def finalPurchase(self):
        return self.driver.find_element(*ConfirmPage.finalP)

    def confirmSuccess(self):
        return self.driver.find_element(*ConfirmPage.confirmS)