from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://partner.zmlearn.com/#/login')
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input'))
)
driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/form/div[1]/div/div/input').send_keys('19074511802')
driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/form/div[3]/div/div/input').send_keys('Cz123456')
driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/form/div[5]/div/button[1]').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/ul/div[2]/a'))
)
driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/ul/div[2]/a').click()
cookies = driver.get_cookies()
print(cookies[1]['value'])
print(cookies[0]['value'])


print("Cookies:", cookies)
