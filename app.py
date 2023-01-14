import dash
from dash import html, dcc

import dash_bootstrap_components as dbc

from ml import ml_predict
from reddit import fetch_more_reddit


app = dash.Dash()
server = app.server


app.layout = html.Div([

    # row 1
     dbc.Row(
        html.H1(children="Reddit Stress Detection",
            style={'margin:':'100px', 'padding': '6px 12px',
                                'width':{"size": 6, "offset": 3},}),
        ),

    # row 2
    dbc.Row([

        dbc.Col([
        
            dbc.Col([
                dcc.Textarea(id='input-text', placeholder='Enter text here', 
                value='',
                style={'width': '50%', 'height': '200px', 'border': '1px solid #ccc',
                    'border-radius': '4px', 'padding': '6px 12px', 'font-size': '14px',
                    'line-height': '1.42857143', 'color': '#555', 'background-color': '#fff'}
            ,)
            
            ,
            dbc.Col([
                html.Button('Predict', id='button', style={"margin-top": "1em"}),
                html.Button('Fetch Post', id='fetch-button', style={"margin-top": "1em", "margin": "10px"}
            )], style={
            "padding": "10px"}),

            ], style={
            "width":"60%",
            "margin": "auto",
            "display": "block;"

            },),

             
         dbc.Col([
            # html.H5('Here'),
            html.Div(id='output-div-fetch'),
        
        ],
        
        width=5,
         style={'width': '40%', 'height': '20px', 'margin-right': '120px'}
             
        ),

        ],  style={
            "display": "flex",
            "margin": "50px"
            },),

        
    ]),


    # row 3
    dbc.Row([
             dbc.Col(
        [ html.Div(id='output-div')],
        ),
    ], style={'margin-left':'30px'})


        
   
])


@app.callback(
    dash.dependencies.Output('output-div', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-text', 'value')]
)
def predict_text(n_clicks, text):
    if not n_clicks:
        return

    print('prediction clicked')

    if text and text != '':
        # Perform prediction here
        result = ml_predict(text)

        if result == 'Stress':
            color = 'red'
        else:
            color = "blue"

        return html.Div([
            html.H4(children="Result", style={'margin:':'100px'}) ,

            html.Span(result, style={"color": color, 
              'padding': '6px 12px', }),
        ])


@app.callback(
    dash.dependencies.Output('output-div-fetch', 'children'),
    [dash.dependencies.Input('fetch-button', 'n_clicks')],
    [dash.dependencies.State('input-text', 'value')]
)
def fetch_text(n_clicks, text):
    if not n_clicks:
        return

    print('Fetching clicked')

    fetched, title = fetch_more_reddit() #fetch_reddit()

    print('\ntitle',title)

    return html.Div([
    html.H2(children="Fetched from Reddit", style={'margin:':'50px'}) ,

    dbc.Row([
        html.H3('Title: '),
        html.H4(title),


    ], style={'margin-top':'30px', 'display':'flex'}),

    # html.H3("Title: ", title),
    html.Ul([
        html.Li(item, style={
                'border': '1px solid #ccc', 'font-size': '15px',
                'line-height': '1.42857143', 'color': '#555',
        
        }) for item in fetched
    ])
])


# Dash code
if __name__ == '__main__':
    app.run_server()
