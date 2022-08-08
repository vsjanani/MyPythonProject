from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://www.ulamart.com/")
webdriverObj.maximize_window()
webdriverObj.find_element(By.ID, "search").send_keys("rock sea salt")
webdriverObj.implicitly_wait(4)
webdriverObj.find_element(By.XPATH, "//div[@class='actions']/button").click()
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "Natural Raw Sea Salt").click()
webdriverObj.find_element(By.ID, "product-addtocart-button").click()
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "shopping cart").click()