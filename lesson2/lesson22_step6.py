from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(math.log(abs(12 * math.sin(x)))))

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()