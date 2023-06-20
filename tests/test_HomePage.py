import pytest
from selenium.webdriver.common.by import By

from pageOjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import Select


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckbox().click()
        self.select_option_from_text(homePage.getGender(), getData["gender"])
        homePage.getEmpStatus().click()
        homePage.getBirthday().send_keys(getData["bday"])
        homePage.submitForm().click()
        alertMessage = homePage.getSuccessMessage().text
        assert ("Success" in alertMessage)
        self.driver.refresh()

    @pytest.fixture(params=[{"name": "Jason Boru", "email": "jasonboru@gmail.com", "password": "Password1234", "gender": "Male", "bday": "01171978"},
                            {"name": "Nola Pearl", "email": "noladog@gmail.com", "password": "PasswordB@rk", "gender": "Female", "bday": "09152021"}])
    def getData(self, request):
        return request.param


