from selenium import webdriver
from selenium.webdriver import ActionChains
# opening browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
#enter url
driver.get("https://www.bluestone.com/")
#maximize windows
driver.maximize_window()
#click on coins
element=driver.find_element_by_xpath("//a[text()='Coins ']")
#actionchains
action=ActionChains(driver)
action.move_to_element(element).perform()
#clicking on 1 gram gold
driver.find_element_by_xpath("//span[text()='1 gram']").click()
driver.find_element_by_id("buy-now").click()




