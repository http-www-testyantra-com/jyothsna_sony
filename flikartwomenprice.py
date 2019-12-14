import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
action=ActionChains(driver)
time.sleep(4)
element=driver.find_element_by_xpath("//span[text()='Women']")
action.move_to_element(element).perform()
driver.find_element_by_xpath("//a[text()='Kurtas & Kurtis']").click()
time.sleep(3)
scr=driver.find_element_by_xpath("//div[@class='_3G9WVX oVjMho']")
action.drag_and_drop_by_offset(scr,50,0).perform()