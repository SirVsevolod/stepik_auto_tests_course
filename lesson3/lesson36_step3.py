import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math





@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser_path = r'C:\chromedriver\chromedriver.exe'
    browser = webdriver.Chrome(browser_path)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestNetwork():
    @pytest.mark.parametrize('network', ['https://stepik.org/lesson/236895/step/1',
                                         'https://stepik.org/lesson/236896/step/1',
                                         'https://stepik.org/lesson/236897/step/1',
                                         'https://stepik.org/lesson/236898/step/1',
                                         'https://stepik.org/lesson/236899/step/1',
                                         'https://stepik.org/lesson/236903/step/1',
                                         'https://stepik.org/lesson/236904/step/1',
                                         'https://stepik.org/lesson/236905/step/1'])
    def test_find_network(self, browser, network):
        link = fr"{network}"
        browser.get(link)
        browser.implicitly_wait(15)
        inputAnswer = browser.find_element(By.TAG_NAME, 'textarea')
        inputAnswer.send_keys(str(math.log(int(time.time() + 0.6))))
        browser.implicitly_wait(1)
        btn = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        btn.click()
        time.sleep(1)
        assert "Correct!" == browser.find_element(By.TAG_NAME, "pre").text, browser.find_element(By.TAG_NAME, "pre").text




