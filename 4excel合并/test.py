import tkinter as tk
from datetime import datetime
import time
def main_fun():
    import pandas as pd
    # 读取BOM表
    bom = pd.read_excel('BOM List.xlsx')
    # 仅保留需要的列
    bom = bom[['Material', 'Material Description', 'Level', 'Explosion level', 'BOM Material', 'Component',
               'Object description', 'Material type']]
    # 读取MO表
    mo = pd.read_excel('MO List.xlsx', sheet_name='04 MO Demand')
    # 筛选Missing parts == Yes
    mo = mo[mo['Missing Parts'] == 'YES']
    # mo去重
    mo = mo.drop_duplicates(subset='Material', keep='first')
    # 读取OBS表
    obs = pd.read_excel('OBS List.xlsx')
    # 匹配XPN，得到wuse
    wuse = pd.merge(bom, obs[['XPN']], left_on='Component', right_on='XPN', how='left')
    wuse = wuse.dropna(subset=['XPN'])
    wuse.drop(['XPN'], axis=1, inplace=True)
    # 使用merge函数合并两个DataFrame
    wuse = pd.merge(wuse, mo[['Material', 'MI Date']], left_on='Component', right_on='Material', how='left')
    # 重命名合并后的列为'Drop Dead Date'
    wuse.rename(columns={'MI Date': 'Drop Dead Date', 'Material_x': 'Material'}, inplace=True)
    wuse.drop(['Material_y'], axis=1, inplace=True)
    # 转换日期格式
    wuse['Drop Dead Date'] = pd.to_datetime(wuse['Drop Dead Date'], errors='coerce')
    wuse['Drop Dead Date'] = wuse['Drop Dead Date'].dt.strftime('%Y-%m')
    # 读取BP表
    bp = pd.read_excel('BP List.xlsx', sheet_name='STO Details Tracking list')
    # 去重
    bp = bp.drop_duplicates(subset='Material', keep='first')
    # 根据T列匹配
    POA0 = pd.merge(wuse, bp[['Material', 'STO Request Date', 'Shipping Amount (STO)']], left_on='Material',
                    right_on='Material', how='left')
    # 得到年月
    POA0['STO Request Year'] = POA0['STO Request Date'].dt.year
    POA0['STO Request Month'] = POA0['STO Request Date'].dt.month
    # 得到数据透视表
    POA = POA0.pivot_table(index='Material', columns=['STO Request Year', 'STO Request Month'],
                           values='Shipping Amount (STO)', aggfunc='sum')
    import datetime
    import numpy as np
    # 获取当前的日期
    current_datetime = datetime.datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    res = []
    # 对之前的月份求和
    for i in POA:
        if i[0] < current_year:
            res.append(POA[i].values)
        elif i[0] == current_year and i[1] < current_month - 1:
            res.append(POA[i].values)
    res = [np.nan_to_num(arr) for arr in res]
    total_sum = np.sum(res, axis=0)
    # 添加到新列中
    POA[(current_year, str(current_month - 1) + '总和')] = total_sum
    print(POA)
    wuse['Drop Dead Date'] = pd.to_datetime(wuse['Drop Dead Date'])
    # 计算与截止月份的REF
    wuse['REF'] = (wuse['Drop Dead Date'].dt.year - current_year) * 12 + (
                wuse['Drop Dead Date'].dt.month - current_month + 1) + 1
    # 确定要添加的列的起始日期
    start_date = pd.to_datetime(f'{current_year}-{current_month - 1}')

    # 计算结束日期（加上14个月）
    end_date = start_date + pd.DateOffset(months=14)

    # 初始化这些列为空
    date_range = pd.date_range(start=start_date, end=end_date, freq='M')
    for date in date_range:
        column_name = date.strftime('%Y-%m')
        wuse[column_name] = ''
    # 根据POA表匹配对应日期对应Material的数值
    for i in range(len(wuse)):
        for c in list(wuse.columns)[10:]:
            try:
                if str(POA[int(c.split('-')[0])][int(c.split('-')[1])][wuse.at[i, 'Material']]) == 'nan':
                    wuse.at[i, c] = 0
                else:
                    wuse.at[i, c] = POA[int(c.split('-')[0])][int(c.split('-')[1])][wuse.at[i, 'Material']]
            except:
                wuse.at[i, c] = 0
    # 其中第一列用汇总覆盖
    for i in range(len(wuse)):
        try:
            wuse.at[i, str(current_year) + '-' + '0' * (2 - len(str(current_month - 1))) + str(current_month - 1)] = \
            POA[(current_year, str(current_month - 1) + '总和')][wuse.at[i, 'Material']]
        except:
            wuse.at[i, str(current_year) + '-' + '0' * (2 - len(str(current_month - 1))) + str(current_month - 1)] = 0
    # 根据不同Material，不同Component计算Summary sheet
    m_max = {}
    m_d = {}
    for i, j in wuse.iterrows():
        if j['Material'] not in m_max:
            m_d[j['Material']] = j['Material Description']
            m_max[j['Material']] = [0 for _ in range(14)]
        for idx in range(14):
            m_max[j['Material']][idx] = max(m_max[j['Material']][idx], list(j)[-14 + idx])
    m_c = {}
    for i, j in wuse.iterrows():
        if j['Material'] not in m_c:
            m_c[j['Material']] = set()
        if j['Component'] not in m_c[j['Material']]:
            m_c[j['Material']].add(j['Component'])
    summ = []
    for i in m_c:
        flag = 0
        for j in list(m_c[i]):
            if flag == 0:
                summ.append([i, m_d[i], j] + m_max[i])
                flag = 1
            else:
                summ.append(['', '', j] + m_max[i])
        summ.append([i + '汇总', '', ''] + m_max[i])
    head = ['Material', 'Material Description', 'Component'] + list(
        map(lambda x: '最大值项：' + x, list(wuse.columns)[-14:]))
    summd = pd.DataFrame(summ, columns=head)
    wuse['Drop Dead Date'] = wuse['Drop Dead Date'].dt.strftime('%Y-%m')
    summd_all = ['总计', '', '']
    for c in summd.columns[3:]:
        summd_all.append(summd[c].sum())
    POA_all = ['总计']
    for c in POA.columns:
        POA_all.append(POA[c].sum())
    with pd.ExcelWriter('res.xlsx', engine='openpyxl') as writer:
        # 将每一个dataframe写入不同的工作表
        pd.DataFrame([], columns=['' for _ in range(10)] + [i + 1 for i in range(14)]).to_excel(writer,
                                                                                                sheet_name='WUSE',
                                                                                                startrow=0, index=False)
        wuse.to_excel(writer, sheet_name='WUSE', startrow=1, index=False)
        POA.to_excel(writer, sheet_name='PO Amount', index=True)
        pd.DataFrame([POA_all], columns=POA_all).to_excel(writer, sheet_name='PO Amount', startrow=len(POA) + 2,
                                                          index=False, header=False)
        POA0.to_excel(writer, sheet_name='PO Amount0', index=False)
        summd.to_excel(writer, sheet_name='Summary', index=False)
        pd.DataFrame([summd_all], columns=summd_all).to_excel(writer, sheet_name='Summary', startrow=len(summd),
                                                              index=False, header=False)
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time_label.config(text=f"Start time: {current_time}")
    window.update()  # 强制更新界面
    start_time = time.time()
    # 执行你的函数（这里用time.sleep()模拟一个耗时操作）
    main_fun()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(str(elapsed_time))
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_label.config(text=f"End time: {current_time}")
    window.update()  # 强制更新界面

# 创建窗口
window = tk.Tk()
window.title("时间统计程序")
window.geometry("600x200")
# 创建按钮
button = tk.Button(window, text="Start", width=10, command=get_current_time)
button.place(x=90,y=150)

button = tk.Button(window, text="End", width=10, command=lambda :exit(0))
button.place(x=400,y=150)

# 创建标签用于显示时间和执行结果
current_time_label = tk.Label(window, text="Start time:")
current_time_label.place(x=50,y=50)

result_label = tk.Label(window, text="End time:")
result_label.place(x=360,y=50)

window.mainloop()
