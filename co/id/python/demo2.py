'''
Created on Feb 5, 2018
Login and Logout
@author: Shanti
'''
from selenium import webdriver

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

driver.get("http://automationpractice.com/index.php?mylogout=")

driver.close()
