from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
words = """鱼竿
冲锋衣
骆驼冲锋衣
北面旗舰店官方
帐篷
棉服
羽绒服男冬季
北面
袜子
始祖鸟官方旗舰
羽绒服
羽绒服女
始祖鸟
北面羽绒服
敌我识别灯
滑雪服女
sp固定器
帐篷户外
手电筒 强光 充电
北面旗舰店官方官网
滑雪装备套装全套
帐篷 户外
羽绒服男
头灯 强光 充电 超亮
柴火灶家用烧木柴
北面冲锋衣
烧烤炉 家用
露营装备 全套
冲锋衣女
始祖鸟冲锋衣
北面官方旗舰店
冲锋衣男
望远镜高倍高清专业级
男士羽绒服冬季
北面官网官方旗舰店
滑雪服男
凯乐石官方旗舰
冲锋衣外套男
冲锋衣女冬季
气垫
凯乐石冲锋衣
鞋子女
烧烤签子
滑雪头盔
汉鼎旗舰官方旗舰店
户外炉具
露营帐篷
户外帐篷
帐篷户外防雨加厚
打火机
滑雪服女款
望远镜高倍高清
柴火灶家用柴火灶
冲锋衣冬季男
始祖鸟兔年限量款
露营椅子
鱼竿手竿
睡袋
蝴蝶折叠刀
优衣库
一次性被罩床单枕套
始祖鸟官方官网旗舰店
鱼线主线 正品
外套冬装男
烧烤架家用
鱼竿手杆超轻 超硬
天文望远镜 高清
冲锋衣男 三合一
北面2022新款羽绒服
天幕帐篷
thenorthface官方旗舰店
进山神器
滑雪手套
棉衣
黑狗天火灯
始祖鸟官方旗舰店官网
北面官网旗舰店
冲锋衣男款
车顶帐篷
始祖鸟殊不知
男士冬款外套
哥伦比亚 冲锋衣
棉服男
背面官网北面女羽绒
路亚竿全套
帐篷户外便携式折叠
鹅绒羽绒服女
北面冲锋服
骆驼
炮台支架
始祖鸟滑雪服
袜子男
外套
儿童滑雪服
冲锋衣外套女
剃须刀
露营推车
探路者冲锋衣
马桶垫子"""
words = words.split('\n')
print(words)
driver = webdriver.Chrome()
driver.maximize_window()
idx = 0
max_idx = len(words)
while idx < max_idx:
    i = words[idx]
    print(i)
    driver.get(f'https://trendinsight.oceanengine.com/arithmetic-index/analysis?keyword={i}&tab=heat_index&appName=aweme')
    t = 0
    while True:
        t += 1
        try:
            el = driver.find_element(by=By.XPATH,
                                     value='//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[1]')
            ActionChains(driver).move_to_element_with_offset(to_element=el, xoffset=50, yoffset=50).perform()
            a1 = driver.find_element(by=By.XPATH,
                                    value='//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/span[1]').text

            el = driver.find_element(by=By.XPATH,
                                     value='//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[1]')
            ActionChains(driver).move_to_element_with_offset(to_element=el, xoffset=0, yoffset=-50).perform()
            a2 = driver.find_element(by=By.XPATH,
                                    value='//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/span[1]').text
            if (not a1) or (not a2):
                idx -= 1
                break
            print('搜索分：', a1)
            print('内容分：',a2)
            break
        except:
            try:
                b = driver.find_element(by=By.XPATH, value='/html/body/div[8]/div/div/div[2]/div[2]/div').text
                if b:
                    print('未收录')
                    break
            except:
                if t > 500:
                    driver = webdriver.Chrome()
                    driver.maximize_window()
                    driver.get(f'https://trendinsight.oceanengine.com/arithmetic-index/analysis?keyword={i}&tab=heat_index&appName=aweme')
                continue
    idx += 1
# //*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[2]/span
#//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/span[2]
#//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[2]/span
#//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[2]/span
#//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[2]/span
#//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[2]/span
#//*[@id="scroll-container"]/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[2]/span

