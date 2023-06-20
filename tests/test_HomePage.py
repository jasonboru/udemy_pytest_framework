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
        # self.selectOptionByText(homePage.getGender(), getData["gender"])



