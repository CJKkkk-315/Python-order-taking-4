import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import threading
import warnings
import numpy as np
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('学生成绩.xlsx')
data = df.values.tolist()
cname = df.columns.tolist()
xx = []
for c in cname:
    if df[c].isnull().sum() / len(df[c]) > 0.2:
        xx.append(c)
xf = [float(i.split('[')[1].split(']')[0]) for i in cname[2:]]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            data[i][j] = 0.1
        if str(data[i][j]) == 'nan':
            data[i][j] = 0
        if '/' in str(data[i][j]):
            data[i][j] = max(list(map(lambda x:float(x.replace('*','')),data[i][j].split('/'))))

def show_credits():
    res = {'学号':[],'姓名':[],'学分':[]}
    for i in data:
        res['学号'].append(i[0])
        res['姓名'].append(i[1])
        res['学分'].append(sum([j if i >= 60 else 0 for i,j in zip(i[2:],xf)]))
    res = pd.DataFrame(res)
    print(res)
    res.to_excel('学分统计.xlsx',index=False)


def show_failed_subjects():
    res = {'学号':[],'姓名':[],'不及格门数':[]}
    for i in data:
        res['学号'].append(i[0])
        res['姓名'].append(i[1])
        res['不及格门数'].append(len([i for i in i[2:] if i != 0 and i < 60]))
    res = pd.DataFrame(res)
    print(res)
    res.to_excel('不及格门数统计.xlsx', index=False)

def show_required_courses():
    res = {'学号': [], '姓名': [], '必修课平均分': []}
    for i in data:
        row = []
        res['学号'].append(i[0])
        res['姓名'].append(i[1])
        for km,s in zip(cname,i[2:]):
            if km not in xx and s != 0:
                row.append(s)
        print(row)
        score = sum(row)/len(row)
        res['必修课平均分'].append(score)
    res = pd.DataFrame(res)
    print(res)

    values = ['优秀', '良好', '中等', '及格', '不及格']
    res['必修课表现'] = pd.cut(res['必修课平均分'], bins=[0, 60, 70, 80, 90, 100], labels=values, right=False)
    grade_counts = res['必修课表现'].value_counts()
    plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
    plt.title('学生成绩分类')
    plt.show()
def show_course_distribution():
    thread = threading.Thread(target=_show_course)
    thread.start()

def _show_course():
    kcm = input('请输入课程名称：')
    idx = cname.index(kcm)

    res = {'得分': []}
    for i in data:
        res['得分'].append(i[2:][idx])
    res = pd.DataFrame(res)
    print(res['得分'].mean())
    print(res['得分'].std())
    values = ['优秀', '良好', '中等', '及格', '不及格']
    res['得分表现'] = pd.cut(res['得分'], bins=[0, 60, 70, 80, 90, 100], labels=values, right=False)
    grade_counts = res['得分表现'].value_counts()
    plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
    plt.title('学生成绩分类')
    plt.show()
def show_student_info():
    thread = threading.Thread(target=_show_student)
    thread.start()

def _show_student():
    sid = input('请输入学生学号：')
    bxs = []
    xxs = []
    for i in data:
        if str(i[0]) == sid:
            for c,score in zip(cname[2:],i[2:]):
                if score:
                    if c in xx:
                        xxs.append([c,str(score)])
                    else:
                        bxs.append([c,str(score)])
            print(i[1])
            print(*[':'.join(i) for i in xxs])
            print(*[':'.join(i) for i in bxs])

            subjects = [i[0] for i in bxs]
            scores = [float(i[1]) for i in bxs]
            num_vars = len(subjects)

            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

            scores += scores[:1]
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.fill(angles, scores, color='red', alpha=0.25)
            ax.set_yticklabels([])
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(subjects)

            for angle, score in zip(angles, scores):
                ax.annotate(str(score), xy=(angle, score))

            ax.set_title('Student Performance')
            plt.show()

            subjects = [i[0] for i in xxs]
            scores = [float(i[1]) for i in xxs]
            num_vars = len(subjects)

            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

            scores += scores[:1]
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.fill(angles, scores, color='red', alpha=0.25)
            ax.set_yticklabels([])
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(subjects)

            for angle, score in zip(angles, scores):
                ax.annotate(str(score), xy=(angle, score))

            ax.set_title('Student Performance')
            plt.show()

            break


root = tk.Tk()

# Create buttons and assign commands to them
button1 = tk.Button(root, text="学分统计", command=show_credits)
button2 = tk.Button(root, text="不及格科目统计", command=show_failed_subjects)
button3 = tk.Button(root, text="必修课平均分统计", command=show_required_courses)
button4 = tk.Button(root, text="课程成绩分布统计", command=show_course_distribution)
button5 = tk.Button(root, text="学生个人信息显示", command=show_student_info)

# Grid layout
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)
button5.grid(row=2, column=0)

root.mainloop()
