import time

from timer import timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

selectObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=selectObj)
webdriverObj.get("https://www.amazon.in/")
webdriverObj.maximize_window()
webdriverObj.find_element(By.ID, 'twotabsearchtextbox').send_keys("women clothing")
webdriverObj.find_element(By.ID, 'nav-search-submit-button').click()
# mylist = webdriverObj.find_elements(By.XPATH, "//a[contains(@href, 'sr_nr_p_n_feature_nineteen_browse-bin')]/div/label/i")
mylist = webdriverObj.find_elements(By.XPATH, "//li[contains(@id,'p_n_feature_nineteen_browse-bin/')]")
for i in mylist:
    if i.text == "Premium Brands":
        print(i.text)
        i.click()
        assert webdriverObj.find_element(By.XPATH, '//li[@id = "p_n_feature_nineteen_browse-bin/27064186031"]/span/a/div/label/input').is_selected()
        print("hi")
        break







