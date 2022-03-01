from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element(By.ID, "answer" )
    x = int(browser.find_element(By.ID,"treasure").get_attribute('valuex'))
    input1.send_keys(str(math.log(abs(12*math.sin(x)))))

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()