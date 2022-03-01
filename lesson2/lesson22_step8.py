from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    inputName = browser.find_element(By.NAME, "firstname")
    inputName.send_keys("name")

    inputLName = browser.find_element(By.NAME, "lastname")
    inputLName.send_keys("lastname")

    inputEmail = browser.find_element(By.NAME, "email")
    inputEmail.send_keys("email")

    inputFile = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    inputFile.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()