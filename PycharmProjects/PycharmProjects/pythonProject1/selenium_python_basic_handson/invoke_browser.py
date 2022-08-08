# import Service as Service
import selenium.webdriver.remote.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service("C:/Users/dines/OneDrive/Documents/MyPythonProject/msedgedriver.exe")
webdriverObj = webdriver.Edge(service=serviceObj)


webdriverObj.get("https://www.amazon.in")
webdriverObj.maximize_window()
print(webdriverObj.title)
print(webdriverObj.current_url)
# print(webdriverobj.refresh(), "refreshed")
# webdriverobj.find_element(By.ID, "nav-a nav-a-2   nav-progressive-attribute").cli