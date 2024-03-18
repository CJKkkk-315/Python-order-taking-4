import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
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

sorted_regions = sorted(code_hash.values())

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='region',
        options=sorted_regions,
        multi=True,
        placeholder='Select ASGS Regions'
    ),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('region', 'value')
)
def dropdown_changed(selected_regions):
    if not selected_regions:
        return {}

    filtered_df = df[df['Region'].isin(selected_regions)]

    fig = px.bar(
        filtered_df,
        x='Region',
        y='Indigenous Student %',
        title='Percentage of Indigenous Students by Region of NSW'
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
