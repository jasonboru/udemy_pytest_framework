import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EO
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # the * behind href means the program will search for a partial match

        results = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        count = len(results)
        print(count)

        for result in results:
            product = result.find_element(By.XPATH, "div/h4/a").text
            print(product)
            if product == "Blackberry":
                result.find_element(By.XPATH, "div/button").click()
            # the result object already contains //div[@class='products']/div from line 19
            # this process chains off the elements adding the child to Parent XPATH

        self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

        self.driver.find_element(By.ID, 'country').send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EO.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        successText = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        assert "Success" in successText


