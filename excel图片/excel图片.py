import openpyxl
import requests
from openpyxl.drawing.image import Image
from io import BytesIO
import json
import os






def download_image(tcode):
    url = f"http://web.eastshow.cn/ytx/store/bar_code/{tcode}"
    print(url)
    payload = {}
    headers = {
        'Authorization': 'YTX_STORE;eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiMTEwIiwidW5pcXVlX25hbWUiOiLosK3pnZkiLCJ1c2VySWQiOiIxMDA1MjMiLCJpc3MiOiJyZXN0YXBpdXNlciIsImF1ZCI6IndZRGd2RkV3dUVIWkNySmxsdTFxSWlpRlVWcmcyeXA5IiwiZXhwIjoxNjgzNjg3OTEyLCJuYmYiOjE2ODM1MTUxMTJ9.1CabBYFS3mS4wnxhcMQfYfRQUjR441TS8D0TvaWHcRM'    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    img_url = json.loads(response.text)['data']['fiimage']
    response = requests.get(img_url)
    img_data = response.content
    return img_data

def insert_images_to_excel(input_file, output_file):
    # 读取Excel文件
    wb = openpyxl.load_workbook(input_file)
    ws = wb.active

    # 遍历每一行
    for row in ws.iter_rows(min_row=6):  # 假设从第二行开始处理数据，第一行为表头
        tcode = row[1].value  # 假设URL在第一列，根据实际情况调整
        if tcode == '总计':
            continue

        # 下载图片
        img_data = download_image(tcode)

        # 将图片插入到第七列单元格中
        img = Image(BytesIO(img_data))
        cell = row[7]  # 第七列单元格
        column_width = ws.column_dimensions[cell.column_letter].width
        row_height = ws.row_dimensions[cell.row].height

        # 调整图片大小以填满单元格
        img.width = int(column_width * 6.2)  # 列宽的单位为字符宽度，大约6.2像素/字符
        img.height = int(row_height)  # 行高的单位为像素

        ws.add_image(img, cell.coordinate)

    # 保存结果到新的Excel文件
    wb.save(output_file)

files = os.listdir('testpicture2')
for file in files:
    input_file = 'testpicture2/' + file
    output_file = 'output/' + file

    insert_images_to_excel(input_file, output_file)

