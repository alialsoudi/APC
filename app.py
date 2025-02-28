import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("حاسبة كمية البوتاس المتبقية"),

    html.Label("معدل التحميل (طن/ساعة):"),
    dcc.Input(id='loading_rate', type='number'),

    html.Label("الموقع (متر):"),
    dcc.Input(id='location_input', type='number'),

    html.Label("سرعة القشاط (متر/ثانية):"),
    dcc.Input(id='BELT_SPEED', type='number'),

    html.Label("كثافة البوتاس (كجم/متر مكعب):"),
    dcc.Input(id='POTASH_DENSITY', type='number'),

    html.Button('احسب', id='calculate'),

    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('calculate', 'n_clicks'),
    Input('loading_rate', 'value'),
    Input('location_input', 'value'),
    Input('BELT_SPEED', 'value'),
    Input('POTASH_DENSITY', 'value')
)
def update_output(n_clicks, loading_rate, location_input, BELT_SPEED, POTASH_DENSITY):
    if n_clicks:
        location = location_input + 100
        loading_rate_kg_per_sec = loading_rate * 1000 / 3600
        cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
        remaining_potash_volume = cross_sectional_area * location
        remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY
        remaining_potash_tons = remaining_potash_mass / 1000
        return f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن"

if __name__ == '__main__':
    app.run_server(debug=True)
