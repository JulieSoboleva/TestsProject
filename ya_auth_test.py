import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ACCOUNT = os.environ.get('YANDEX_ACCOUNT')
PASSWORD = os.environ.get('YANDEX_PASSWORD')

def test_auth(driver):
    driver.get('https://passport.yandex.ru/auth/')
    btn_email = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'
                                              '/div/div/div[2]/div[3]/div/div/div'
                                              '/div/form/div/div[2]/div[1]/div[1]'
                                              '/button')
    btn_email.click()
    input_email = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
    input_email.send_keys(f'{ACCOUNT}@yandex.ru')
    input_email.send_keys(Keys.ENTER)
    input_password = driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
    input_password.send_keys(PASSWORD)
    input_password.send_keys(Keys.ENTER)
    assert 'Яндекс ID' in driver.title


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    test_auth(driver)
    driver.close()
