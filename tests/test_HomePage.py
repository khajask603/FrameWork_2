import time

import pytest

from TestData import HomePageData
from TestData.HomePageData import HomePagedata
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getdata):
        log=self.getlogger()

        homepage= HomePage(self.driver)
        log.info("first name is "+getdata["firstname"])
        homepage.getName().send_keys(getdata['firstname'])
        homepage.getEmail().send_keys(getdata['lastname'])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),getdata["gender"])
        time.sleep(4)
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePagedata.getTestdata("Testcase2"))
    def getdata(self, request):
        return request.param



