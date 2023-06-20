from pageOjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Jason Boru")

