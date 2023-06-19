import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    service_obj = Service("/Users/jasonobrien/drivers/chrome_driver/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(4)

    driver.get("https://rahulshettyacademy.com/angularpractice")
    request.cls.driver = driver
    yield
    driver.close()