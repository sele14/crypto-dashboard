import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_trich_components as dtc

from src.navbar import navbar

def layout() -> html.Div:
    """Creates the main layout / UI structure."""
    layout = html.Div([
        
        # store data
        dcc.Store(id='store-data'),

        # navbar
        navbar(),

        # sidebar
        html.Div([
            dtc.SideBar([
                dtc.SideBarItem(id='id_1', label="Get Data", icon="fas fa-table"),
                dtc.SideBarItem(id='id_2', label="Data Viz", icon="fas fa-chart-line"),
                dtc.SideBarItem(id='id_3', label="Download", icon="fas fa-file-download"),
        ], bg_color='#16181a', className='sidebar'),
        ],
        # style={'position': 'relative'}
        ),

        html.Div([
            # page content from sidebar
            html.Div([], id="page-content"),
            
        ], className='layout-body')
    ],className='main-layout')

    return layout