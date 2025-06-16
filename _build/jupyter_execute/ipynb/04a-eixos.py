#!/usr/bin/env python
# coding: utf-8

# # Eixos, Escalas e Sistemas de Coordenadas

# Definir escalas de posição é imprescindível para visualizar informações, especialmente quantitativas. Escalas de posição em conjunto com um arranjo geométrico formam um _sistema de coordenadas_.
# 
# O sistema de coordenadas mais comum que utilizamos é o Cartesiano, em que o eixo de abscissas (geralmente representado pela variável $x$) corre horizontalmente e o de ordenadas (geralmente representado pela variável $y$) corre verticalmente. Entretanto, a maneira de relacionar dados poderia ocorrer com $y$ correndo de maneira oblíqua em relação a $y$, ou com $y$ mudando de maneira circular e $x$ de maneira radial. Neste último caso, teríamos um _sistema de coordenadas polares_. 
# 
# Escalas ajudam a posicionar a informação e a criar representações visuais com _razões de aspecto_ distintas. Figuras esticadas na direção vertical e estreitas na direção horizontal enfatizarão um sentido de "crescer para cima", por exemplo. Por outro lado, figuras compridas na direção horizontal e encurtadas na direção vertical podem dar uma ideia de algo que se "prolonga para o lado". Definir razões de aspecto é uma escolha totalmente dependente do projeto visual. 

# ## Sistemas cartesianos e razões de aspecto
# 
# Vejamos um exemplo de como criar representações visuais cartesianas com diferentes razões de aspecto.
# 
# ### Sinal estocástico
# 
# Um sinal estocástico (ou aleatório) é aquele em que nenhuma previsibilidade ou padrão são detectáveis. Comportamentos estocásticos estão presentes em eventos climáticos, ativos do mercado financeiro, sistemas eletrônicos e audiovisuais, atividades bioquímicas e em muitas outras áreas. Casos típicos buscam visualizar como uma dada grandeza varia em função do tempo.

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
from string import ascii_lowercase as lc

def test_aspect_ratio(Lx,fator,tag):
    
    dist = np.random.normal(size=(200),loc=0.0,scale=1.0)
    
    fig, ax = plt.subplots(figsize=(Lx,fator*Lx))
    
    ax.plot(dist,lw=1.0,c='#117029')
    ax.set_xlabel('x',fontsize=8)
    ax.set_ylabel('y',fontsize=8)
    
    ax.set_title(f'{tag}) Lx = {Lx}; Ly = {fator*Lx}',fontsize=8)

c = 0
for Lx in [2,4]:
    for fator in [0.1,0.5,1,2]:
        test_aspect_ratio(Lx,fator,lc[c])
        c += 1


# Dos casos anteriores, haja vista a natureza da informação plotada, percebe-se que nem todas possuem um visual agradável. Na sua opinião, alguma representação visual é a mais adequada? Para tomar a decisão de escolha, que critério(s) você usaria?

# ```{admonition} Dica
# :class: dropdown
# Para aprofundamento, estude sobre o controle de razão de aspecto de eixos com ax.axis() no Guia Rápido de Plotagem - matplotlib.
# ```

# ### Série temporal
# 
# A visualização abaixo corresponde a dados reais de montantes repassados pela Petrobras ao Fundo Amazônia - BNDES entre 2012 e 2018 de acordo com o Ministério do Meio Ambiente.

# In[262]:


import pandas as pd
import seaborn as sns

# dados 
f_amaz = pd.read_csv('../data/petr-repasse-redd-amazonia.csv')
f_amaz.drop(index=0,inplace=True)
f_amaz


# In[263]:


# visualização
sns.set_style("darkgrid")
fig, ax = plt.subplots(1,2,figsize=(10,3),constrained_layout=True)
fig.suptitle('Repasses para Fundo Amazônia - BNDES: Petrobras')

f = sns.lineplot(x='ano',y='repasse',data=f_amaz, marker='o',c='#117029',ax=ax[0])
f.set_title('Escala linear');
f.set_ylabel('repasse (R$)');

f = sns.lineplot(x='ano',y='repasse',data=f_amaz, marker='o',c='#117029',ax=ax[1])
f.set(yscale='log') # 'linear', 'log', 'symlog', 'logit', 'function', 'functionlog'
f.set_title('Escala logarítmica');
f.set_ylabel('');


