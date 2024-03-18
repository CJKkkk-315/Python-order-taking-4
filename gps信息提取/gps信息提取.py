from PIL import Image
import exifread

# 打开图片文件
with open('gps工具箱/3号附近_coor_32.852436_101.359760_3634.188320_60ED0EE9-7A2E-40BE-A05D-2027B76E100A_20230912113821_0.jpg', 'rb') as image_file:
    image = Image.open(image_file)

    # 读取EXIF数据
    exif_data = image._getexif()

    if exif_data:
        # 获取经纬度信息
        gps_info = exif_data.get(34853)  # GPS信息的标签ID是34853

        if gps_info:
            # 解析经纬度信息
            gps_info_dict = exifread.process_file(image_file, details=False)

            # 提取经度和纬度信息
            latitude = gps_info_dict['GPS GPSLatitude']
            longitude = gps_info_dict['GPS GPSLongitude']

            # 转换经度和纬度的格式
            latitude_degrees = latitude.values[0].num / latitude.values[0].den
            latitude_minutes = latitude.values[1].num / latitude.values[1].den
            latitude_seconds = latitude.values[2].num / latitude.values[2].den

            longitude_degrees = longitude.values[0].num / longitude.values[0].den
            longitude_minutes = longitude.values[1].num / longitude.values[1].den
            longitude_seconds = longitude.values[2].num / longitude.values[2].den

            # 打印经纬度信息
            print(f"纬度：{latitude_degrees}° {latitude_minutes}' {latitude_seconds}\"")
            print(f"经度：{longitude_degrees}° {longitude_minutes}' {longitude_seconds}\"")
        else:
            print("没有找到GPS信息")
    else:
        print("没有找到EXIF数据")
