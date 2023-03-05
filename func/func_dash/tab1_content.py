import dash_bootstrap_components as dbc
from dash_extensions.enrich import html
from func.func_dash.buttons import search, enable

# Наполнение вкладок
def tab1_content():
    
    text_input = html.Div([
        dbc.Input(id="input", value="DB:EE:85:7F:44:09", type="text"),
        dbc.FormText("Вставьте MAC-адресс устройства здесь..."),
        ])
    
    # Кнопки
    button_search = search()
    button_enable = enable()
    
    content = dbc.Card( # Мне нравится рамочка, поэтому и использую
        dbc.CardBody([
            # Строка 1
            dbc.Row([
                dbc.Col([
                    text_input
                    ], width={"size": 3}),
                dbc.Col([
                    html.H5('Для поиска датчиков нажмите кнопку "Поиск датчиков".')
                    ], style={'marginTop': '5px'}, width={"size": 6, 'offset': 3}),
                ]),
            # Строка 2
            dbc.Row([
                dbc.Col([
                        button_enable
                        ]),
                dbc.Col([
                    button_search
                    ], width={"size": 3, 'offset' : 3}),
                dbc.Col([
                    html.Div(id='near_devices_list')
                    ]),
                ], style={'marginTop': '15px'}), 
            # Строка 3
            dbc.Row([html.Div(id='text_start')
                     ], style={'marginTop': '20px'})
            ]),
        className="mt-3")
    return content