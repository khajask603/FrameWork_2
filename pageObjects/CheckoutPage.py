from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class CheckoutPage(BaseClass):

    #Locatores--------
    productNames = ".card-title a"
    CardFooter="(//div[@class='card-footer'])//button"
    checkoutButton = "//a[@class='nav-link btn btn-primary']"
    checkoutButton_2 = ".btn.btn-success"
    # ------------Constructore----------
    def __init__(self, driver):
        self.driver = driver

    #-----Acton methods--------
    def get_Product_Names(self):
        return self.driver.find_elements(By.CSS_SELECTOR,self.productNames)

    def click_AddButton(self):
        self.driver.find_element(By.XPATH,self.CardFooter).click()

    def Click_Chekout_Button(self):
        self.driver.find_element(By.XPATH, self.checkoutButton).click()



    def Click_SecondChekout_Button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkoutButton_2).click()
        confirmPage=ConfirmPage(self.driver)
        return confirmPage
    #Test-----