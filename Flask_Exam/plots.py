import plotly
import plotly.graph_objects as go
from cleaning_data import data_mobil
import json

def mpg():
    df = data_mobil()
    df_group = df['mpg'].value_counts()
    fig = go.Figure([
        go.Bar(x=df_group.index, y = df_group.values)
        ])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def horsepower():
    df = data_mobil()
    df_group2 = df['horsepower'].value_counts()
    fig = go.Figure([
        go.Bar(x = df_group2.index, y = df_group2.values)
    ])
    fig_json = json.dumps(fig, cls =plotly.utils.PlotlyJSONEncoder)
    return fig_json