# Este exemplo lida com valores financeiros. No primeiro caso, a escala do eixo _y_ é linear; no segundo, é _logarítmica_, isto é, não linear. 
# 
# Há situações em que escalas não lineares para os eixos mostram-se mais adequadas do que escalas não lineares. Os exemplos a seguir fazem essas diferenciações.

# In[264]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc_file_defaults()

# dados
x = np.array([1,3.16,10,31.6,100])

# figuras
fig, ax = plt.subplots(1,4,figsize=(10,1),constrained_layout=True)

# plotagens
ax[0].plot(x,0*x,'o',ms=8,c='#117029')
ax[0].get_yaxis().set_visible(False)
ax[0].axis('equal')
ax[0].spines['bottom'].set_color('gray')
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].set_xlabel('$x$')
ax[0].set_title('dados originais; escala linear',fontsize=8)

ax[1].semilogx(x,0*x,'o',ms=8,c='#117029')
ax[1].get_yaxis().set_visible(False)
ax[1].axis('equal')
ax[1].spines['bottom'].set_color('gray')
ax[1].spines['top'].set_visible(False)
ax[1].spines['left'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].set_xlabel('$x$')
ax[1].set_title('dados originais; escala logarítmica',fontsize=8)

ax[2].plot([1,2,3,4,5],0*x,'o',ms=8,c='#117029')
ax[2].get_yaxis().set_visible(False)
ax[2].axis('equal')
ax[2].set_xticks([1,2,3,4,5])
ax[2].set_xticklabels([0,0.5,1.0,1.5,2.0])
ax[2].spines['bottom'].set_color('gray')
ax[2].spines['top'].set_visible(False)
ax[2].spines['left'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].set_xlabel('$\log_{10}(x)$')
ax[2].set_title('dados transformados; escala linear',fontsize=8)

ax[3].plot([1,2,3,4,5],0*x,'o',ms=8,c='#117029')
ax[3].get_yaxis().set_visible(False)
ax[3].axis('equal')
ax[3].set_xticks([1,2,3,4,5])
ax[3].set_xticklabels([1,3.16,10,31.6,100])
ax[3].spines['bottom'].set_color('gray')
ax[3].spines['top'].set_visible(False)
ax[3].spines['left'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].set_xlabel('$x$')
ax[3].set_title('dados originais; escala logarítmica',fontsize=8);


# ## Sistemas polares
# 
# A representação de quantidades em coordenadas polares é feita alterando o mecanismo de _projeção_ dos eixos.

# In[19]:


r = np.arange(0, 300, 0.01)
theta = 0.5*r*np.sin(r)

# configuração do eixo
fig, ax = plt.subplots(figsize=(4,4),subplot_kw={'projection': 'polar'})
ax.plot(theta, r,c='#117029')
ax.set_rmax(10)
ax.set_title('Plotagem da função $\\theta(r) = \\frac{1}{2}r sen(r)$', va='center',fontsize=8);


# ```{admonition} Curiosidade
# :class: dropdown
# A metodologia do ranking global de universidades [U-Multirank](https://www.umultirank.org) usa 36 indicadores divididos em 5 dimensões (ensino e aprendizagem, pesquisa, transferência de conhecimento, orientação internacional e engajamento regional) para avaliar o desempenho de uma instituição de ensino superior. Essas dimensões são representadas visualmente através de um "gráfico de raios de sol" ([sunburst](https://www.umultirank.org/press-media/media-center/infographics/)), o qual, por sua vez, é construído sob um sistema de coordenadas polares. Porém, apenas as variações radiais (nível de excelência de uma dada dimensão) realmente importam. 
# ```

# ### Exemplo: Temperatura oceânica ao longo do tempo
# 
# Sistemas polares são apropriados para visualizar a variação de temperatura oceânica ao longo do tempo em diferentes lâminas d'água. O exemplo a seguir mostra a dinâmica de temperatura ao longo de 10 anos para a temperatura de uma região do Mar Mediterrâneo. O código é uma adaptação de sua versão [original](https://matplotlib.org/matplotblog/posts/animated-polar-plot/), com dados obtidos do banco de dados ARGO, por meio da base de dados francesa [ERDDAP](https://erddap.ifremer.fr/erddap/griddap/SDC_NS_CLIM_TS_V1_m.html).  

# In[ ]:


