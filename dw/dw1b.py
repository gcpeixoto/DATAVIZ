# boilerplate Dash
from dash import Dash, html, dcc, dash_table, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

# dataframe
df = pd.read_csv('../data/crimes-pb-2015-2018.csv')

# instanciamento
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# layout
app.layout = html.Div([
    
    html.H1(children='Crimes Violentos Letais Intencionais (CVLI)', 
            style={'textAlign':'center',
                   'color':'black'}),
    
    html.H2('Cidade: João Pessoa - PB', style={'color':'#117029'}),
    html.P('Informações adicionais:'),
    html.Ul([
    html.Li('Cobertura Temporal: 2015 - 2018'),
    html.Li('Prevalência (p): quantifica o quanto é comum, ou rara, uma determinada ocorrência ou situação numa população.'),
    html.Li('Fórmula: p = ( quantidade de casos / população ) x 100%'),
    html.Li(['Fonte da pesquisa: ',
             html.A('Repositório UFPB: Tese', 
           href='https://repositorio.ufpb.br/jspui/bitstream/123456789/16029/1/PMS09102019.pdf')
        ])
    ]),
    html.Hr(),
    html.H2('Tabela',style={'color':'#117029'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    html.Hr(),
    html.H2('Seleção de Variáveis para Histograma', style={'color':'#117029'}),
    dcc.RadioItems(options=['Prevalência',
                            'Arma de fogo','Arma branca',
                            'Outros'], 
                   value='Arma de fogo', 
                   id='RdBtn1'),
    dcc.Graph(figure={},id='Grph1'),
    html.Hr(),
    html.H5('UFPB | CDIA | DATAVIZ | Ano 2023',style={'textAlign':'center','color':'#117029'}),
    ])

# callback
@callback(
    Output(component_id='Grph1', component_property='figure'),
    Input(component_id='RdBtn1', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='Bairros', y=col_chosen)
    return fig

# execução
# > python dcs28.py
if __name__ == '__main__':
    app.run_server(debug=True,
                   port=os.getenv('PORT',8090))
