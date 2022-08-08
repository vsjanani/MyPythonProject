from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://the-internet.herokuapp.com/windows")
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "Click").click()
webdriverObj.switch_to.window(webdriverObj.window_handles[0])
