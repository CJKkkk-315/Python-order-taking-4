import os
from PIL import Image

# 指定你的目标文件夹
directory = "老38-75第2列汇总1193例"
new_directory = 'res_half_images'
# 遍历文件夹中的文件
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        # 打开图片
        img = Image.open(os.path.join(directory, filename))
        # 获取图片的宽度和高度
        width, height = img.size
        # 只保留右边一半
        right_half = img.crop((width/2.03, height/7.5, width, height/1.08))
        # 保存新的图片
        right_half.save(os.path.join(new_directory, "right_half_" + filename))
