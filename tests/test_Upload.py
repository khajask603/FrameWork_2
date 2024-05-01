from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=ops)
driver.maximize_window()
driver.implicitly_wait(5)
filepath=r"C:\Users\SHAIK KHAJA MOHIDDIN\Downloads\download.xlsx"
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.XPATH,"//button[@id='downloadButton']").click()

fileInput=driver.find_element(By.XPATH,"//input[@type='file']")
fileInput.send_keys(filepath)

toastlocatore=By.XPATH,"//div[contains(text(),'Updated Excel Data Successfully.')]"

wait=WebDriverWait(driver,5)
wait.until(EC.visibility_of_element_located(toastlocatore))

print(driver.find_element(*toastlocatore).text)
print(driver.find_element(By.XPATH, "//div[contains(text(),'Updated Excel Data Successfully.')]").text)


# wait = WebDriverWait(self.driver, 10)
#         wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
driver.quit()