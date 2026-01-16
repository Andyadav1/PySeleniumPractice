import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(1)

ProductList = driver.find_elements(By.XPATH,"//div[@class='products']/div")
ProductCount = len(ProductList)

print(ProductCount)
assert ProductCount > 0
print("products appeared correctly")

ExpectedPL = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
CurrentPL = []
for product in ProductList:
    CurrentPL.append(product.find_element(By.XPATH,"h4").text)
    product.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()
assert CurrentPL == ExpectedPL
print(CurrentPL)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='totAmt']")))

ProductPrice = driver.find_elements(By.XPATH,"//tr/td[5]/p")
TotalPrice = 0
for price in ProductPrice:
    TotalPrice = TotalPrice + int(price.text)

TotalAmount = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
assert TotalPrice == TotalAmount
print("Price Calculation is correct")

driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[text()='Code applied ..!']")))

ToralAfterDiscount = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)
assert TotalPrice > ToralAfterDiscount
print("Discount application confirmed")






