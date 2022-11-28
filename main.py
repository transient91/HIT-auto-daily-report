import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

if __name__ == '__main__':
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Edge(options=options, service=Service('./msedgedriver.exe'))

    driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/edit')

    username = '学号'
    password = '密码'

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password, Keys.RETURN)

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="dtjwd"]/a').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="mrsb"]/div[63]/label/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="mrsb"]/div[64]/label/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="mrsb"]/div[65]/label/span[1]').click()

    driver.find_element(By.XPATH, '//*[@id="tj_btn"]').click()

    driver.close()
