from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
while True:
    url = 'http://192.168.102.166/eportal/success.jsp?userIndex=37653630346430653061356563363365343164653032323438653962353437615f31302e39372e36312e3132315f323032323330363033303437'
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    # driver.find_element(by=By.XPATH,value='//*[@id="username_tip"]').send_keys('202230603047')
    ActionChains(driver).send_keys('202230603047').perform()
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    ActionChains(driver).send_keys('00377863aA').perform()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    driver.quit()