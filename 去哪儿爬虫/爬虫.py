import requests
from bs4 import BeautifulSoup
import time
for page in range(20):
    try:
        time.sleep(3)
        url = "https://piao.qunar.com/ticket/list.htm?keyword=%E5%8C%97%E4%BA%AC&region=null&from=mps_search_suggest&page=" + str(page)
        headers = {
          'cookie': 'SECKEY_ABVK=W+l+0qPNS1MCwgpJu05sFDC3LgmsLVX0esoXvaYs2Xg%3D; BMAP_SECKEY=BVXxcO-sWPmQuE8oWdpZZxj4ujimTpVeB2u71YkTvpAsnUbviRjZ1aJxb8tINfGke-ZM4-FcJIFZyMSQ5ggeTdP9qg85gZNIi5Ib--JQprhKCtQqUqUVvfPiu7M5dIxGQ_qHJZW0YTKKAZx_RD7iCS4iLP9be6R8UdHfLCKzRptaF6bEtM0iHaZ7c2N76A8_; QN1=000078002eb4462d79f0f65a; QN300=organic; QN71="MTEyLjQ5LjE5OS4xOTE656aP5beeOjE="; QN205=organic; QN277=organic; _i=DFiEZnwmmzRwWia6tdC1x7Zhevww; _vi=6z2IH_1L20FeXyZR3Bg__JS98VsyPRGVGa5kcBmO9I-qGr6z-pYTby8qRXVOPB5zGKuAqODqu7YLXIm93ZqpRauMv7PU7LBhwPlK4wUkx5tnvaSjJN3xZqyXgVgjGhEVONE782O9hrvHG0JMNHA1c-7JAncqxQVxWKOQrxd3bCg7; QN57=16619379817930.19505481997319007; QN269=FD86BC20290E11EDBAB5FA163EEFDE16; fid=a5d61537-f806-4660-b743-6d13dc522f95; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN267=124297257876f52a3b; csrfToken=i2Q2UGx9vPYij2PSDj9UrkBgte9WC8G1; ariaDefaultTheme=undefined; QN58=1661937981792%7C1661938209333%7C2; QN271=24c3fae9-016a-4a25-9d3a-a98ee1483073; Hm_lvt_15577700f8ecddb1a927813c81166ade=1661937982,1661938210; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1661938210; JSESSIONID=F47595413ED7C7A79433FB73677230F0; __qt=v1%7CVTJGc2RHVmtYMStWcDdpcnRwNVRXbktqTmlPK2kxdVEvUVdOeXJXaXFIZ3huVEtMVnNQQjlmcVpReUFmRFFoRUMvUGFVZFU5VHMwT0ZZbE9kMmh0cXdEQkgyOXVGVEN4T05VTE1nck9XQnBjVjhQN01BdHQ5RWJ6NC9BUURUL1YyTDF0ZDRnOS9sUTJZcGl6RWx5cWJmWnpFaXc5c0REdlBqK0FGRmtPeEZVPQ%3D%3D%7C1661938286122%7CVTJGc2RHVmtYMTgzUmtBUnhFZ1F6ZVd3dVpLbkswZFFETFBGb1d2cmZQRndhSHFIWnJEcmFPTExYWEFoTTM0dUNGMDREeWhZZTNSNVJzNnJTSGp1MWc9PQ%3D%3D%7CVTJGc2RHVmtYMS9SWlhMWm5LZUplWGprMDA4VUtjY0FheTMwMUk2clFnQWh5Zmhac2ZOdzFncEJNeEhRY0U1ODNod2U3YkpkNlhOVHdRNm5mbmljQ1kyUUhZek04eUUzcjFkeUZjNjdUZU1VMVVBUzJFRFU5QTRQaWxkV1dBVlpUSWVLbXlEbTFEQzhzNzFERHZ5UXY0YmdOM1dPZ0haeWJTZGF0VkIxampwSWxqRnZ3T0J1VW5RanNQVFZhWGVxbzZubEZTL1h6Z0RFcldNajhtaVZERTJBOXBuZk1KU2tIUjRjb3ozLzhocmRnL0QyUkJQRC9yL1RveXBYbTJTRDh3UXdoaU5QM0Q2eXZ3NHU5UUM1ZnNHR1B3WmlWU2VieEpzYkVJZUxmdCtVUzF1UnUwcHhZTXF3aVJEd0xFYlJwWFVvZVdtWmZ6V0RqSytrYmo5SVdLOGdMeSs2cURVWVdOVXpYTnVPdEowZWZIR0pDM2FRNjRzL3BlMTNKVWpyU1A1bjIyeWJVVndmTHdYdW10WC8xZVVnYVAybE9LMVlDWitla0lCZG1mekhiTDRTYXNyeTdXVGlBaFpscVloUkVBSkh0MFFUVWExcU1rV1hGdWQ3K1YvOG5pcWJQSU9zMDV4VFJhQ0FWYnM3SmZJOHRMWGRQZTRaZVVHWFdCd3RaRWJpTWZ6UkVCWHRyWjA2TWd1YWdMTWM2WUJ3SXZZMmRxUFdGN2VoNkRKTFRvRE5lZk5veTdXZzFRSmhGSUZvWUIxdDJhOVlDRkw5cE9TQjRod25aSU1CdGpKenJya08xN0lpeXRiR2JELytURU04QmRJZzZEOUxidEpNeWQ0dzBOWVhJaWNIdFZLbEsrV2xEVWdTcFNQQkkraXNEdUxvOGVRUDh4Sm1zMzNSTDJGd0dMZmlCb3BNRzNKMnRsYzVTeFBKZWY1cTZrSWdzT2hZWWtpc0E4SjZyRG5EQkh5ZG9mRmY1RnZYZUVJdnV2bGNGMnczS2pXbjlHV3F3ZjNzVmlDWXNnVmRoSUZ6a0dYemE2b2dPNjZNNW92RzJRZGVveEZOS28zZkFDTlBMYVRhSU8vb0hoQzNZV1QxNHJqMg%3D%3D; JSESSIONID=1682174E42EDF4BFBE52A6F50FDF690E',
        }
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text)
        for item in soup.find(id='search-list').find_all(class_='sight_item'):
            name = item.find(class_='name').text
            price = item.find(class_='sight_item_price').find(name='em').text
            area = item.find(class_='area').find(name='a').text
            hot = item.find(class_='product_star_level').find(name='em')['title'].replace('热度: ','')
            sale = item.find(class_='hot_num').text
            addr = item.find(class_='address').find(name='span').text
            print([name,price,area,hot,sale,addr])
    except:
        break