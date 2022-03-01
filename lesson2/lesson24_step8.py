from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,
                                                                               "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    inputAns = browser.find_element(By.ID, "answer")
    inputAns.send_keys(str(math.log(abs(12 * math.sin(x)))))

    button2 = browser.find_element(By.ID, "solve")
    button2.click()
finally:
    time.sleep(30)
    browser.quit()