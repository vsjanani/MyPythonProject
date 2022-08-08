from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceobj = Service("/usr/bin/chromedriver")
webdriverobj = webdriver.Chrome(service=serviceobj)
webdriverobj.get("https://www.amazon.in/")
webdriverobj.maximize_window()
webdriverobj.implicitly_wait(3)
webdriverobj.find_element(By.ID, "nav-link-accountList").click()
webdriverobj.find_element(By.ID, "createAccountSubmit").click()
webdriverobj.find_element(By.XPATH, "//input[@name='customerName']").send_keys("123")
webdriverobj.find_element(By.CSS_SELECTOR, "[type='submit']").click()
print(webdriverobj.find_element(By.XPATH, "//div[contains(text(),'number')]").text)
webdriverobj.find_element(By.LINK_TEXT, "Create a free business account").click()
webdriverobj.find_element(By.XPATH, "//span[text()='Why is verification needed?']").click()
