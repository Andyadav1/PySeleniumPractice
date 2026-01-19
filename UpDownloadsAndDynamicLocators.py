from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ExcelFileIO import UpdateExcelData

FilePath = "/home/andy/Downloads/download.xlsx"
FruitName = "Orange"
NewValue = "999"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options )
wait = WebDriverWait(driver,10)
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/upload-download-test/")

FileDownload = driver.find_element(By.XPATH,"//button[text()='Download']")

UpdateExcelData(FilePath,FruitName,"price",NewValue)

FileUpload = driver.find_element(By.XPATH,"//input[@type='file']")
FileUpload.send_keys(FilePath)
UpSuccessToast = (By.XPATH,"//div[text()='Updated Excel Data Successfully.']")
wait.until(expected_conditions.visibility_of_element_located(UpSuccessToast))
assert  expected_conditions.visibility_of_element_located(UpSuccessToast)
print(driver.find_element(*UpSuccessToast).text)

FruitColumn = driver.find_element(By.XPATH,"//div[text()='Fruit Name']").get_attribute("data-column-id")
PriceColumn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
Price = driver.find_element(By.XPATH,"//div[@id = 'cell-"+FruitColumn+"-undefined']/div[text() = '"+FruitName+"']/../../div[@id='cell-"+PriceColumn+"-undefined']").text

assert  Price ==  NewValue
print(Price)
