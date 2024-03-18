import requests
import json
import pandas as pd
import os
def search(ghid, phone):
    url = f"https://e.ikcrm.com/api/pc/customer_commons?common_id={ghid}&maxLimit=false&hasNextPage=false&total=1&search_key={phone}&custom_field_name=address.tel&page=1&per_page=200"

    payload = {}
    headers = {
        'authority': 'e.ikcrm.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Token token="cbcb3ea779a540c6d5be737fa67072be",device="web"',
        'cookie': 'aliyungf_tc=ee59086f34f9a34087a10e4fd5864f6608fe12e090a57b803b1f3eefd588f099; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=K1VBdXh1TEpNaWZHK1ZlRXZRMmM3eW1KVUM4cXJzZUNJV2dLSkhodkEzN2JSRC9udzNlM2VveU8zemxYS3lBQXdld3FtdWt0TmMwRUxNSmtOQU1XNGpJNzM2aVR1TFR6dnlSdFRFdmF6Z0pFdkRJUzlhRHdudzgvcGZvK2lkVmlwMmx4bGY5Y3lERU5IS2FlRkNDWmtWOHRPTjhtVmJZTGIrdUtuUjZUY0Q1THNCZkxwaGRRRGJKQkZVZy9Xa3hPeUxVeXRRY2dndjE0TzNNTDhyVWJ4elljbWkzc0tYd2FsSTF0anNEMm9LNDVicnp1WEdtOWQ0UGFuczZuTWR2VEEvVGdJREpUWHdKTWJIbE1BWWVaTk42QlFkUlE0NGFHb1J6cXdUU2lhdzdsNDdGRWhnelBEVVZWVmk2TjlUVVVFTDN1SCtMb3BZSTdHN0tvY25QVm04bzdNSXBQTHNkSDJuZGVKOUM1NUllemFibFVjWjN3bUY5dE54SzdmVTd0SnRBZE8zMGZCb2RVSTc0SHhKWkg3b0wvSklVU2YrYWxBRWhvNjZBWTFiQT0tLTd4dFVIVno3ODVTTzZkVml2UGdWaGc9PQ%3D%3D--f26a285ee24af4545975f719efdb57bdf0b00cd4',
        'referer': 'https://e.ikcrm.com/pioneers',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-lx-gid': 'wwjiVhsWsQ2R4M9JwNlA',
        'x-tingyun': 'c=B|XKUyACVWCWU;x=ba463b4365ac47fb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res_data = json.loads(response.text)
    return res_data['data']['list']

def change_comment(ghid, sid, comment):

    url = f"https://e.ikcrm.com/api/pc/customer_commons/{sid}"

    payload = json.dumps({
        "customer": {
            "note": comment
        },
        "common_id": ghid
    })
    headers = {
        'authority': 'e.ikcrm.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Token token="cbcb3ea779a540c6d5be737fa67072be",device="web"',
        'content-type': 'application/json',
        'cookie': 'aliyungf_tc=ee59086f34f9a34087a10e4fd5864f6608fe12e090a57b803b1f3eefd588f099; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=OEg0K2w4VUMyNWZlWVVwN3ArcUxtRGtJckdIWm1PTG94MnVwYTJvY3dOYmxnWkZaeEx1dU5iVGlEK2NvajQwQ2M3RDRoVDlnYUhwNUZ0dXRFVUVsWHhOT0FBd29pNlQ3L3ZING1aanJoYkFxNVFYT3l3SThYR1FwYzF4cThrM2VUV0FzMG1oY2RzNWNYaFhyWnMvOUNUbkllVVIzK3IyRnlWSjlzL3hMY0gwWkFoQXVKQTFLZFhIekZPSDMxbUM0RVV2OXhzMzBuVUdSd2hjSjFEdlV6YWE3WnRJd3JqaUh6OHlkZklSK24yak5FR2J2SUVDMlZpeWNOZXBIa0hZZk9pYWJVUmVvcWNGSU4yUTVJYWFaa3RXbGZDTkU2NnJJUlg4cnQyaUlsNTNRYWc0TlRyOGduTWZrK0pYc2R4WmthOVFQbUxaTDZKKzdzcmJmUFdPcXh2NE51SHZBRG1vYllGQllVRVZMOVhNWVl1bzJzNU1VdXpvMHVERW5OM3hpYStZTGZ1bzlYdFpRWGlGdldyS2F5ZVE4TUU2QlZzNkVPcVQ4T05UQWhGWT0tLWRwZStiSkZETWlkNTJSRkZRejZRWUE9PQ%3D%3D--c9ffb16f7640efdec2d5be4cfecd5477ef677797',
        'origin': 'https://e.ikcrm.com',
        'referer': 'https://e.ikcrm.com/pioneers',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-lx-gid': 'wwjiVhsWsQ2R4M9JwNlA',
        'x-tingyun': 'c=B|XKUyACVWCWU;x=41059c401a914e91'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return json.loads(response.text)['result']

def move(ghid, sid):
    url = f"https://e.ikcrm.com/api/customer_commons/mass_transfer?common_id={ghid}"

    payload = f"authenticity_token=vgWcj9bC45wh%2B%2FU5bYnmN6PIh8Jw4945YbHO6WhP9CqpG3rQWcVuyuWZAGzKxrQ6ufn8ffx40aUDN%2FFvBtZ2UQ%3D%3D&user_id=12014356&transfer_contracts=false&transfer_opportunities=false&nowin_opportunities=false&customer_ids%5B%5D={sid}"
    headers = {
        'authority': 'e.ikcrm.com',
        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'aliyungf_tc=ee59086f34f9a34087a10e4fd5864f6608fe12e090a57b803b1f3eefd588f099; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=WmJYNjAyeEpSTmkreGJXc3dOQW9aYi92UmtmbDFNVFRoWDc4dUI3T2lDWmkrR24veGpyWXJqZDNMTUpONk5CM2s5a3dXbDFNbThhcmZvaFRuMW5Rb0tnS2J0UDFLbExnRCszVm9ZTk8rUThsT3lucTk2ZnlFbGF1RHNBR0ZMbkRjcm5XSTJtajRkbSsyK1VDcllmMVpEeFdNeVpsM1l1TGpPMHBDNnpJM0hFamNqOVRySDhqTWtEU2NUazJYVllZam9iaXZmVjMvNTBNVk5iZGRZbHA1ZVI5K1dYcXJLdjYwcS9mNlordUt2RkJYQ1NoOWdPd1RvbTRCYWQvVWI4cXlyVTAzRTJqOStSQm5UdnNIejJ3eFJNVUUzeExhaUJ3V0dvOWlQWU5XZGZ1YlNRZGdZWnNOYjJzVVpBMDVYeGVSOUQrQU9ENEViYnAvWDI3bGRwOGJJNFE3eGc3d2hZblMyRUZpeUIwOUZiVHNrU3dnbit3Mi84QkRmY1BKci9MSWN5UkgrUUJjYklxTkYwSmNaUnJEVWZQdGpscStmTStjaWVPa2lDRGswVT0tLXdjbmdkdlpURi9HTVF4VFBDMlQ2S1E9PQ%3D%3D--e7c37edfd0a51d033ecdbc42b2a5022475b4b6d2',
        'origin': 'https://e.ikcrm.com',
        'referer': 'https://e.ikcrm.com/pioneers',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-csrf-token': 'vgWcj9bC45wh+/U5bYnmN6PIh8Jw4945YbHO6WhP9CqpG3rQWcVuyuWZAGzKxrQ6ufn8ffx40aUDN/FvBtZ2UQ==',
        'x-requested-with': 'XMLHttpRequest',
        'x-tingyun': 'c=B|XKUyACVWCWU;x=bf336db863f44edc'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text

def search_all(phone):
    url = "https://e.ikcrm.com/api/pc/v1/customers/pc_index"

    payload = json.dumps({
        "current": 1,
        "pageSize": 10,
        "total": 1,
        "custom_field_name": "address.tel",
        "search_key": phone,
        "page": 1,
        "maxLimit": False,
        "hasNextPage": False,
        "per_page": 10
    })
    headers = {
        'authority': 'e.ikcrm.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Token token="cbcb3ea779a540c6d5be737fa67072be",device="web"',
        'content-type': 'application/json',
        'cookie': 'aliyungf_tc=ee59086f34f9a34087a10e4fd5864f6608fe12e090a57b803b1f3eefd588f099; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=TEtleHlFcUpIRFJwL1RSVTg3cHJZeS9mZVdKNWJyNWdCWXZybEQ4MnNJOWlOWm5RUVNJVktmaCtmemNPWE95aFA4Qld2SXhRMS9WV1paQ3FsSG9VL284bkY0OW1DL21vQnhlWHZ4UlJiQlFkNWVodERWcEwxMjU2SHFrTUhCWkVtRVViNW90NjltVkI4NFlKd2wyckx3Ri9hTU90NTJKM0JGaFJSUEJRRTdPd0xYWXhDUGFZM3FPbUlNWUJKRnBnNGk4Um1pK1o2enBWTUVlYlZrSi9zOEJLV2V2NDVFUjh3SUdNUjNmNy9WQVVxcU8vN09xcDA2a0gxbjV2UGhSZ2l2YUxick5tNndBaE0yZURuMFRlOTRHZm10L1J5Y0hMblBNbk9GclgyY3ZNeHl1akhJR2paUkFDVVByd2NrQi9teUx5RWpFeUxzb0JBdTZEQW80bGREYWRXZW9kblRrcU9aSWFDdVNFa0tGU083L1RTTzFFaFRqUkwrbXVFdkJsMHdkU3ZCU0NpM3FiVG14ZEh4L1Ztc0VMQWpCRzFsVnlVanpEQjg5akJSQT0tLUdmM2dtMHJuUko4dUdGMkZTd3RjV0E9PQ%3D%3D--46f6e683304af94f57525888c65e3b6d5010f7b6',
        'origin': 'https://e.ikcrm.com',
        'referer': 'https://e.ikcrm.com/pioneers',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-lx-gid': 'wwjiVhsWsQ2R4M9JwNlA',
        'x-tingyun': 'c=B|XKUyACVWCWU;x=766ccaa958ff4cff'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res_data = json.loads(response.text)
    return res_data['data']['list']

def change_comment_all(sid, comment):

    url = f"https://e.ikcrm.com/api/pc/customers/{sid}"

    payload = json.dumps({
        "customer": {
            "note": comment
        }
    })
    headers = {
        'authority': 'e.ikcrm.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Token token="cbcb3ea779a540c6d5be737fa67072be",device="web"',
        'content-type': 'application/json',
        'cookie': 'aliyungf_tc=ee59086f34f9a34087a10e4fd5864f6608fe12e090a57b803b1f3eefd588f099; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=VlZ6WVRzMTdiWityb0l5OUllV21LYzdES3VQSEhkRkI2OGo5VThNbWlwMXNjVHRpOVE2VmlaREh0WmpTNUhQaTl3MERoYzhFWGtEcnRSem15d2w5S3JLTkc0a1VaU3lBbFNSYjNHVVZ4Z3VFMzRVUnAyS05kUXVKaXNjSUpjNWhFelAzaFUvelFKSVZpNjRINWo0TGFYR1N2czhSVE9zNnlYcytWUTN5OXk1SjUzWUREVWFQOURyQjdpUy93L1pZVU1yb0Q5Ukxwd2xjMEw5TUl3bndaYUJnaTNKbE8zQWpUN1pnS3AraTdTYTl0Y0RhVWs1Skg0YVBJRWRGdUhrOVhLa0JvWjlBUFVGYWZrOWxuZmRCSTZ2aWJ0QmxYZE0yb1lReEFXZ241RGtIYjNmN2RTUU1VanJ6Mm0wcUErK3JiTjBadmRONmFQcHc5WEl5S2xtTndxbS94V0hpMVpJaDBWcnNIMXdWMEcvYUxQWHNpSllwdllDbG9GUlFZVFJ0TE44UWdwQVhxVUovb3EwcEF4ZGRyd3pKc2V6bjEwa0NHRUU3N3hTK3pSZz0tLXNxWjNQVHVSb0l0RmtFWGp4RHRzamc9PQ%3D%3D--1cbdb07be9738e3493c05d50ead4aa30de42823d',
        'origin': 'https://e.ikcrm.com',
        'referer': 'https://e.ikcrm.com/pioneers',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-lx-gid': 'wwjiVhsWsQ2R4M9JwNlA',
        'x-tingyun': 'c=B|XKUyACVWCWU;x=26071f12c6f44842'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return json.loads(response.text)['message']

try:
    file = [i for i in os.listdir() if i[-4:] == 'xlsx'][0]
    data = pd.read_excel(file)
    print(data)
    data['备注'] = data['备注'].fillna('空白')
    phonea = data['常用手机'].values.tolist()
    phone = []
    for pp in phonea:
        try:
            phone.append(str(int(pp)))
        except:
            continue
    comment = data['备注'].values.tolist()
    phone = [str(i).strip() for i in phone]
    # data = [['18868692085','test']]
    data = [[i,j] for i,j in zip(phone, comment)]
    ghname = [['公海','189081'], ['洛阳','214917'], ['废池子','189136']]
    for row in data:
        flag = 1
        print('-'*30)
        print(f'正在搜索{row[0]}')
        for gh in ghname:
            print(f'正在搜索{gh[0]}')
            res_data = search(gh[1], row[0])
            if len(res_data):
                flag = 0
                print(f'{gh[0]}已找到')
                sid = res_data[0]['id']
                print('修改备注:', change_comment(gh[1], sid, row[1]))
                content = move(gh[1],sid)
                print(content)
                print('转移成功！')
                break
            else:
                print(f'{gh[0]}未找到')

        if flag:
            res_data = search_all(row[0])
            if len(res_data):
                print('客户已找到')
                sid = res_data[0]['id']
                print('修改备注:', change_comment_all(sid, row[1]))
except Exception as e:
    with open('error_log.txt', 'a') as file:
        file.write(str(e) + '\n')
