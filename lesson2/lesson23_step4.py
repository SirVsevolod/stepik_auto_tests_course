from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, "input_value").text)
    inputAns = browser.find_element(By.ID, "answer")
    inputAns.send_keys(str(math.log(abs(12*math.sin(x)))))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
