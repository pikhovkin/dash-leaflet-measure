import dash
from dash import html
import dash_leaflet as dl

import dash_leaflet_measure as dlm


app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    dl.Map(id='map', zoom=4, children=[
        dl.LayersControl(children=[
            dl.BaseLayer(dl.TileLayer(), name='OpenStreetMap', checked=True)
        ]),
        # dl.MeasureControl(),
        dlm.MeasureControl(),
    ], style=dict(width='100%', height='100%'))
], style=dict(width='99%', height='99%', position='absolute'))


if __name__ == '__main__':
    app.run_server(debug=True)
