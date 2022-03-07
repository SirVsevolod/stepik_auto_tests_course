import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_btn_add(browser):
    browser.get(link)
    time.sleep(30)
    btn_add = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    btn_add.click()
    result = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs"), "19,99"))

    text = browser.find_element(By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs").text
    print(text)
    assert "19,99" in text

