from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://www.ulamart.com/customer/account/login")
webdriverObj.find_element(By.ID, "email").send_keys("jansree90@gmail.com")
webdriverObj.find_element(By.ID, "email").text
print(webdriverObj.find_element(By.ID, "email").get_attribute("value"))
print(webdriverObj.execute_script('return document.getElementById("email").value'))


