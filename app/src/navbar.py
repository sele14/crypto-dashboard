import dash
import dash_core_components as dcc
import dash_html_components as html

def navbar() -> html.Div:
    """A navbar component, creating the top navigation bar."""
    navbar = html.Div([
        html.Nav([
            html.Ul([
                # dcc.Link([
                    html.A([
                        html.Span(["Crypto Trading Dashboard"], className='link-text')
                    ], className='nav-link')
                # ],href="/", className='nav-item')
            ], className='navbar-nav')

        ], className='navbar')
    ])

    return navbar