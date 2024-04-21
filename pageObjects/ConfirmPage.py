from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):

    #Locatores--------
    check_Box = "//div[@class='checkbox checkbox-primary']"
    purchaseButton="//input[@value='Purchase']"
    namesBlock="//div[@class='suggestions']//a"

    # ------------Constructore----------
    def __init__(self, driver):
        self.driver = driver

    #-----Acton methods--------------
    def Select_Country(self,Country_String):
        self.driver.find_element(By.ID, "country").send_keys(Country_String[:3])
        self.verifiy_link_presence(self.namesBlock)
        CountryNames = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']//a")
        for Country in CountryNames:
            if Country.text == Country_String:
                Country.click()
                break

    def Click_CheckBox(self):
        cb=self.driver.find_element(By.XPATH, self.check_Box)
        cb.click()

    def Click_Purchase_Button(self):
        self.driver.find_element(By.XPATH,self.purchaseButton).click()
