import pandas as pd
df = pd.read_csv('情感分析结果.csv')
print(df)
df.to_excel('情感分析结果.xlsx')