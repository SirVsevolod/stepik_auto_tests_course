from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element(By.ID, "answer" )
    x = int(browser.find_element(By.ID, "input_value").text)
    input1.send_keys(str(math.log(abs(12*math.sin(x)))))

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(30)
    browser.quit()