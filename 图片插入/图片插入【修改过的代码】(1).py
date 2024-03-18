import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def insert_images_to_excel(excel_path, folder_path):
    # 使用 pandas 读取 excel 文件
    df = pd.read_excel(excel_path, sheet_name='图文介绍')

    # 加载工作簿
    wb = load_workbook(excel_path)

    # 选择工作表，如果你的工作表名不是'Sheet1'，请改成你的工作表名
    ws = wb['图文介绍']
    print(df)
    # 在指定的文件夹中寻找 jpg 文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(f"Processing file: {file}")  # 打印出正在处理的文件名
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                # 如果找到的 jpg 文件的名字（不含扩展名）在 excel 的第二列中，就将其路径添加到第六列
                file_name = os.path.splitext(file)[0]
                if file_name in df.iloc[:, 0].values:
                    row_index = df.index[df.iloc[:, 0] == file_name][0] + 2  # pandas 从0开始，openpyxl 从1开始，且排除了标题行
                    img = Image(os.path.join(root, file))
                    img.width = 60
                    img.height = 80
                    ws.add_image(img, f'C{row_index}')  # 'D'表示第四列

    # 保存工作簿
    wb.save("new_excel.xlsx")

# 调用函数
insert_images_to_excel('定价体系.xlsx', '图片2')
