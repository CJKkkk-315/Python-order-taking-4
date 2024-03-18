import pandas as pd
import plotly.express as px
schools = pd.read_csv('master_dataset.csv')
schools['Indigenous_pct'] = pd.to_numeric(schools['Indigenous_pct'], errors='coerce')
grouped = schools.groupby('ASGS_remoteness')
group_sizes = grouped.size()
group_percentages = schools.groupby('ASGS_remoteness')['Indigenous_pct'].mean()
code_hash = {'IR':'Inner Regional Australia','MC':'Major Cities of Australia','OR':'Outer Regional Australia','R':'Remote Australia','VR':'Very Remote Australia'}
code_name = list(pd.DataFrame(group_percentages).index)
value_list = list(group_percentages)
df = pd.DataFrame({'Region':code_name,'Indigenous Student %':value_list})
print('Valid region codes: MC, IR, OR, R, VR')
need = []
input_code = []
while True:
    user_input = input('Region:')
    if user_input == '':
        break
    if user_input not in code_hash:
        print('Invalid region code. Please try again.')
    else:
        need.append(code_hash[user_input])
        input_code.append(user_input)
if len(need) < 2:
    print('ERROR: Two or more region codes must be entered.')
else:
    print('Producing graph for regions:' + ','.join(input_code) + '...')
    print('Done!')
    filtered_df = df[df['Region'].isin(need)]
    fig = px.bar(
        filtered_df,
        x='Region',
        y='Indigenous Student %',
        title='Percentage of Indigenous Students by Region of NSW'
    )
    fig.show()

