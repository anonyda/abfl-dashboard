from dash import Dash
from dash.dependencies import Input, State, Output
from .Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_html_components as html

url_base = '/dash/app1/'

df=pd.read_csv(r'C:\Users\Saara\python\prosperLoanData_.csv')

df['LoanOriginationDate'] = pd.to_datetime(df['LoanOriginationDate'])
df['ListingCreationDate'] = pd.to_datetime(df['ListingCreationDate'])
df['ClosedDate'] = pd.to_datetime(df['ClosedDate'])
df = df.sort_values(by='LoanOriginationDate',ascending=True)
data = [go.Scatter(
        x=df['LoanOriginationDate'],
        y = df['LoanNumber'],
        showlegend = True,
        name = 'Customers added',

    )]

graphLayout = dict(
    title='Customers Added',
    yaxis = dict(
        title = 'No. of customers added'),
    xaxis=dict(
        title = 'Date',
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(count=2,
                    label='2y',
                    step='year',
                    stepmode='backward'),
                dict(count=3,
                    label='3y',
                    step='year',
                    stepmode='backward'),
                dict(count=4,
                    label='4y',
                    step='year',
                    stepmode='backward'),
                dict(count=5,
                    label='5y',
                    step='year',
                    stepmode='backward'),
                dict(count=6,
                    label='6y',
                    step='year',
                    stepmode='backward'),
                dict(count=7,
                    label='7y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)
fig1 = dict(data=data, layout=graphLayout)

trace1 = go.Bar(
        x=df['LoanOriginationDate'],
        y = df['LenderYield'],
        showlegend = True,
        name = 'LenderYield',
        #mode='lines'
    )
trace2 = go.Bar(
        x=df['LoanOriginationDate'],
        y = df['EstimatedEffectiveYield'],
        showlegend = True,
        name = 'EstimatedEffectiveYield',
        #mode='lines'
    )

data2 = [trace1, trace2]

layout2 = dict(
    title='Yeild Of Company',
    yaxis = dict(
        title = 'Estimated vs actual '),
    xaxis=dict(
        title = 'Date',
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(count=2,
                    label='2y',
                    step='year',
                    stepmode='backward'),
                dict(count=3,
                    label='3y',
                    step='year',
                    stepmode='backward'),
                dict(count=4,
                    label='4y',
                    step='year',
                    stepmode='backward'),
                dict(count=5,
                    label='5y',
                    step='year',
                    stepmode='backward'),
                dict(count=6,
                    label='6y',
                    step='year',
                    stepmode='backward'),
                dict(count=7,
                    label='7y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)
fig2= dict(data=data2, layout=layout2)


trace3 = go.Bar(
        x=df['LoanOriginationDate'],
        y = df['EstimatedEffectiveYield'],
        showlegend = True,
        name = 'EstimatedEffectiveYield',
        #mode='lines'
    )

data3 = [trace1, trace3]

layout3 = dict(
    title='Yeild Of Company',
    yaxis = dict(
        title = 'Estimated vs actual '),
    xaxis=dict(
        title = 'Date',
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(count=2,
                    label='2y',
                    step='year',
                    stepmode='backward'),
                dict(count=3,
                    label='3y',
                    step='year',
                    stepmode='backward'),
                dict(count=4,
                    label='4y',
                    step='year',
                    stepmode='backward'),
                dict(count=5,
                    label='5y',
                    step='year',
                    stepmode='backward'),
                dict(count=6,
                    label='6y',
                    step='year',
                    stepmode='backward'),
                dict(count=7,
                    label='7y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)
fig3= dict(data=data3, layout=layout3)
#
# trace4 = go.Bar(
#         x=df['LoanOriginationDate'],
#         y = df['EstimatedEffectiveYield'],
#         showlegend = True,
#         name = 'EstimatedEffectiveYield',
#         #mode='lines'
#     )
#
# data4 = [trace1, trace2]
#
# layout4 = dict(
#     title='Yeild Of Company',
#     yaxis = dict(
#         title = 'Estimated vs actual '),
#     xaxis=dict(
#         title = 'Date',
#         rangeselector=dict(
#             buttons=list([
#                 dict(count=1,
#                      label='1m',
#                      step='month',
#                      stepmode='backward'),
#                 dict(count=6,
#                      label='6m',
#                      step='month',
#                      stepmode='backward'),
#                 dict(count=1,
#                     label='YTD',
#                     step='year',
#                     stepmode='todate'),
#                 dict(count=1,
#                     label='1y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(count=2,
#                     label='2y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(count=3,
#                     label='3y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(count=4,
#                     label='4y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(count=5,
#                     label='5y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(count=6,
#                     label='6y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(count=7,
#                     label='7y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(step='all')
#             ])
#         ),
#         rangeslider=dict(
#             visible = True
#         ),
#         type='date'
#     )
# )
# fig4= dict(data=data4, layout=layout4)

# layout = html.Div(
#     dcc.Graph(
#         figure=fig1
layout = html.Div(
    [
    dbc.Row([
        dbc.Col([
            html.H1('Performance'),
            html.Br(),
            dcc.Graph(
            figure=fig1
            ),
        ], width=6),
        dbc.Col([
            html.H1('Performance'),
            html.Br(),
            dcc.Graph(
                figure=fig3
            ),
            ]),
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Performance'),
            html.Br(),
            dcc.Graph(
            figure=fig1
            ),
        ], width=6),
        dbc.Col([
            html.H1('Performance'),
            html.Br(),
            dcc.Graph(
                figure=fig3
            ),
            ]),
    ]),
])
#     )
# )

# layout = html.Div(
#     [
#         dbc.Row(dbc.Col(html.Div("A single column"))),
#         dbc.Row(
#             [
#                 dbc.Col(html.Div("One of three columns")),
#                 dbc.Col(html.Div("One of three columns")),
#                 dbc.Col(html.Div("One of three columns")),
#             ]
#         ),
#     ]
# )

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base, external_stylesheets=[dbc.themes.BOOTSTRAP])
    apply_layout_with_auth(app, layout)

    '''@app.callback(
            Output('target', 'children'),
            [Input('input_text', 'value')])
    def callback_fun(value):
        return 'your input is {}'.format(value)'''
    
    return app.server