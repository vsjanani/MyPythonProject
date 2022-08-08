from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serviceObj = Service(r"/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://www.amazon.in")
webdriverObj.maximize_window()
webdriverObj.find_element(By.CSS_SELECTOR, 'select[name="url"]').click()
categories = Select(webdriverObj.find_element(By.NAME, "url"))
for values in categories.options:
    print(values.text)
# categories.select_by_index(0)
# categories.select_by_visible_text('Amazon Devices')
# categories.select_by_value('search-alias=mobile-apps')
# labelName = webdriverObj.find_element(By.ID, "nav-search-label-id").text
# assert labelName == 'Apps - Games'
mylist = webdriverObj.find_elements(By.ID, 'searchDropdownBox')
for values in mylist:
    print(values.text)

