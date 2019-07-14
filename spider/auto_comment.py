from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

browser.get('https://www.huya.com/131499')

login = browser.find_element(By.ID, "nav-login")
login.click()
time.sleep(20)

try:
    browser.switch_to.frame('UDBSdkLgn_iframe')

    phone = browser.find_element_by_xpath("//input[@class='udb-input udb-input-account']")
    print(phone)
    phone.send_keys('13421062248')
    time.sleep(1)


    password = browser.find_element_by_xpath("//input[@class='udb-input udb-input-pw']")
    password.send_keys('lxy_13421062248')
    time.sleep(1)

    start = browser.find_element(By.ID, "login-btn")
    start.click()
    time.sleep(2)

    browser.switch_to.default_content()

    L = ['666666', '国服杨戬', '炸了炸了', '想看你送外卖', '一如既往的秀']

    input_msg = browser.find_element(By.ID, "pub_msg_input")
    send_msg = browser.find_element(By.ID, "msg_send_bt")
    m = 0
    while m < 10:
        n = random.randint(0, 4)
        msg = L[n]
        input_msg.send_keys(msg)
        time.sleep(1)
        send_msg.click()
        print(msg)
        time.sleep(20)
        m += 1
except:
    print('失败！')
finally:
    browser.close()
