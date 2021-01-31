import plotly.express as px

def line(df, col):

    fig = px.line(df, x="Timestamp", y=col)

    fig.update_layout(
        xaxis_title = '',
        yaxis_title = 'Price',
        )
    
    return fig