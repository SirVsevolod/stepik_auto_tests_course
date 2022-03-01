from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block>.first_class>.first")
    input1.send_keys("name")
    input1 = browser.find_element_by_css_selector(".first_block>.second_class>.second")
    input1.send_keys("password")
    input1 = browser.find_element_by_css_selector(".first_block>.third_class>.third")
    input1.send_keys("email")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(30)
    browser.quit()