import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_btn_add(browser):
    browser.get(link)
    time.sleep(30)
    btn_add = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    btn_add.click()
    time.sleep(3)
    result = browser.find_element(By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs").text
    print(result)
    assert "19,99" in result

