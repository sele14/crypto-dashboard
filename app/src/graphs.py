import plotly.express as px
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
