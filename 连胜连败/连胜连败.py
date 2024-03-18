import csv
import json
import os
from collections import defaultdict
# 定义战力类型
fight_type = 'fight_score'
# 起始何结束时间
start_time = '2023071212'
end_time = '2023071403'
# 连败连胜人数和人次列表，一共7个分段
final_rs_win = [[0 for _ in range(8)] for _ in range(7)]
final_rc_win = [[0 for _ in range(8)] for _ in range(7)]
final_rs_los = [[0 for _ in range(8)] for _ in range(7)]
final_rc_los = [[0 for _ in range(8)] for _ in range(7)]
# 筛选后的文件列表


def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


# 使用你的目录替换 'your_directory'

def time_select(start_time, end_time):
    files = []
    # 根据时间筛选
    for file in dir_files:
        time = ''.join(file.split('_')[-2:]).split('.')[0]
        if start_time <= time <= end_time:
            files.append(file)
    return files

def group_by_user(files):

    # 定义用户字典
    user_data = defaultdict(list)
    # 处理每个文件
    for file in files:
        rows = open(file).read().split('\n')
        # 去除空值
        rows = [i for i in rows if i]
        # 每个文件的每行
        for row in rows:
            # 读取json数据
            js_data = json.loads(row)
            # 新建一个key，方便对用户分类
            js_data['user_key'] = '-'.join([str(js_data[i]) for i in ['account_id','zid','sid','role_id']])
            # 仅保留对我们有用的值
            row_data = {}
            row_data['start_time'] = js_data['start_time']
            row_data['map_fight_score'] = js_data['map_fight_score']
            row_data['fight_score'] = js_data['fight_score']
            row_data['user_key'] = js_data['user_key']
            row_data['race_result_num'] = js_data['race_result_num']
            row_data['race_result'] = js_data['race_result']
            user_data[row_data['user_key']].append(row_data)
    return user_data

def count_res(user_data):
    # 遍历分类后的每个用户数据
    for key in user_data:
        user_win = []
        user_los = []
        # 根据时间排序
        user_data[key].sort(key=lambda x:x['start_time'])
        # 获得战力，最低为6000
        if fight_type == 'map_fight_score':
            min_score = 6000
        else:
            min_score = 7500
        score = max(user_data[key][-1][fight_type] - min_score,0)
        # 根据战力分段对应索引
        if score == 0:
            fight_idx = 0
        else:
            fight_idx = score//1500 + 1
        # 最高为13500
        fight_idx = min(fight_idx,6)
        # 记录第一场的连胜/连败场数和连胜连败状态
        start_num = user_data[key][0]['race_result_num']
        now_result = user_data[key][0]['race_result']
        for i in range(1,len(user_data[key])):
            # 如果保持相同状态，场数加1
            if user_data[key][i]['race_result'] == now_result:
                start_num += 1
            # 若不同，则中断重新记录，把上一次场数加入到结果列表中
            else:
                if user_data[key][i]['race_result'] == 0:
                    user_win.append(start_num)
                else:
                    user_los.append(start_num)
                start_num = 1
                now_result = user_data[key][i]['race_result']
        # 最后的结果也要记录一次
        if now_result == 0:
            user_los.append(start_num)
        else:
            user_win.append(start_num)
        # 连胜/连败最多记录到7以上
        user_win = [min(i, 8) for i in user_win]
        user_los = [min(i, 8) for i in user_los]
        # 根据战力分段索引，记录到总表中
        for i in user_win:
            final_rc_win[fight_idx][i-1] += 1
        for i in user_los:
            final_rc_los[fight_idx][i-1] += 1
        # 使用set去重，说明开始计算人数和不是人次
        user_win = set(user_win)
        user_los = set(user_los)
        # 和上面一样操作
        for i in user_win:
            final_rs_win[fight_idx][i-1] += 1
        for i in user_los:
            final_rs_los[fight_idx][i-1] += 1
def write_file():
    # 下面都是写入文件而已
    ans = []
    if fight_type == 'map_fight_score':
        fight_list = ['<6000','6500~7499','7500~8999','9000~10499','10500~11999','12000~13499','13500以上']
    else:
        fight_list = ['<7500', '7500~8999', '9000~10499', '10500~11999', '12000~13499', '13500~14999','15000以上']
    header = ['战力分段','7败以上人数'] + [f'{i}败人数' for i in range(7,0,-1)] + [f'{i}胜人数' for i in range(1,8)] + ['7胜以上人数']
    header += ['7败以上人次'] + [f'{i}败人次' for i in range(7,0,-1)] + [f'{i}胜人次' for i in range(1,8)] + ['7胜以上人次']
    print(header)
    for i in range(7):
        row = [fight_list[i]]
        row += final_rs_los[i][::-1] + final_rs_win[i] + final_rc_los[i][::-1] + final_rc_win[i]
        print(row)
        ans.append(row)
    with open('战力.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows([header] + ans)

dir_files = list_files('data')

files = time_select(start_time, end_time)

user_data = group_by_user(files)

count_res(user_data)

write_file()