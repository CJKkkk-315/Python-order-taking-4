import matplotlib.pyplot as plt
import numpy as np

# 需要的科目
subjects = ['Math', 'English', 'Biology', 'Physics', 'Chemistry']

# 对应的成绩
scores = [88, 92, 80, 90, 85]

# 数据数量
num_vars = len(subjects)

# 计算角度
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 确保雷达图是圆形的
scores += scores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, scores, color='red', alpha=0.25)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(subjects)

# 在雷达图上添加标注
for angle, score in zip(angles, scores):
    ax.annotate(str(score), xy=(angle, score))

ax.set_title('Student Performance')
plt.show()