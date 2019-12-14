from selenium import webdriver
from selenium.webdriver import ActionChains
class Bluestone:
    def val(self):
        # opening browser
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
        # maximize windows
        driver.get("https://www.bluestone.com/")
        # click on coins
        driver.maximize_window()
        # actionchains
        element = driver.find_element_by_xpath("//a[text()='All Jewellery ']")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element1 = driver.find_element_by_xpath("//a[text()='Kadas']")
        element1.click()
        driver.find_element_by_xpath("(//img[@class='hc img-responsive center-block'])[1]").click()
        driver.find_element_by_xpath("//input[@id='buy-now']").click()
        # error massage
        text = driver.find_element_by_xpath("//div[@class='formErrorContent']")
        # checking error massage
        print(text.is_displayed())
blu=Bluestone()
blu.val()
