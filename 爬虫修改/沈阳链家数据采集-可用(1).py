#导入三个需要用到的模块
import requests
import re
import csv
from bs4 import BeautifulSoup
import time

#先写csv的代码,写在循环外面,避免别循环执行多次
with open('房屋-区域.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_write = csv.DictWriter(f, fieldnames=['标题','房屋区域','房屋地址', '房屋户型', '房屋面积', '房屋朝向','装修情况','有无电梯','房屋楼层','预计总价格','每平方价格','建成年份','房屋网址'])
    csv_write.writeheader()  #写入一次csv表头

    for k in range(1,100):#采集10页的数据
        response = requests.get(f'https://sy.lianjia.com/ershoufang/pg{k}/')#requests的get用法,响应体由response接收

        result = response.text #用result接收网站响应体response的文本数据,所有房屋数据都在这里面
        # soup = BeautifulSoup(result)

        website = re.findall('<a class="noresultRecommend img LOGCLICKDATA" href=(.*?) target="_blank" data-log_index=.*? data-el="ershoufang" data-housecode=.*? data-is_focus="" data-sl="">',result, re.S)
        # website表示网址,从请求的网址获取到每个房屋的详细网址
        print(website) #website是列表

        headers = {
            'Host': 'sy.lianjia.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
        }  #以防万一 网站有反爬,加上请求头进行伪装

        for i in website:
            i = i.replace('"','')  #从website中一个一个取出每一个网址i
            details = requests.get(i,headers=headers)  #再一次请求网址,这次是房屋详细页的网址,响应体由details接收
            detail = details.text   #用detail接收响应体details的文本数据,这是一个房屋的详细信息，for循环会进行多次抓取

            title = re.findall('<h1 class="main" title="(.*?)</h1>',detail,re.S)#标题
            quyu = re.findall('<span class="label">所在区域</span><span class="info"><a href=.*? target="_blank">(.*?)</a>',detail,re.S)#区域
            # 从detail中利用正则模块写规则抓取每条信息
            address = re.findall('<a href=.*? target="_blank" class="info ">(.*?)</a>',detail,re.S)#房屋地址
            address = str(address).replace('[','').replace(']','').replace("'",'')    # str是把列表强行转换成字符串,replace是操作字符串的函数

            room = re.findall('<li><span class="label">房屋户型</span>(.*?)</li>',detail,re.S)  # 房屋户型
            room = str(room).replace('[','').replace(']','').replace("'",'')

            area = re.findall('<li><span class="label">建筑面积</span>(.*?)</li>',detail,re.S)  # 房屋面积
            area = str(area).replace('[','').replace(']','').replace("'",'')

            chaoxiang = re.findall('<li><span class="label">房屋朝向</span>(.*?)</li>',detail,re.S)  # 房屋朝向
            chaoxiang = str(chaoxiang).replace('[','').replace(']','').replace("'",'')

            zhuangxiu = re.findall('<li><span class="label">装修情况</span>(.*?)</li>',detail,re.S)  # 装修情况
            zhuangxiu = str(zhuangxiu).replace('[','').replace(']','').replace("'",'')

            elevator = re.findall('<li><span class="label">配备电梯</span>(.*?)</li>', detail, re.S)  # 有无电梯
            elevator = str(elevator).replace('[','').replace(']','').replace("'",'')

            floor = re.findall('<li><span class="label">所在楼层</span>(.*?)</li>',detail,re.S)  # 房屋楼层
            floor = str(floor).replace('[','').replace(']','').replace("'",'')

            yuji_price = re.findall('<div class="price "><span class="total">(.*?)</span>',detail,re.S)  # 预计总价格
            yuji_price = str(yuji_price).replace('[','').replace(']','').replace("'",'') + '万'

            price = re.findall('<span class="unitPriceValue">(.*?)<i>元/平米</i></span>',detail,re.S)  # 每平方价格
            price = str(price).replace('[','').replace(']','').replace("'",'') + '元/平方'

            year = re.findall('<div class="subInfo noHidden">(.*?)</div>',detail,re.S)   # 建成年份
            year = str(year).replace('[','').replace(']','').replace("'",'').split('/')[0]

            print(title,quyu,address,room,area,chaoxiang,zhuangxiu,elevator,floor,yuji_price,price,year)  # 打印一遍数据查看,避免出错

            d = {'标题':title,'房屋区域':quyu,'房屋地址': address, '房屋户型': room, '房屋面积': area, '房屋朝向': chaoxiang,'装修情况':zhuangxiu,'有无电梯':elevator,
                 '房屋楼层':floor,'预计总价格':yuji_price,'每平方价格':price,'建成年份':year,'房屋网址':i}
            csv_write.writerow(d)  # 表头上面已经写入了,现在在每个表头下写入正确的数据
        


