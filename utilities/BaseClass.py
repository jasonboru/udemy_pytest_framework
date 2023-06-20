import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EO
from selenium.webdriver.support.ui import Select
import inspect
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandeler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandeler.setFormatter(formatter)

        logger.addHandler(fileHandeler)

        logger.setLevel(logging.DEBUG)

        return logger

    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EO.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_from_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


