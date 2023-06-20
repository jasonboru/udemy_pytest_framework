import pytest
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageOjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import Select


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()

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
        log.info(alertMessage)
        assert ("Success" in alertMessage)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param



