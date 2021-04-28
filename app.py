import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 8],
    y=[5, 56, 52, 10],
    mode='markers',
    name='data',
    hoverinfo='text',
    marker={'color': 'blue'}
))

fig.update_layout(
    xaxis_title='x',
    yaxis_title='y',
    dragmode='select',
    width=500,
    height=500,
    uirevision='static',
)

app.layout = dbc.Container(
    [
        dbc.Spinner(html.Div([
            dcc.Graph(id='chart1', figure=fig),
            dcc.Graph(id='chart2', figure=fig),
            dcc.Graph(id='chart3', figure=fig),
        ], id="card"), debounce=2000),
        dbc.Button("Trigger", id="trigger"),
    ],
    className="p-5",
)


@app.callback(
    Output("chart1", "fig"),
    Input("trigger", "n_clicks")
)
def callback(n):
    return fig

@app.callback(
    Output("chart2", "fig"),
    Input("trigger", "n_clicks")
)
def callback(n):
    return fig

@app.callback(
    Output("chart3", "fig"),
    Input("trigger", "n_clicks")
)
def callback(n):
    return fig


if __name__ == "__main__":
    app.run_server(debug=False)
