import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging
import os


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        # Get the directory of the current file
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        logger = logging.getLogger()
        file_handler = logging.FileHandler(os.path.join(os.path.dirname(current_file_dir), 'logs', 'automation.log'))
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        return logger

    def verifiy_link_presence(self,xpath):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def selectOptionByText(self,locator, text):
        sel=Select(locator)
        sel.select_by_visible_text(text)