import pandas as pd
bom = pd.read_excel('BOM List.xlsx')
bom = bom[['Material','Material Description','Level','Explosion level','BOM Material','Component','Object description','Material type']]
mo = pd.read_excel('MO List.xlsx',sheet_name='04 MO Demand')
print(mo)
mo = mo[mo['Missing Parts'] == 'YES']
print(mo)
# 使用merge函数合并两个DataFrame
wuse = pd.merge(bom, mo, left_on='Component', right_on='Material', how='left')

# 重命名合并后的列为'Drop Dead Date'
wuse.rename(columns={'Date': 'Drop Dead Date'}, inplace=True)

print(wuse)