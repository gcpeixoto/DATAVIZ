#!/usr/bin/env python
# coding: utf-8

# # _Dataviz Workshop_: _Dashboarding_ com _Dash_

# ## Objetivos do workshop
# 
# - Apresentar o ecossistema _Dash_ para criação de aplicações web para exploração e visualização de dados;
# - Compreender o processo básico de criação de um _dashboard_ utilizando _Dash_;
# - Desenvolver um _dashboard_ simples para exploração de dados sobre crimes violentos letais intencionais em João Pessoa.

# ## Ferramentas utilizadas
# 
# - Módulos Python    
#     - `dash`
#     - `dash_bootstrap_components`
#     - `plotly`
#     - `os`
#     - `pandas`
#     - `python` (interpretador)

# ## Sobre o _Dash_

# > _Dash is the original low-code framework for rapidly building data apps in Python._
# 
# - Ou seja, _Dash_ é um ecossistema que nos permite criar aplicações para exploração e visualização de dados para a web de forma rápida e totalmente em Python. 
# 
# - Basicamente, o _Dash_ possui três componentes fundamentais:
#     - [_Flask_](https://flask.palletsprojects.com/en/2.3.x/): a ferramenta de _backend_;
#     - [_Plotly_](https://plotly.com/python/): a ferramenta que provê as bibliotecas de plotagem (em nosso caso, usamos Python);
#     - [_React_](https://react.dev): a ferramenta que fornece o arcabouço interativo e de _frontend_;
# 
# - Uma vez que o Dash tem a vantagem de facilitar o desenvolvimento de aplicações puramente em Python, não é necessário conhecer profundamente HTML, CSS ou Javascript, por exemplo.
# 
# - Figuras feitas em matplotlib podem ser convertidas para _Dash_ com 
# `plotly.tools.mpl_to_plotly` (checar)

# ### Instalação
# 
# É recomendável instalar o _Dash_ através do _pip_: `pip install dash`.

# ### Pacotes essenciais
# 
# O _Dash_ contém alguns pacotes essenciais dedicados a funcionalidades específicas, a saber:
# - `Dash`: pacote principal e _backbone_ de qualquer aplicação a ser criada;
# - `Dash Core Components`: pacote de componentes interativas de manipulação (botões, _dropdowns_, _sliders_ etc.);
# - `Dash HTML Components`: pacote que fornece elementos HTML como classes Python;
# - `Dash Bootstrap Components`: pacote mantido por terceiros que cuida das opções _bootstrap_ (controle visual, opções de layout, interface etc.)

# ### Processo geral de criação de apps em Dash
# 
# - _Importações_ (_boilerplate_): receita básica de importação de módulos.
# - _Instanciamento_: criação do app via `Dash`;
# - _Chamada de layout_: formação dos contêineres e elementos básicos do _frontend_, principalmente via HTML. 
# - _Chamada de callbacks_: uso de decoradores Python que se aplicam a funções mais genéricas que tratam da disposição das representações visuais e da interatividade.
# - _Execução_: _deployment_ via comando Python.
# 

# ## Exemplos
# 
# Os exemplos são gerados por execução dos scripts acessórios localizados no diretório `dw`.
# 
# 
# - Demonstração básica: `python ../dw/dw1a.py`
# - Plataforma CVLI: `python ../dw/dw1b.py`

# ### Execução com _JupyterDash_
# 
# A execução diretamente via VSCode ou Jupyter notebook pode ser feita com a ajuda do módulo [JupyterDash](https://github.com/plotly/jupyter-dash) por meio da opção `app.run_server(mode='inline')`. Abaixo, criamos um _demo app_ nesses moldes.

# In[ ]:


# boilerplate imports 
import plotly.express as px
from dash import Dash #from jupyter_dash import JupyterDash
from dash import html, dcc, Output, Input
from pandas import read_csv

# carrega dados
df = read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# constroi app
app = Dash(__name__) #app = JupyterDash(__name__) 
app.layout = html.Div([
    html.H1(children='Crescimento populacional por país', 
            style={'color':'#117029'}),
    dcc.Dropdown(df.country.unique(), 'Brazil', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

# callback de atualização
@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

# executa app e mostra resultado inline
app.run() #app.run_server(mode='inline',inline_exceptions=True,PORT=8050)


# ### Modos de visualização
# 
# Há três modos disponíveis para visualizar um app com JupyterDash:
# 
# - `app.run_server(mode='external')`: saída para browser.
# - `app.run_server(mode='inline')`: saída para notebook.
# - `app.run_server(mode='jupyterlab')`: saída para JupyterLab.

# ## Referências
# 
# - [Dash User Guide](https://dash.plotly.com)
# - [Introducing JupyterDash](https://medium.com/plotly/introducing-jupyterdash-811f1f57c02e)
