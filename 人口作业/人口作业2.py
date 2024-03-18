# 读取文件
def read_csv(file):
    try:
        with open(file, 'r') as f:
            # 按行读取
            content = f.readlines()
            # 去掉换行符等，并且按,分隔成列表
            rows = [row.strip().split(',') for row in content]
            return rows
    except Exception as e:
        return None


# 标准差公式
def standard_error(region_data):
    mean = sum(region_data) / len(region_data)
    squared_diff = [(x - mean) ** 2 for x in region_data]
    variance = sum(squared_diff) / (len(squared_diff) - 1)
    return round((variance ** 0.5) / (len(squared_diff) ** 0.5), 4)


# cos相似度公式
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(y ** 2 for y in b) ** 0.5
    return round(dot_product / (norm_a * norm_b), 4)


# 检测该行是否有效
def is_valid(row):
    try:
        country, population, net_change, land_area, region = row
        # 如果国家或者地区为空，则返回false
        if not country or not region:
            return False
        # 如果人口或面积为负数，返回false
        if int(population) <= 0 or float(land_area) <= 0:
            return False
        return True
    except:
        return False


# 处理数据
def process_data(data):
    # 列名小写
    header = [col.lower() for col in data[0]]
    # 由于可能会有多余的列，先找到我们需要的列索引
    country_index = header.index('country')
    population_index = header.index('population')
    net_change_index = header.index('net change')
    land_area_index = header.index('land area')
    region_index = header.index('regions')

    region_data = {}
    region_summary = {}
    # 逐行处理
    for row in data[1:]:
        # 判断该行是否有效
        if not is_valid([row[country_index], row[population_index], row[net_change_index], row[land_area_index], row[region_index]]):
            continue
        # 数值类型转换和小写转换
        country = row[country_index].strip().lower()
        region = row[region_index].strip().lower()
        population = int(row[population_index])
        net_change = int(row[net_change_index])
        land_area = int(row[land_area_index])

        if region not in region_data:
            region_data[region] = []
            region_summary[region] = {}
        # 如果这个地区已经有该国家，则跳过
        if country in region_summary[region]:
            continue
        # 为对应地区加入人口和面积数据
        region_data[region].append([population, land_area])
        # 初始化对应地区对应国家的数据
        region_summary[region][country] = [population, net_change, 0, round(population / land_area, 4), 0]

    for region, countries in region_summary.items():
        # 计算地区的总人口
        total_population = sum([x[0] for x in countries.values()])
        # 按照国家人口，国家人口密度，国家名排序
        sorted_countries = sorted(countries.items(),
                                  key=lambda x: (-x[1][0], -x[1][3], x[0]))

        for i, (country, values) in enumerate(sorted_countries):
            # 计算人口占比，并赋予相应的排名
            values[2] = round(values[0] / total_population * 100, 4)
            values[4] = i + 1
            region_summary[region][country] = values
    # 调用写好的公式函数计算标准差和cos相似度
    output1 = {region: [standard_error([i[0] for i in region_data[region]]), cosine_similarity([i[0] for i in region_data[region]], [i[1] for i in region_data[region]])] for region in region_data}
    # 返回两个字典
    return output1, region_summary


# 主函数
def main(csvfile):
    data = read_csv(csvfile)
    # 如果读取函数失败，返回两个空字典
    if data is None:
        return {}, {}
    try:
        # 如果处理失败，返回两个空字典
        output1, output2 = process_data(data)
        return output1, output2
    except Exception as e:
        return {}, {}


OP1, OP2 = main('countries.csv')
OP1s= {'asia': [0.8699, 106617709.6196], 'africa': [0.8023, 16530585.7337], 'europe': [0.7383, 12535004.8413], 'latin america & caribbean': [0.9446, 22441416.3173], 'northern america': [0.7841, 80089583.5645], 'oceania': [0.9514, 2553663.855]}
