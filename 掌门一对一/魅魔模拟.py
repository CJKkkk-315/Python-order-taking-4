from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://emrpg.com/mix#/lostark/comboLearning')
actions = ActionChains(driver)
time.sleep(7)
for j in range(10):
    bs = []
    for i in range(1,8):
        bs.append(driver.find_element(by=By.XPATH, value=f'//*[@id="app"]/div/div/div[3]/div[{i}]/button').text)
    for b in bs:
        actions.send_keys(b).perform()
    time.sleep(1)




