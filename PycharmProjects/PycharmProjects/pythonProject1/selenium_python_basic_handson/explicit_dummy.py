from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://www.ulamart.com/")
webdriverObj.maximize_window()
webdriverObj.find_element(By.ID, "search").send_keys("rock sea salt")
webdriverObj.find_element(By.XPATH, "//div[@class='actions']/button").click()
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "Natural Raw Sea Salt").click()
webdriverObj.find_element(By.ID, "product-addtocart-button").click()
expObj = WebDriverWait(webdriverObj, 5)
expObj.until(expected_conditions.presence_of_element_located( (By.PARTIAL_LINK_TEXT, 'shopping cart')) )
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "shopping cart").click()
currentURL = 'https://www.ulamart.com/checkout/cart/'
assert webdriverObj.current_url == currentURL
