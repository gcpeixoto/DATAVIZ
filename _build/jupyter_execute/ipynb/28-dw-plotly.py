#!/usr/bin/env python
# coding: utf-8

# # _Dataviz Workshop_: objetos gráficos e _Plotly Express_

# ## Objetivos do workshop
# 
# - Reconhecer a estrutura hierárquica de objetos gráficos;
# - Criar e atualizar instâncias do módulo `Plotly Express`;
# - Renderizar RVs interativas prontas para publicação na web;

# ## Ferramentas utilizadas
# 
# - Módulos Python        
#     - `plotly.express`
#     - `pandas`

# ## Objetos gráficos
# 
# Objetos gráficos são estruturas de dados hierárquicas (na forma de árvore) que descrevem uma RV em linguagem de máquina através de um esquema predefinido. O módulo `Plotly Express` é alimentado por esses objetos. O que ele faz é basicamente converter estruturas de dados Python em JSON serializados para pronta renderização na web. O termo _objeto gráfico_ refere-se a instâncias de classes Python que são hierarquicamente organizadas para cada tipo de RV. As principais classes são `Figure` e `FigureWidget`. Ambas permitem que os elementos do objeto JSON (nós da árvore), chamados de "atributos", sejam manipuláveis para controlar todas as características da RV, tais como o layout, os traços, a renderização e a exportação para diferentes formatos.
# 
# A construção de um objeto gráfico requer muitas linhas de código. Abaixo, mostramos um exemplo para um banco de dados de livros de uma biblioteca.

# In[1]:


import pandas as pd

# Livros disponíveis na biblioteca
df = pd.DataFrame({
    "Livro": ['Teoria da Computação','Ciência de Dados para Energia','Linguagens de Programação', 
              'Teoria da Computação','Ciência de Dados para Energia','Linguagens de Programação'],
    "Autor": ['Etelvin','Bruff','Non','Deltin','Fargo','Folly'],
    "Quantidade disponível": [10,6,4,6,8,2]
})


# In[2]:


import plotly.graph_objects as go
from IPython.display import display, HTML
from plotly.offline import plot


# Objeto gráfico
fig = go.Figure()
for autor, grupo in df.groupby("Autor"):
    fig.add_trace(go.Bar(x=grupo["Livro"], y=grupo["Quantidade disponível"], name=autor,
      hovertemplate="Autor=%s<br>Livro=%%{x}<br>Quantidade disponível=%%{y}<extra></extra>" % autor))
fig.update_layout(legend_title_text = "Autor")
fig.update_xaxes(title_text="Livro")
fig.update_yaxes(title_text="Quantidade disponível")

plot(fig, show_link=False,filename='dw-plotly-exemplo-1.html')
display(HTML('dw-plotly-exemplo-1.html'))


# A estrutura complexa acima é reproduzida de maneira equivalente com `Plotly Express` com apenas uma linha:

# In[3]:


import plotly.express as px

fig = px.bar(df,x="Livro",y="Quantidade disponível",color="Autor",barmode="group")

plot(fig, show_link=False,filename='dw-plotly-exemplo-2.html')
display(HTML('dw-plotly-exemplo-2.html'))


# ## Figuras como estruturas de dados
# 
# Apesar de a `Plotly` ser uma API para renderização de RVs e trazer muita facilidades para plotoagem interativa, haverá casos em que precisaremos manipular os atributos de uma figura para criar visuais customizados. Por isso, é também importante compreender um pouco das estruturas das figuras utilizadas pela `Plotly`, que basicamente são do tipo `dict` ou instâncias da classe `plotly.graph_objects.Figure`.

# - Para visualizar a estrutura, podemos usar `print`:

# In[4]:


import plotly.express as px

fig = px.line(x=["TC","CDIA","LP"], y=[16,14,6], title="Totais")

plot(fig, show_link=False,filename='dw-plotly-exemplo-3.html')
display(HTML('dw-plotly-exemplo-3.html'))


# In[5]:


print(fig)


# - Para visualizá-la como JSON, usamos:

# In[6]:


fig.show("json") 


# - Para exportá-la para JSON:

# In[7]:


fig.to_json() 


# - Adicionalmente, para exportá-la como um `dict` Python padrão, podemos usar:

# In[8]:


fig.to_dict() 


# ## Hierarquia do objeto `Figure` (esquema)

