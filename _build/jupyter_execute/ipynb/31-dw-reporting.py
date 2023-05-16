#!/usr/bin/env python
# coding: utf-8

# # _Dataviz Workshop_: _Reporting_ com _xhtml2pdf_

# In[1]:


from xhtml2pdf import pisa
import pandas as pd, re


# In[2]:


# geração de HTML atualizável
def html_data(table):
    text = f'\
        <h2>Dados</h2>\
        <p>Mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Ultricies mi eget mauris pharetra et ultrices neque ornare aenean.\
        Sit amet cursus sit amet. Varius vel pharetra vel turpis nunc eget lorem. Enim lobortis scelerisque fermentum dui faucibus.\
        Nibh tellus molestie nunc non blandit massa enim nec dui. Non nisi est sit amet facilisis magna.\
        {table.to_html(index=False)}\
        </p>\
        <h2>Análise</h2>\
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
        Viverra ipsum nunc aliquet bibendum enim facilisis. Dui nunc mattis enim ut tellus elementum sagittis vitae. Sed adipiscing diam donec adipiscing tristique.\
        Ut sem nulla pharetra diam sit. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Diam phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet.\
        Elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique. Pharetra convallis posuere morbi leo. Et magnis dis parturient montes nascetur.\
        Tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed. Amet justo donec enim diam vulputate ut pharetra sit amet. Tempor nec feugiat nisl pretium fusce id velit.\
        Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan. Mollis nunc sed id semper risus in hendrerit gravida rutrum. Ultrices vitae auctor eu augue ut.\
        Sit amet nisl suscipit adipiscing bibendum est ultricies integer. Urna condimentum mattis pellentesque id. Quisque non tellus orci ac auctor augue.\
        Dolor sed viverra ipsum nunc aliquet bibendum enim.\
        \n\
        Et malesuada fames ac turpis egestas. Pretium nibh ipsum consequat nisl vel pretium. Consectetur adipiscing elit ut aliquam purus.\
        Duis at consectetur lorem donec massa. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. In iaculis nunc sed augue lacus viverra.\
        Malesuada fames ac turpis egestas maecenas pharetra convallis. Massa sed elementum tempus egestas. Turpis egestas maecenas pharetra convallis posuere morbi. \
        Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus. Tempus iaculis urna id volutpat.\
        \n'
    
    return text


# In[3]:


df = pd.read_csv('../data/crimes-pb-2015-2018.csv')


# In[4]:


# carregamento do modelo
html_report_template = '../dw/reporting/report_template.html'


# In[5]:


# função de utilidade para conversão
def html_to_pdf(html_in, pdf_out):
    
    # arquivo de saída
    outfile = open(pdf_out, 'w+b')

    # conversão
    c = pisa.CreatePDF(html_in, dest=outfile)

    # fecha arquivo
    outfile.close()

    # retorna True se houver erro; False, senão
    return c.err


# In[11]:


if __name__ == "__main__":
    pisa.showLogging()
    
    # inserção de dado no modelo
    with open(html_report_template) as h:
        source_html = h.read()
        cutoff = re.search('(</body>)',source_html).span()[0]
        head = source_html[:cutoff]    
        tail = source_html[cutoff:]
        mid = html_data(df)    
        source_html = head + mid + tail
    
        html_to_pdf(source_html,'../dw/reporting/dw-report.pdf')
        


# In[17]:


from IPython.display import IFrame

IFrame(src='http://gcpeixoto.github.io/DATAVIZ/dw/reporting/dw-report.pdf',
       width=600,height=400)


# ## Objetivos do workshop
# 
# - Apresentar o ecossistema _Dash_ para criação de aplicações web para exploração e visualização de dados;
# - Compreender o processo básico de criação de um _dashboard_ utilizando _Dash_;
# - Desenvolver um _dashboard_ simples para exploração de dados sobre crimes violentos letais intencionais em João Pessoa.

# ## Ferramentas utilizadas
# 
# - Módulos Python    
#     - `dash`
#     - `dash_bootstrap_componentes`
#     - `plotly`
#     - `os`
#     - `pandas`
#     - `python` (interpretador)

# ## Sobre o _Dash_

# > _Dash is the original low-code framework for rapidly building data apps in Python._
# 
# - Ou seja, _Dash_ é um ecossistema que nos permite criar aplicações para exploração e visualização de dados para a web de forma rápida e totalmente em Python. 
# 
# - Basicamente, o _Dash_ é uma possui três componentes fundamentais:
#     - [_Flask_](https://flask.palletsprojects.com/en/2.3.x/): a ferramenta de _backend_;
#     - [_Plotly_](https://plotly.com/python/): a feramenta que provê as bibliotecas de plotagem (em nosso caso, usamos Python);
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
# A execução diretamente via Jupyter notebook pode ser feita com a ajuda do módulo [JupyterDash](https://github.com/plotly/jupyter-dash) por meio da opção `app.run_server(mode='inline')`. Abaixo, criamos um _demo app_ nesses moldes.

# In[ ]:


# boilerplate imports 
import plotly.express as px
from jupyter_dash import JupyterDash
from dash import html, dcc, Output, Input
from pandas import read_csv

# carrega dados
df = read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# constroi app
app = JupyterDash(__name__)
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
app.run_server(mode='inline')


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
