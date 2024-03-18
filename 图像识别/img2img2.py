from PIL import Image
import os
for file in os.listdir('新1-11第2列189例'):
    # 打开你的图片
    img = Image.open('新1-11第2列189例/' + file)

    # 获取图片的宽度和高度
    width, height = img.size

    # 裁剪左边1/2的部分并等分为4部分
    left_half = img.crop((0, 0, width//2.8, height/1.03))
    parts = left_half.crop((0, 6*height//10, width//2.8, 7.1*height//10))

    # 将剩下的部分向左移动
    remainder = img.crop((width//2.8, 0, width, height/1.03))

    # 创建一个新的空白图片，宽度为原图片宽度，高度为原图片高度
    new_img = Image.new('RGB', (width, height))

    # 将剩余部分粘贴到新图片的左边
    new_img.paste(remainder, (0, 0))

    # 将左半部分的第三部分粘贴到新图片的右边上方
    new_img.paste(parts, (0, 0))

    # 保存新的图片
    new_img.save('res_mix_images2/' + file)
