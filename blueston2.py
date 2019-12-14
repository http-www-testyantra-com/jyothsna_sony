import time

from selenium import webdriver
# opening browser
class Bluestone:
 def validating_msg(self):
     driver = webdriver.Chrome("C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
     driver.implicitly_wait(10)
     # enter url
     driver.get("https://www.bluestone.com/")
     # maximize windows
     driver.maximize_window()
     time.sleep(10)
     driver.find_element_by_xpath("//img[@alt='Goldmine Scheme']").click()
     driver.find_element_by_id("amount").send_keys(6000)
     driver.find_element_by_id("Email").send_keys("jyothsna@gmail.com")
     driver.find_element_by_id("gmsStart").click()
     time.sleep(3)
     driver.find_element_by_xpath("//input[@type='submit']").click()
     errormsg = driver.find_element_by_id("contactNumber").get_attribute("title")
     driver.find_element_by_id("fullname").send_keys("jyo")
     expected = "Please enter valid mobile number"
     assert errormsg == expected, "error message is not  dispaying"
     print("error msg is displaying:", errormsg)
obj=Bluestone()
obj.validating_msg()





