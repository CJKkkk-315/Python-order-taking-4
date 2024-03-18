import requests
import json

def search_place(query, region, ak):
    # url = 'https://api.map.baidu.com/place/v2/suggestion'
    url = 'http://api.map.baidu.com/place/v2/search'
    params = {
        'q': query,
        'region': region,
        'output': 'json',
        'ak': ak,
    }
    response = requests.get(url, params=params)
    return response.json()
qq = """1727.云岩区玺樾云璟城市综合体项目
　　1728.南明区首钢贵钢老区开发棚改项目(贵阳金嘉华置业投资公司部分)
　　1729.乌当区北衙尚城安置房项目(C地块)
　　1730.贵阳清镇市铜雀台建设项目
　　1731.清镇市鲤鱼村望城组棚户区改造项目(城市综合体)
　　1732.清镇市前进路矿产公司地块棚户区(旧城)改造建设项目(城市综合体)
　　1733.清镇金地旭辉·枫华建设项目"""
ak = "KjrpW4jkUuRqB9W1i56YcPElNyvgolSn"
for q in qq.split('\n'):
    # print(q)
    query = q.split('.')[1]
    region = "贵州"
    results = search_place(query, region, ak)
    for result in results['results']:
        print(query,result['address'])
        break