# O esquema de um objeto `Figure` manipulável pela Plotly possui três atributos de primeiro nível e vários atributos de níveis inferiores. Os três primários são: 
# 
# - `data`: contém uma lista de `dicts` que controlam os traços (substratos, vetores de dados, eixos, glifos etc.)
# - `layout`: `dict` de outros atributos que controlam o posicionamento e partes não relacionadas à figura (margens, cores, fontes, menus, sliders etc.)
# - `frame`: lista de `dicts` que definem sequências de frames em plots animados controlados por botões de menu ou sliders.

# Podemos criar uma RV do zero a partir de um dataframe acrescentando valores aos atributos explicitamente. Vejamos um exemplo:

# In[9]:


import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()


# In[10]:


# Figura vazia
fig = go.Figure() 
print(fig)


# In[11]:


# Adiciona traço do tipo histograma
fig.add_trace(go.Histogram(x=df['total_bill']),)
print(fig)


# In[12]:


# Atualiza layout
fig.update_layout(
    title='Histogram of Bills',
    xaxis_title='Total',
    yaxis_title='Frequency',
    bargap=0.05,    
    showlegend=False
)
print(fig)


# In[13]:


# Visualização
plot(fig, show_link=False,filename='dw-plotly-exemplo-4.html')
display(HTML('dw-plotly-exemplo-4.html'))


# In[14]:


# Atualiza cor do traço
fig.update_traces(marker_color='#02a5e2')

plot(fig, show_link=False,filename='dw-plotly-exemplo-5.html')
display(HTML('dw-plotly-exemplo-5.html'))


# ### Estilos personalizados
# 
# Quando não há necessidade de se criar algo do zero, pode-se usar as interfaces disponíveis. O dado anterior pode ser manipulado através dos passos a seguir:

# In[15]:


df = px.data.tips()
fig = px.histogram(df,x="total_bill",title="Histogram of Bills")
fig.update_traces(marker_color='#02a5e2')
fig.update_layout(
    title='Histogram of Bills',
    xaxis_title='Total',
    yaxis_title='Frequency',
    bargap=0.05,    
    showlegend=False
)

plot(fig, show_link=False,filename='dw-plotly-exemplo-6.html')
display(HTML('dw-plotly-exemplo-6.html'))


# Agora, vamos manipular o estilo para ter uma RV melhor:

# In[16]:


# interface
fig = px.histogram(df,x="day",
                   y="total_bill",
                   title="Histogram of Bills",
                   color="sex",
                   width=450,
                   height=350,
                   labels={
                       "sex": 'Gender',
                       "day": "Day of Week",
                       "total_bill": "Receipts"
                   },
                   category_orders={
                       "day": ['Thur','Fri', 'Sat','Sun'],
                       "sex": ['Male','Female']
                   },
                   color_discrete_map={
                       "Male": "orange", # CSS colors
                       "Female": "orchid"
                   },
                   template="plotly" # ['ggplot2', 'seaborn', 'simple_white', 
                                     # 'plotly','plotly_white', 'plotly_dark', 
                                     # 'presentation', 'xgridoff','ygridoff', 
                                     # 'gridon', 'none']
                   )

# atualizações
fig.update_yaxes(
    tickprefix="US$", 
    showgrid=True)

fig.update_layout(
    font_family="Rockwell",
    legend=dict(title=None, orientation="v", y=1, yanchor="bottom", x=0.8, xanchor="center"))

fig.add_shape(
    type="line", 
    line_color="black", 
    line_width=1.0, 
    opacity=1, 
    line_dash="dash",
    x0=0, x1=1, xref="paper", y0=950, y1=950, yref="y")

fig.add_annotation(
    text="below!", 
    x="Fri",
    y=400, 
    arrowhead=1, 
    showarrow=True)


plot(fig, show_link=False,filename='dw-plotly-exemplo-7.html')
display(HTML('dw-plotly-exemplo-7.html'))


# ```{admonition} Curiosidade
# :class: dropdown
# A criação e atualização de RVs em plotly basicamente depende de funções de alto nível baseadas nos prefixos add* e update*. Novos traços são adicionados com "add_trace" e seus atributos atualizados com "update_trace". Já "uptade_layout" serve para atualizar layouts. Estas são as mais usadas, mas existem outras.
# ```
