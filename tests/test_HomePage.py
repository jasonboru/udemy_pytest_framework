from selenium.webdriver.common.by import By

from pageOjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import Select


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Jason Boru")
        homePage.getEmail().send_keys("jasonboru@gmail.com")
        homePage.getPassword().send_keys("Password1234")
        homePage.getCheckbox().click()
        homePage.getGender()
        homePage.getEmpStatus().click()
        homePage.getBirthday().send_keys("01171978")
        homePage.submitForm().click()
        alertMessage = homePage.getSuccessMessage().text
        assert ("Success" in alertMessage)




