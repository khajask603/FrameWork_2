import pytest
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):  # Accessing the driver instance from the BaseClass->No Need of #self.driver=setup
    def test_e2e(self):
        log=self.getlogger()

        homepage = HomePage(self.driver)  # ---HomePage Page Object
        checkoutpage = homepage.Click_Shop_Button()  # ---Checkout Page Object
        cards = checkoutpage.get_Product_Names()
        log.info("---------Pulling all the Products Names----------")

        i = -1
        for product in cards:
            i = i + 1
            productName = product.text
            print(productName)
            log.info(productName)

            if productName == 'Blackberry':
                checkoutpage.click_AddButton()

        log.error("Print Error Reason")
        checkoutpage.Click_Chekout_Button()

        confirmPage = checkoutpage.Click_SecondChekout_Button()  # ---Confrim Page Object
        log.info("------------Entering the Country Names----------")
        confirmPage.Select_Country("India")
        confirmPage.Click_CheckBox()
        confirmPage.Click_Purchase_Button()
        self.verifiy_link_presence("//div[@class='alert alert-success alert-dismissible']")
        SuccessText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(SuccessText)
        log.info("------------The Text recivied is ----------"+SuccessText)
        assert "Success! Thank you!" in SuccessText
