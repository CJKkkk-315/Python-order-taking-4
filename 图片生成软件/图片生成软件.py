import pandas as pd
import matplotlib.pyplot as plt



def add_values_on_bars(ax, rects, space, formatf):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            f'{formatf(height)}',
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, space),  # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom'
        )

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.labelweight'] = 'bold'

file = '模板.xlsx'
data = pd.read_excel(file,skiprows=9)

data = data.dropna(axis=1, how='all')
titles = data.values[:,0]
print(titles)
data = data.drop(data.columns[0], axis=1)
print(data)
x = data.columns
fig, axs = plt.subplots(len(titles), 1, figsize=(15, 9))  # 4行1列的subplot布局，你可以通过figsize调整总图像的大小
# 设定一些颜色和样式
colors = [(176/255,216/255,228/255), (3/255,188/255,253/255), (68/255,130/255,180/255), (114/255,128/255,143/255)]*2


title_font = {
    'fontsize':15,
    'fontweight': 'bold'
}
i = 0
y = data.values[i]
bars = axs[i].bar(x, y, color=colors[i], edgecolor='black')
axs[i].spines['top'].set_visible(False)
axs[i].spines['right'].set_visible(False)
axs[i].set_title(titles[i], fontdict=title_font)
add_values_on_bars(axs[i], bars, 0.3, lambda xx: format(round(xx), ','))

i += 1
y = data.values[i]
bars = axs[i].bar(x, y, color=colors[i], edgecolor='black')
axs[i].spines['top'].set_visible(False)
axs[i].spines['right'].set_visible(False)
axs[i].set_title(titles[i], fontdict=title_font)
add_values_on_bars(axs[i], bars, 0.3, lambda xx: format(round(xx), ','))

i += 1
y = data.values[i]
bars = axs[i].bar(x, y, color=colors[i], edgecolor='black')
axs[i].spines['top'].set_visible(False)
axs[i].spines['right'].set_visible(False)
axs[i].set_title(titles[i], fontdict=title_font)
add_values_on_bars(axs[i], bars, 0.3, lambda xx: round(xx,2))

i += 1
y = data.values[i]
bars = axs[i].bar(x, y, color=colors[i], edgecolor='black')
axs[i].spines['top'].set_visible(False)
axs[i].spines['right'].set_visible(False)
axs[i].set_title(titles[i], fontdict=title_font)
add_values_on_bars(axs[i], bars, 0.3, lambda xx: str(round(xx*100,2)) + '%')
i += 1
if i < len(titles):

    y = data.values[i]
    bars = axs[i].bar(x, y, color=colors[i], edgecolor='black')
    axs[i].spines['top'].set_visible(False)
    axs[i].spines['right'].set_visible(False)
    axs[i].set_title(titles[i], fontdict=title_font)
    add_values_on_bars(axs[i], bars, 0.3, lambda xx: format(round(xx), ','))
i += 1
if i < len(titles):

    y = data.values[i]
    bars = axs[i].bar(x, y, color=colors[i], edgecolor='black')
    axs[i].spines['top'].set_visible(False)
    axs[i].spines['right'].set_visible(False)
    axs[i].set_title(titles[i], fontdict=title_font)
    add_values_on_bars(axs[i], bars, 0.3, lambda xx: str(round(xx*100,2)) + '%')


plt.tight_layout()
plt.savefig('res.png')