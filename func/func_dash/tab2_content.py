import dash_bootstrap_components as dbc
from dash_extensions.enrich import html


# Наполнение вкладок
def tab2_content():    
    content = dbc.Card(
        dbc.CardBody([
                dbc.Row([
                dbc.Col(html.Div('Траляля'))
            ]),
            
            ]),
        className="mt-3",)
    return content