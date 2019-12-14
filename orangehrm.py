from selenium import webdriver
driver=webdriver.Chrome(executable_path= "C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()
#links = [link.get_attribute('href') for link in driver.find_elements_by_xpath("//div[@class='menu']")]
list=driver.find_elements_by_xpath("//a[@class='firstLevelMenu']")
l=[]
for i in list:
   l.append( i.text)
for i in range(len(l)):
    driver.find_element_by_xpath("//a[@class='firstLevelMenu']/b[text()='"+l[i]+"']").click()
    print(l[i])






