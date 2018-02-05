'''
Created on Feb 5, 2018
Cart is empty after logout
@author: deShantiLa
'''
from selenium import webdriver
import time

user = "made.shanti@mail.com"
pwd = "123456A"

driver = webdriver.Firefox()
driver.get("http://automationpractice.com/index.php")
driver.get("http://automationpractice.com/index.php?controller=my-account")

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("passwd")
elem.send_keys(pwd)
elem = driver.find_element_by_id("SubmitLogin").click()

driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
driver.get("http://automationpractice.com/index.php?id_product=1&controller=product")

elem = driver.find_element_by_id("add_to_cart").click()
time.sleep(10)

driver.get("http://automationpractice.com/index.php?id_product=1&controller=product")

driver.get("http://automationpractice.com/index.php?mylogout=")

time.sleep(5)

driver.get("http://automationpractice.com/index.php?controller=my-account")

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("passwd")
elem.send_keys(pwd)
elem = driver.find_element_by_id("SubmitLogin").click()


