import pytest
from selenium.webdriver.common.by import By

from pageOjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import Select


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData[0])
        homePage.getEmail().send_keys(getData[1])
        homePage.getPassword().send_keys(getData[2])
        homePage.getCheckbox().click()
        self.select_option_from_text(homePage.getGender(), getData[3])
        homePage.getEmpStatus().click()
        homePage.getBirthday().send_keys(getData[4])
        homePage.submitForm().click()
        alertMessage = homePage.getSuccessMessage().text
        assert ("Success" in alertMessage)
        self.driver.refresh()

    @pytest.fixture(params=[("Jason Boru", "jasonboru@gmail.com", "Password1234", "Male", "01171978"),
                            ("Nola Pearl", "noladog@gmail.com", "PasswordB@rk", "Female", "09152021")])
    def getData(self, request):
        return request.param