import numpy as np, pandas as pd, matplotlib, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

plt.rcParams['xtick.major.pad']='17'
plt.rcParams["axes.axisbelow"] = False
matplotlib.rc('axes',edgecolor='w')

# Read data
ndf = pd.read_csv('../data/mediterranean-sea-temp-argo.csv')

# Range data
daterange = np.arange('2010-01-01','2020-01-03', dtype='datetime64[7D]')


# Settings
big_angle= 360/12  # polar division
date_angle=((360/365)*ndf['day_of_the_year'])*np.pi/180  # corresponding angle for each day
inner, outer = 10, 30 # inner, outer ring limit values
ocean_color = ["#008790","#004752"] # surface, depth colors 


# Utility functions
def dress_axes(ax):
    """Format polar axes for yearly variation."""
    
    ax.set_facecolor('w')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    
    # Months labels
    middles=np.arange(big_angle/2 ,360, big_angle)*np.pi/180
    ax.set_xticks(middles)
    ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
    ax.set_yticks([15,20,25])
    ax.set_yticklabels(['15 °C','20 °C','25 °C'])
    
    # Radial ticks angle
    ax.set_rlabel_position(359)
    ax.tick_params(axis='both',color='w')
    plt.grid(None,axis='x')
    plt.grid(axis='y',color='w', linestyle=':', linewidth=1)    
    
    # Bar plot as background

    ax.bar(middles, outer, width=big_angle*np.pi/180, bottom=inner, color='lightgray', edgecolor='w',zorder=0)
    plt.ylim([2,outer])
    
    # Custom legend
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Surface', markerfacecolor=ocean_color[0], markersize=15),
                       Line2D([0], [0], marker='o', color='w', label='1000m', markerfacecolor=ocean_color[1], markersize=15),
                       ]
    ax.legend(handles=legend_elements, loc='center', fontsize=13, frameon=False)
    
    # Main title
    plt.suptitle('Temperaturas no Mar Mediterrâneo (ARGO data)',fontsize=16,horizontalalignment='center')
    
    
# Open figure
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)
dress_axes(ax)

# For animation with blit=True, to render only changes
line_ts = ax.plot([], [], '-', color=ocean_color[0], alpha=1.0, linewidth=5)[0]
line_t1000 = ax.plot([], [], '-', color=ocean_color[1], alpha=1.0, linewidth=5)[0]
line_ts_fine = ax.plot([], [], '-', color=ocean_color[0], linewidth=0.7)[0]
line_t1000_fine = ax.plot([], [], '-', color=ocean_color[1], linewidth=0.7)[0]
line_ref = ax.plot([], [], 'k-', linewidth=0.5)[0]

# Update function for animation
def draw_data(i):
    
    # Limit between thin lines and thick line: current date minus 51 weeks
    i0 = np.max([i - 51, 0])

    # Update the data for the thick lines (full range)
    line_ts.set_data(date_angle[i0:i+1], ndf['tsurf'][i0:i+1])
    line_t1000.set_data(date_angle[i0:i+1], ndf['t1000'][i0:i+1])

    # Update the data for the fine lines (detailed)
    line_ts_fine.set_data(date_angle[0:i+1], ndf['tsurf'][0:i+1])
    line_t1000_fine.set_data(date_angle[0:i+1], ndf['t1000'][0:i+1])

    # Update the reference line (vertical line indicating current time)
    line_ref.set_data([date_angle[i], date_angle[i]], [inner, outer])

    # Update title with current year
    ax.set_title(str(ndf['active_year'][i]), fontsize=16, horizontalalignment='center')

    return line_ts, line_t1000, line_ts_fine, line_t1000_fine, line_ref
    
# Test it
# draw_data(322); plt.show()    
plt.close(fig)


# In[13]:


# increase interval for more resolution
anim = FuncAnimation(fig, draw_data, interval=20, frames=len(daterange)-1, repeat=False, blit=True)    
HTML(anim.to_html5_video())


# ## Sistemas geoespaciais
# 
# Sistemas geoespaciais são úteis para plotagem de dados cartográficos, mapas e geolocalizações.

# In[274]:


import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.5, 3))
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines()
ax.gridlines();


# ## Visualizações 3D

