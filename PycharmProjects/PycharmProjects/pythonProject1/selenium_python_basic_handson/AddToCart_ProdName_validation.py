from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.get("https://www.ulamart.com/pulses")
webdriverObj.maximize_window()
webdriverObj.implicitly_wait(5)
bookingList = []
cartList = []
addToCart = webdriverObj.find_elements(By.XPATH, '//a[@href="javascript:void(0)"]')
for eachAddToCart in addToCart:
    bookingList.append(eachAddToCart.find_element(By.XPATH, "parent::div/parent::figcaption/parent::div/parent::div/following-sibling::div/strong/a").text)
    eachAddToCart.click()
    webdriverObj.find_element(By.ID, "form-action-addToCart").click()
    # print(webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "shopping cart").accessible_name)
print(bookingList)
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "shopping cart").click()
cartElements = webdriverObj.find_elements(By.XPATH, "//tbody/tr/td/div/strong/a")
for eachCartElements in cartElements:
    cartList.append(eachCartElements.text)
print(cartList)
# assert bookingList == cartList
#     below piece of code is to click the cart icon and then click proceed to buy option.
#     Instead, direct shopping cart link has to be clicked.
# webdriverObj.find_element(By.CSS_SELECTOR, ".showcart").click()
# webdriverObj.find_element(By.CSS_SELECTOR, "#top-cart-btn-checkout").click()

#***********To validate if total amount is equal to the sum of each item's price************

ProductPrice = webdriverObj.find_elements(By.XPATH, "//tbody/tr/td[4]/span/span/span")
CalculatedSum = 0
for EachProductPrice in ProductPrice:
    CalculatedSum = CalculatedSum + int(EachProductPrice.text[1:])

print(CalculatedSum)
ActualSum = int(webdriverObj.find_element(By.CSS_SELECTOR, ".grand td strong .price").text[1:])
print(ActualSum)
# assert CalculatedSum == ActualSum
