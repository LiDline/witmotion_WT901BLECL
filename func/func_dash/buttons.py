import dash_bootstrap_components as dbc
from dash_extensions.enrich import html


# Кнопка поиска устройства
def search():
    button_search = dbc.Button("Поиск датчиков", color="primary", id='button_search', n_clicks=0, size="lg",)
    return button_search


# Кнопка старт/стоп
def enable():
    enable = dbc.Button("Подключиться к датчику", color="primary", id='button_start', n_clicks=0, size="lg",)
    return enable