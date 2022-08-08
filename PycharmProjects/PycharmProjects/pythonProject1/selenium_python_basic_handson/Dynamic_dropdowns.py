from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://rahulshettyacademy.com/dropdownsPractise/")