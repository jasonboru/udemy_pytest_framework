import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EO
from selenium.webdriver.support.wait import WebDriverWait

from pageOjects.CheckoutPage import CheckOutPage
from pageOjects.ConfirmPage import ConfirmPage
from pageOjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooters()[i].click()

        checkOutPage.clickToCart().click()

        # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        checkOutPage.checkoutCart().click( )

        # self.driver.find_element(By.ID, 'country').send_keys("ind")
        confirmPage = ConfirmPage(self.driver)
        log.info("entering country name as 'ind'")
        confirmPage.getCountry().send_keys("ind")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EO.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verify_link_presence("India")
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.pickIndia().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.agreeTC().click()

        # self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        confirmPage.finalPurchase().click()

        # successText = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        successText = confirmPage.confirmSuccess().text
        log.info("Text received from application is: " + successText)

        assert "Success" in successText


