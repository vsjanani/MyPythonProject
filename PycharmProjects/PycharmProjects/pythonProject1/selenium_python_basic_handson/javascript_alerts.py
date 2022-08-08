from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
webdriverObj.maximize_window()
webdriverObj.find_element(By.ID, "alertexamples").click()
alertObj = webdriverObj.switch_to.alert
print(alertObj.text)
alertObj.accept()
webdriverObj.find_element(By.CSS_SELECTOR, "[value='Show confirm box']").click()
print(alertObj.text)
alertObj.accept()
webdriverObj.find_element(By.CSS_SELECTOR, "[value='Show confirm box']").click()
alertObj.dismiss()
webdriverObj.find_element(By.ID, "promptexample").click()
alertObj.send_keys("janani")
alertObj.accept()
promptValue = webdriverObj.find_element(By.ID, "promptretval").text
print(promptValue)
webdriverObj.find_element(By.ID, "promptexample").click()
alertObj.dismiss()
promptValue = webdriverObj.find_element(By.ID, "promptretval").text
print(promptValue)
webdriverObj.find_element(By.ID, "promptexample").click()
alertObj.accept()
promptValue = webdriverObj.find_element(By.ID, "promptretval").text
print(promptValue)



