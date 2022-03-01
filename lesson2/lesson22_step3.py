from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    number1 = browser.find_element(By.ID, "num1").text
    number2 = browser.find_element(By.ID, "num2").text
    summ = int(number1) + int(number2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(30)
    browser.quit()