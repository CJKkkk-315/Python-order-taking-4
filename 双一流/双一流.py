import csv  # 导入Python的csv模块，用于处理csv文件

# 读取双一流高校信息，并返回两个字典：一个是学校到省区的映射，另一个是省区到双一流高校数量的映射
def load_shuangyiliu(filename):
    schools = {}  # 建立一个空字典，用于存储学校名称及其对应的省区
    provinces = {}  # 建立一个空字典，用于存储省区及其对应的学校数量
    with open(filename, 'r', encoding='utf-8') as file:  # 以只读模式打开文件
        reader = csv.reader(file, delimiter=' ')  # 创建一个csv.reader对象，用于读取文件内容
        for row in reader:  # 遍历文件中的每一行
            school, province = row  # 获取每一行的学校名称和省区名称
            schools[school] = province  # 在学校字典中添加学校名称及其对应的省区
            if province not in provinces:  # 如果这个省区在省区字典中不存在
                provinces[province] = 0  # 则在省区字典中添加这个省区，并初始化学校数量为0
            provinces[province] += 1  # 然后将这个省区的学校数量加1
    return schools, provinces  # 返回学校字典和省区字典

schools, provinces = load_shuangyiliu('ShuangYiLiu.txt')  # 加载双一流高校的信息

# 根据查询字符串，自动判断是省区还是学校，并进行相应的查询
def query(schools, provinces, query_str):
    # 首先检查输入是否是学校名称
    if query_str in schools:  # 如果输入的是学校名称
        print(f"{query_str}所在的省区是：{schools[query_str]}")  # 查询并打印学校所在的省区
    # 然后检查输入是否是省区名称
    elif query_str in provinces:  # 如果输入的是省区名称
        print(f"{query_str}的双一流高校数量是：{provinces[query_str]}")  # 查询并打印省区的双一流高校数量
    # 如果既不是学校名称也不是省区名称，打印“无”
    else:
        print("无")

# 示例查询
query_str = input("请输入省区或学校名称：")  # 获取用户输入的查询字符串
query(schools, provinces, query_str)  # 使用查询字符串进行查询
