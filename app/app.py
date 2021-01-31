# Import dash and dash dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

# Other libs
import pandas as pd
import plotly.graph_objects as go
import argparse


# Import helper functions
from src.page_contents import content_1, content_2, content_3
from src.layout import layout
from src.get_data import get_crypto_data
from src.graphs import line

from src.configs import config

external_stylesheets = [
{
    'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    'crossorigin': 'anonymous'
}
]
app = dash.Dash(__name__,
				external_stylesheets=external_stylesheets,
				suppress_callback_exceptions=True,
				)

app.title = "Crypto Dashboard"


app.layout = layout()

# Page Content / Sidebar selector
@app.callback(
    Output("page-content", "children"),
    [
        Input("id_1", "n_clicks_timestamp"),
        Input("id_2", "n_clicks_timestamp"),
        Input("id_3", "n_clicks_timestamp"),
    ]
)
def toggle_collapse(input1, input2, input3):
    btn_df = pd.DataFrame({"input1": [input1], "input2": [input2],
                           "input3": [input3]
						})
    
    btn_df = btn_df.fillna(0)

    if btn_df.idxmax(axis=1).values == "input1":
        return content_1
    if btn_df.idxmax(axis=1).values == "input2":
        return content_2
    if btn_df.idxmax(axis=1).values == "input3":
        return content_3

# store data
@app.callback(
    Output("store-data", "data"),
    [Input("select-crypto", "value")]
)
def store_data(crypto_symbol):

    # make time-param be an input as well, add later
    df = get_crypto_data(crypto_symbol, '1d', save = False)

    return df.to_json()

# datatable
@app.callback(
    Output("crypto-data", "children"),
    [Input("store-data", "data")]
)
def crypto_datatable(data):

    # make time-param be an input as well, add later
    # df = get_crypto_data(crypto_symbol, '1d', save = False)
    df = pd.read_json(data)

    return dash_table.DataTable(
                data=df.to_dict('records'),
                id='table',
                columns=[
                    {'name': i, 
                    'id': i,
                    'selectable' : True,
                    }
                    for i in df.columns
                    ],
                sort_action="native",
                filter_action='native',
                sort_mode='multi',
                page_current = 0,
                page_size = 10,
                style_table={
                    'overflowX': 'scroll',
                    'overflowY': 'scroll',
                    },
                style_as_list_view=True,
                style_header={
                    'backgroundColor': config['bg-primary'],
                    'fontWeight': 'bold'
                    },
                style_cell={
                            'backgroundColor': config['bg-primary'],
                            'padding': '10px',
                            'left-margin' : '8px',
                            'textAlign': 'center',
                            'fontSize':15,
                            'font-family':'sans-serif'
                            }
                )

# line graph
@app.callback(
    Output("line-graph", "figure"),
    [Input("select-col", "value"),
    Input('store-data', 'data')]
)
def line_graph(col, data):

    df = pd.read_json(data)
    fig = line(df, col)

    return fig


if __name__ == '__main__':
	# app.run_server(host='0.0.0.0', debug=True, port=8050)
	app.run_server(debug=True)
