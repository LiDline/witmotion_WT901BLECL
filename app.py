from dash_extensions import WebSocket
from dash_extensions.enrich import html, Output, Input, State, DashProxy, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import os
import dash
from dash import DiskcacheManager, CeleryManager


from func.func_dash.tab1_content import tab1_content
from func.func_dash.tab2_content import tab2_content
from func.device_search import device_search


if 'REDIS_URL' in os.environ:
    # Use Redis & Celery if REDIS_URL set as an env variable
    from celery import Celery
    celery_app = Celery(__name__, broker=os.environ['REDIS_URL'], backend=os.environ['REDIS_URL'])
    background_callback_manager = CeleryManager(celery_app)
    suppress_callback_exceptions=True

else:
    # Diskcache for non-production apps when developing locally
    import diskcache
    cache = diskcache.Cache("./cache")
    background_callback_manager = DiskcacheManager(cache)


'''App'''

app = DashProxy(name="WT901BLE", external_stylesheets=[dbc.themes.BOOTSTRAP],
                background_callback_manager=background_callback_manager,
                suppress_callback_exceptions=True # Если не все объекты, на которые ссылаются, сейчас существуют
                )
#___________________________________________________________________________________________________

# Client-side function (for performance) that updates the graph.
with open('func/graph.js') as f:    # plot the data
    update_graph = f.read()
#___________________________________________________________________________________________________

tabs = html.Div([
    dbc.Tabs([
            dbc.Tab(label="Bluetooth", tab_id="Bluetooth"),
            dbc.Tab(label="USB", tab_id="USB"),
            ], id="tabs", active_tab="Bluetooth"),
    html.Div(id="content"),
    ])
#___________________________________________________________________________________________________

'''Layout'''

app.layout = html.Div([
    
    # Header
    dbc.Row([
            dbc.Col(html.H1('WT901BLE',
                            style={'textAlign': 'center', 'marginTop': '10px'}))
            ], className='app-headr'),
    # Other
    dbc.Row([
        dbc.Row([
                dbc.Col(html.H4('Выберите тип считывающего устройства:', 
                                style={'marginTop': '15px'}))
                ]),
        dbc.Row([tabs], style={'marginTop': '15px'}),
            ], style={'marginLeft': '80px', 'marginRight': '80px'}), 
    ])
#___________________________________________________________________________________________________

'''Callback'''

# Callback for Tabs
@app.callback(Output("content", "children"), 
              [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "Bluetooth":
        return tab1_content()
    elif at == "USB":
        return tab2_content()


# Кнопка "Поиск устройств"
@dash.callback(
    output=Output("near_devices_list", "children"),
    inputs=Input("button_search", "n_clicks"),
    prevent_initial_call=True,   # Не включает callback при первом запуске
    background=True,
    running=[
        (Output("button_search", "disabled"), True, False),
        (Output("button_start", "disabled"), True, False),
        ])
def update_button(n_clicks):
    values = device_search()
    if len(values) > 0:
        table_header = [html.Thead(html.Tr([html.Th("Имя устройства"), html.Th("Адресс")]))]
        row = [
            html.Tr([html.Td(values[i].name), html.Td(values[i].address)]) for i in range(len(values))
               ]

        table_body = [html.Tbody(row)]
        return dbc.Table(table_header + table_body, bordered=True)
    return ['Устройства не найдены']


# Кнопка подключения
@dash.callback(
    Output("text_start", "children"),
    Input("button_start", "n_clicks"),
    prevent_initial_call=True,
    background=True,
    running=[
        (Output("button_start", "disabled"), True, False),
        (Output("button_search", "disabled"), True, False),
        (Output("input", "disabled"), True, False),
    ],

)
def start_button(n_clicks):
    res = dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph"), WebSocket(id="ws", url="ws://127.0.0.1:5000/WT901"),
            ], width={"size": 12},),
        ])
    return res


app.clientside_callback(update_graph, 
                        Output("graph", "figure"), 
                        Input("ws", "message"),
                        )

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)