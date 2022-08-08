from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--ignore-certificate-errors")
serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj, options=chromeOptions)
webdriverObj.implicitly_wait(5)
webdriverObj.get("https://www.amazon.in/")
# MouseHover = ActionChains(webdriverObj)
# # MouseHover.move_to_element(webdriverObj.find_element(By.ID, "nav-link-accountList")).perform()
# # MouseHover.click(webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "Create")).perform()
# webdriverObj.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
# webdriverObj.maximize_window()
# webdriverObj.switch_to.frame("globalSqa")
# webdriverObj.find_element(By.XPATH, "//div[@id='portfolio_items']/div[6]").click()
# jaani = webdriverObj.find_element(By.XPATH, "//div[@id='portfolio_items']/div[6]")
# print(jaani.location_once_scrolled_into_view)
# webdriverObj.switch_to.default_content()
# print(webdriverObj.find_element(By.ID, "menu-item-6898").text)
# MouseHover.scroll(500, 500, 500, 500).perform()
#





