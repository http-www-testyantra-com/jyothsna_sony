import time

from selenium import webdriver
from selenium.webdriver import ActionChains
# opening browser
from selenium.webdriver.support.select import Select
class Bluestone:
 driver=webdriver.Chrome("C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
 def login(self):
   driver = webdriver.Chrome("C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
   driver.implicitly_wait(10)
#enter url
   driver.get("https://www.bluestone.com/")
#maximize windows
   driver.maximize_window()
   driver.find_element_by_xpath("//img[@alt='Goldmine Scheme']").click()
   driver.find_element_by_id("amount").send_keys(6000)
   driver.find_element_by_id("Email").send_keys("jyothsna@gmail.com")
   driver.find_element_by_id("gmsStart").click()
   driver.find_element_by_id("contactNumber").send_keys(9837598390)
   driver.find_element_by_id("fullname").send_keys("jyo")
   driver.find_element_by_id("address").send_keys(" basavanagudi ,banglore-560021")
   driver.find_element_by_id("postcode_delivery").send_keys(560021)
   driver.find_element_by_xpath("//input[@name='_eventId_savePersonalAddressDetails']").click()
   driver.find_element_by_id("nomineeName").send_keys("jee")
   sel = Select(driver.find_element_by_name("nomineeRelationship"))
   sel.select_by_visible_text('Spouse')
   nationality = Select(driver.find_element_by_id("nomineeNationality"))
   nationality.select_by_visible_text('Indian')
   driver.find_element_by_xpath("//input[@name='_eventId_checkoutSaveAddressDetails']").click()
   actual = driver.title
   expected = "Gold Mine Payment Option | BlueStone.com"
   assert actual == expected, "the page  not dispalyed"
   print("the page is displayed")
   driver.close()
obj=Bluestone()
obj.login()




