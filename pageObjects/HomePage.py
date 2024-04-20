from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    ShopButton = "a[href*='/angularpractice/shop']"
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")


    def __init__(self, driver):
        self.driver = driver

    #-----Acton methods--------------
    def Click_Shop_Button(self):
        ShopButton=self.driver.find_element(By.CSS_SELECTOR,self.ShopButton)
        ShopButton.click()
        checkoutpage=CheckoutPage(self.driver)
        return checkoutpage



    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)


