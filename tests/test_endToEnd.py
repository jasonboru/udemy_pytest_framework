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

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooters()[i].click()

        checkOutPage.clickToCart().click()

        # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        checkOutPage.checkoutCart().click( )

        # self.driver.find_element(By.ID, 'country').send_keys("ind")
        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCountry().send_keys("ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EO.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        successText = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        assert "Success" in successText


