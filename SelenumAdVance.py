import time
from ctypes.macholib.dyld import dyld_override_search
from enum import verify
from os import MFD_ALLOW_SEALING
from smtplib import OLDSTYLE_AUTH
from time import time_ns

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)



driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action= ActionChains(driver)

#Some IMPORTANT actions
#action.double_click()
#action.drag_and_drop()
#action.context_click()
#ction.click_and_hold()

action.move_to_element(driver.find_element(By.XPATH,"//button[text()='Mouse Hover']")).perform()
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Reload']")).click().perform()

action.click(driver.find_element(By.XPATH,"//button[text()='Open Window']")).perform()
WindowList = driver.window_handles
#wait.until(expected_conditions.new_window_is_opened(current_handles= WindowList))
driver.switch_to.window(WindowList[1])
NewWindowProof = driver.find_element(By.XPATH, "//div[@class='col-lg-4 col-md-4']/div/a/img[@alt='Logo']")
assert expected_conditions.presence_of_element_located(NewWindowProof)
print("New Window Opened Successfully")
driver.close()
driver.switch_to.window(WindowList[0])
FirstWindowProof = driver.find_element(By.XPATH,"//img[@src='images/rs_logo.png']")
assert  expected_conditions.presence_of_element_located(FirstWindowProof)
print("back to First page")

driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH,"//a[@class='theme-btn']").click()
driver.switch_to.default_content()

driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
driver.switch_to.alert.accept()
driver.switch_to.default_content()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0,document.body.scrollTopMax)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0,document.body.scrollTopMax)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0,document.body.scrollTopMax)")
