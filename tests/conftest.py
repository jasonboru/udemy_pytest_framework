import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    match browser_name:
        case "chrome":
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        case "firefox":
            from selenium.webdriver.firefox.service import Service
            from webdriver_manager.firefox import GeckoDriverManager
            driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        case "edge":
            from selenium.webdriver.edge.options import Options
            from selenium.webdriver.edge.service import Service as EdgeService
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver

    # yield

    # driver.close()