# Visualizações bidimensionais são sempre preferíveis a tridimensionais devido à carga cognitiva exigida para interpretação da informação em 3D. Entretanto, nem sempre é possível atingir representações visuais satisfatórias com apenas 2 dimensões, especialmente quando a terceira dimensão possui variações. Este é o caso de uma superfície descrita como $z = f(x,y)$ em que $z$ é uma elevação de terreno, por exemplo. Eixos 3D são particularmente excelentes quando se quer interagir com ou manipular o visual.

# ### Visualização de funções matemáticas
# 
# O exemplo abaixo mostra como plotar a função dada por
# $f(x,y) = 4e^{ - \
#      \left[ \left( x -  \frac{a+b}{2} \right)^2  + \
#              \left( y -  \frac{c+d}{2} \right)^2 \right] },$
# para o domínio bidimensional $[a,b] \times [c,d]$. Esta função, em sentido genérico, poderia bem representar uma pequena montanha, um tipo de chapéu, ou mesmo uma protuberância, tal qual um puxão na pele ou uma ectasia corneana. Independentemente da aplicação, as representações visuais fornecidas forneceriam diferentes posto de vista para o fenômeno, ajudando o _viewer_ a interpretá-lo melhor.

# In[267]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# limites do domínio: região do plano [a,b] x [c,d]
a, b = -2, 2
c, d = -1, 3

# no. de pontos em cada direção
nx, ny = 40, 40 

# distribuição dos pontos
x = np.linspace(a,b,nx)
y = np.linspace(c,d,ny)

# grade 2D
[X,Y] = np.meshgrid(x,y)

# superfíe
Z = 4*np.exp(-( ( X - (a+b)/2 )**2 + ( Y - (c+d)/2 )**2 ))

# plotagem
fig = plt.figure(figsize=(10,4),constrained_layout=True)
fig.suptitle('$f(x,y) = 4e^{ -      \\left[ \\left( x -  \\frac{a+b}{2} \\right)^2  +              \\left( y -  \\frac{c+d}{2} \\right)^2 \\right] }$')

gs = fig.add_gridspec(1,3) 
ax1 = fig.add_subplot(gs[0],projection='3d')
ax2 = fig.add_subplot(gs[1],projection='3d')
ax3 = fig.add_subplot(gs[2])

# superfície
ax1.set_zlim(0,5)
s = ax1.plot_surface(X,Y,Z,cmap=cm.jet)
fig.colorbar(s, shrink=0.5,ax=ax1)
ax1.set_title('Superfície',fontsize=8)

# aramado
ax2.set_zlim(0,5)
s = ax2.plot_wireframe(X,Y,Z,cmap=cm.jet,lw=0.4)
ax2.axis('off')
ax2.set_title('Superfície aramada',fontsize=8)

# curvas de nível com preenchimento
ax3.contourf(X,Y,Z,cmap=cm.jet)
ax3.axis([a,b,c,d])
ax3.set_title('Curvas de nível',fontsize=8);


# ```{admonition} Curiosidade
# :class: dropdown
# O [ceratocone](https://pt.wikipedia.org/wiki/Ceratocone) é uma doença da córnea (estrutura do olho humano) que progride a curvatura normal dela, deixando-a cada vez mais no formato de um cone. Consequentemente, o elevado grau ocular faz com que a pessoa acometida da doença tenha uma visão superembaçada. De certa maneira, a superfície deformada da córnea pode ser aproximada por uma função matemática que, não surpreendentemente, dependerá de uma representação visual como a mostrada nesta seção para auxiliar oftalmologistas em seus diagnósticos. 
# ```
# 

# ### Visualização de dados multidimensionais categóricos
# 
# A representação visual abaixo lida com os preços de combustíveis aplicados em diversos municípios da Paraíba por diferentes operadoras (bandeiras).

# In[ ]:


import plotly.express as px
from plotly.offline import plot
import numpy as np
import pandas as pd
from IPython.display import display, HTML

df = pd.read_csv('../data/preco-combs-pb-2022-02.csv')
fig = px.scatter_3d(df, 
                    x='Produto', 
                    y='Municipio', 
                    z='Bandeira', 
                    size='Valor de Venda', 
                    color='Valor de Venda',
                    hover_data=['Valor de Venda'])
fig.update_layout(margin=dict(l=50, r=50, t=50, b=50),
                  font=dict(size=10))
plot(fig, show_link=False,filename='../exemplo-vis-3d.html')
display(HTML('../exemplo-vis-3d.html'))

