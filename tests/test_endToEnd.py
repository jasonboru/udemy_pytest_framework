from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestOne:
    def test_e2e(self):

        import time



        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        service_obj = Service("/Users/jasonobrien/drivers/chrome_driver/chromedriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(4)

        driver.get("https://rahulshettyacademy.com/angularpractice")

        # click link to go to shop
        driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # the * behind href means the program will search for a partial match

        results = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        count = len(results)
        print(count)

        for result in results:
            product = result.find_element(By.XPATH, "div/h4/a").text
            print(product)
            if product == "Blackberry":
                result.find_element(By.XPATH, "div/button").click()
            # the result object already contains //div[@class='products']/div from line 19
            # this process chains off the elements adding the child to Parent XPATH

        driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

        driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

        driver.find_element(By.ID, 'country').send_keys("ind")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        driver.find_element(By.LINK_TEXT, "India").click()

        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        successText = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        assert "Success" in successText

        driver.close()


