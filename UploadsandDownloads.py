from asyncio import FutureCallGraph
from os import fdopen
from pydoc import cli

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.fed_cm import click_dialog_button
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

FilePath = "/home/andy/Downloads/download.xlsx"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options )
wait = WebDriverWait(driver,10)
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/upload-download-test/")

FileDownload = driver.find_element(By.XPATH,"//button[text()='Download']")


FileUpload = driver.find_element(By.XPATH,"//input[@type='file']")
FileUpload.send_keys(FilePath)
UpSuccessToast = (By.XPATH,"//div[text()='Updated Excel Data Successfully.']")
wait.until(expected_conditions.visibility_of_element_located(UpSuccessToast))
assert  expected_conditions.visibility_of_element_located(UpSuccessToast)
print(driver.find_element(*UpSuccessToast).text)