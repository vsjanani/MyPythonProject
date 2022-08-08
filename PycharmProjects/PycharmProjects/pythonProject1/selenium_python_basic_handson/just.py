from selenium import webdriver
from selenium.webdriver.chrome.service import Service

webdriverObj = webdriver.Chrome(service=Service("C:/Users/dines/OneDrive/Documents/MyPythonProject/chromedriver.exe"))
webdriverObj.get("https://www.amazon.in")
print(webdriverObj.capabilities)