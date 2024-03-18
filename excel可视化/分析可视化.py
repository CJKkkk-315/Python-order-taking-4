import pandas as pd
from pyecharts.charts import Pie, Bar, Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 加载数据
df = pd.read_csv('movie.csv')

# 主题设置
theme = ThemeType.LIGHT

# 分析: 总体电影分类情况＋中国大陆电影分类情况
all_movie_type = df['类型'].value_counts()
china_movie_type = df[df['地区'] == '中国大陆']['类型'].value_counts()

# 可视化: 总体电影分类情况饼图
pie1 = Pie(init_opts=opts.InitOpts(theme=theme))
pie1.add(
    "",
    [list(z) for z in zip(all_movie_type.index.tolist(), all_movie_type.values.tolist())],
    radius=["40%", "65%"],  # 调整饼图大小
)
pie1.set_global_opts(
    title_opts=opts.TitleOpts(title="总体电影分类情况", pos_top="5%", pos_left="5%"),  # 调整标题位置
    legend_opts=opts.LegendOpts(pos_top="15%"),  # 调整图例位置
)
pie1.set_series_opts(
    label_opts=opts.LabelOpts(position="outside"),  # 标签在饼图外部
    center=["50%", "65%"],  # 调整饼图位置
)
pie1.render("总体电影分类情况.html")

# 可视化: 中国大陆电影分类情况饼图
pie2 = Pie(init_opts=opts.InitOpts(theme=theme))
pie2.add(
    "",
    [list(z) for z in zip(china_movie_type.index.tolist(), china_movie_type.values.tolist())],
    radius=["40%", "65%"],  # 调整饼图大小
)
pie2.set_global_opts(
    title_opts=opts.TitleOpts(title="中国大陆电影分类情况", pos_top="5%", pos_left="5%"),  # 调整标题位置
    legend_opts=opts.LegendOpts(pos_top="15%"),  # 调整图例位置
)
pie2.set_series_opts(
    label_opts=opts.LabelOpts(position="outside"),  # 标签在饼图外部
    center=["50%", "65%"],  # 调整饼图位置
)
pie2.render("中国大陆电影分类情况.html")




# 分析：电影类型与评分的关系+电影特色与评分的关系
type_score_avg = df.groupby('类型')['评分'].mean().round(2).reset_index()
feature_score_avg = df.groupby('特色')['评分'].mean().round(2).reset_index()

# 可视化：折线图
line1 = Line(init_opts=opts.InitOpts(theme=theme))
line1.add_xaxis(type_score_avg['类型'].tolist())
line1.add_yaxis("类型平均评分", type_score_avg['评分'].tolist())
line1.set_global_opts(title_opts=opts.TitleOpts(title="电影类型与平均评分的关系"))
line1.render("电影类型与平均评分的关系.html")

line2 = Line(init_opts=opts.InitOpts(theme=theme))
line2.add_xaxis(feature_score_avg['特色'].tolist())
line2.add_yaxis("特色平均评分", feature_score_avg['评分'].tolist())
line2.set_global_opts(title_opts=opts.TitleOpts(title="电影特色与平均评分的关系"))
line2.render("电影特色与平均评分的关系.html")

df.drop_duplicates(subset='电影名', keep='first', inplace=True)
df['导演'] = df['导演'].apply(lambda x:x.split('|')[0])
# 标记电影质量
df['电影级别'] = pd.cut(df['评分'], bins=[0, 6, 8.5, 10], labels=['烂片', '一般片', '好片'])

# 找出好片数量最多的前10个导演
top_directors = df[df['电影级别'] == '好片']['导演'].value_counts().nlargest(10)

# 只考虑这10个导演的电影
df_top_directors = df[df['导演'].isin(top_directors.index)]

# 统计他们的电影级别分布
grouped = df_top_directors.groupby('导演')['电影级别'].value_counts().unstack().fillna(0)

# 按照好片数量排序
grouped = grouped.loc[top_directors.index]

# 可视化3: 柱状图
bar = Bar(init_opts=opts.InitOpts(theme=theme))
bar.add_xaxis(grouped.index.tolist())
bar.add_yaxis("烂片", grouped['烂片'].tolist(), stack="stack1", label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis("一般片", grouped['一般片'].tolist(), stack="stack1", label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis("好片", grouped['好片'].tolist(), stack="stack1", label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="好片最多的前10名导演电影级别分布"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30, interval=0, font_size=8))  # 设置字体大小为10
)
bar.render("前10名导演电影级别分布.html")

