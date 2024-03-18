def main(csvfile, region):
    try:
        # 定义需要筛选的区域
        need_region = region
        # 索引存储在变量中，更加直观
        name, pop, yearly, net, area, region = 0, 1, 2, 3, 4, 5
        # 从文件中读取数据
        data = []
        with open(csvfile) as f:
            lines = f.read().split('\n')
            del lines[0]
            for line in lines:
                # 去除空行
                if line:
                    row = line.split(',')
                    # 对类型进行一定转换
                    data.append([row[name].replace('"',''), int(row[pop]), float(row[yearly]), int(row[net]),
                                 float(row[area]), row[region].replace('"','')])
        # 筛选制定区域的数据
        region_data = []
        for row in data:
            if row[region] == need_region:
                region_data.append(row)
        # 筛选正数
        pos_data = []
        for row in region_data:
            if row[net] > 0:
                pos_data.append(row)
        if not pos_data:
            max_min = []
        else:
            # 排序，并获得最大值和最小值
            pos_data.sort(key=lambda x: x[pop], reverse=True)
            max_min = [pos_data[0][name], pos_data[-1][name]]
        # 如果没有该区域数据，返回默认空值
        if len(region_data) == 0:
            return [], [], [], 0
        else:
            # 计算平均人口和平均面积，以及标准差
            average_pop = sum([i[pop] for i in region_data]) / len(region_data)
            average_area = sum([i[area] for i in region_data]) / len(region_data)
            std = (sum([(i[pop]-average_pop)**2 for i in region_data])/(len(region_data)-1))**0.5

            # 获取每个国家的密度
            density = []
            for row in region_data:
                each_density = round(row[pop] / row[area], 4)
                density.append([row[name], each_density])
            # 密度排序
            density.sort(key=lambda x: x[1], reverse=True)
            # 计算相关性系数
            corr_up = sum([(i[pop] - average_pop) * (i[area] - average_area) for i in region_data])
            corr_down = sum([(i[pop] - average_pop)**2 for i in region_data]) * sum([(i[area] - average_area)**2 for i in region_data])
            corr_down = corr_down ** 0.5
            corr = corr_up/corr_down
            # round 4位处理
            average_pop = round(average_pop, 4)
            std = round(std, 4)
            corr = round(corr, 4)
            # 返回结果
            stdvAverage = [average_pop, std]
            return max_min, stdvAverage, density, corr
    # 若程序有任何异常，返回默认空值
    except:
        return [], [], [], 0

MaxMin, stdvAverage, density, corr = main('countries.csv', 'Asia')
print(MaxMin)
print(stdvAverage)
print(density)
print(corr)
