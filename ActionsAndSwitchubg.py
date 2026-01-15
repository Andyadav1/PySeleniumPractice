import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action= ActionChains(driver)

#Some IMPORTANT actions
#action.double_click()
#action.drag_and_drop()
#action.context_click()
#ction.click_and_hold()

action.move_to_element(driver.find_element(By.XPATH,"//button[text()='Mouse Hover']")).perform()
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Reload']")).click().perform()

action.click(driver.find_element(By.XPATH,"//button[text()='Open Window']")).perform()