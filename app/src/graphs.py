import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.configs import config

def line(df, col):

    fig = px.line(df, x="Timestamp", y=col)

    fig.update_layout(
        xaxis_title = '',
        yaxis_title = 'Price',

        font_color=config['text-secondary'],
        plot_bgcolor=config['bg-primary'],
        paper_bgcolor=config['bg-primary'],
        xaxis =  {'showgrid': False},
        yaxis = {'showgrid': False}

        )

    fig.update_traces(line_color=config['text-secondary'])

    
    return fig

def greeks_plot(df, cols):
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # chack if Forward in columns, as it requires secondary axis
    
    if 'Forward' in cols:
        fig.add_trace(
            go.Scatter(
                    x=df['BaseDate'],
                    y=df['Forward'],
                    mode='lines',
                    name='Forward'
                
                ), secondary_y=True
            )
        
        # remove forward so we can keep it on secondary axis
        cols.remove('Forward')
        for i in range(len(cols)):

            fig.add_trace(
                go.Scatter(
                        x=df['BaseDate'],
                        y=df[cols[i]],
                        mode='lines',
                        name=cols[i]
                    )
                )

    else:
        for i in range(len(cols)):
        
            fig.add_trace(
                go.Scatter(
                        x=df['BaseDate'],
                        y=df[cols[i]],
                        mode='lines',
                        name=cols[i]
                    )
                )

    fig.update_layout(
        xaxis_title = '',
        yaxis_title = '',
        yaxis2_title = '',


        font_color=config['text-secondary'],
        plot_bgcolor=config['bg-primary'],
        paper_bgcolor=config['bg-primary'],
        xaxis =  {'showgrid': False},
        yaxis = {'showgrid': False},
        yaxis2 = {'showgrid': False}

        )

    return fig