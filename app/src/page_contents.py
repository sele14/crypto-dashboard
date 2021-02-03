import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

# Other libs
import pandas as pd

from src.configs import config

# the content of each page for sidebar
content_1 = html.Div([
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='select-crypto',
                    options=[
                        {'label': 'Bitcoin', 'value': 'BTCUSDT'},
                        {'label': 'Ethereum', 'value': 'ETCUSDT'},
                        {'label': 'Litecoin', 'value': 'LTCUSDT'},
                        {'label': 'Tether', 'value': 'USDTBIDR'},
                        {'label': 'Ripple', 'value': 'XRPUSDT'},
                        {'label': 'Polkadot', 'value': 'DOTUSDT'},
                    ],
                    value='BTCUSDT',
                    clearable=False
                )
            ], className='three columns'),
    ], className='row'),

    # datatable row
    html.Div([
        html.Div(id='crypto-data', className='eight columns data-table'),
    ], className='row'),
    
])
])

content_2 = html.Div([
    html.Div([
        dcc.RadioItems(
            id='select-col',
            options=[
                {'label': 'Open', 'value': 'Open'},
                {'label': 'High', 'value': 'High'},
                {'label': 'Low', 'value': 'Low'},
                {'label': 'Close', 'value': 'Close'},
                {'label': 'Volume', 'value': 'Volume'},
            ],
            inputStyle={
                "margin-right": "10px",
                "margin-left": "10px"
                },
            value='Open',
        )
    ],className='row'),
    html.Div([
        html.Div([
            dcc.Graph(id='line-graph',
                        figure={
                            'layout': {
                            'plot_bgcolor': config['bg-primary'],
                            'paper_bgcolor': config['bg-primary'],
                        }
                    }
            )
        ], className='nine columns'),

    ], className='row line-gr')

])
content_3 = html.Div('content 3')
