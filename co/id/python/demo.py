from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = "made.shanti@mail.com"
pwd = "123456A"

driver = webdriver.Firefox()
driver.get("http://automationpractice.com/index.php")
driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")#Category "WOMEN"
driver.get("http://automationpractice.com/index.php?id_category=4&controller=category")#Category "TOP"
driver.get("http://automationpractice.com/index.php?controller=cart&add=1&id_product=1&token=e817bb0705dd58da8db074c69f729fd8")#pilih product

elem = driver.find_element_by_id("cart_quantity_up_1_1_0_0")#add quantity
elem.click()

elem = driver.find_element_by_xpath('//a[@href="'+"http://automationpractice.com/index.php?controller=order&step=1"+'"]').click()#error technical

elem = driver.find_element_by_id("email_create")
elem.send_keys(email)
elem = driver.find_element_by_id("SubmitCreate").click()
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("passwd")
elem.send_keys(pwd)
elem = driver.find_element_by_id("SubmitLogin").click()#error technical
elem = driver.find_element_by_name("processAddress").click()
elem = driver.find_element_by_id("cgv").click()
elem = driver.find_element_by_name("processCarrier").click()

elem = driver.find_element_by_xpath('//a[@href="'+"http://automationpractice.com/index.php?fc=module&module=bankwire&controller=payment"+'"]').click()

elem = driver.find_element_by_xpath('//label[@for="I confirm my order"]/parent::td/following-sibling::td').click()


# elem.send_keys(Keys.RETURN)
