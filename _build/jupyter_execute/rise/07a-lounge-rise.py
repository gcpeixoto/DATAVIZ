#!/usr/bin/env python
# coding: utf-8

# # _Lounge_ das Representações Visuais
# 
# Prof. Gustavo Oliveira
# 
# CI/DCC/UFPB
# 
# [gcpeixoto.github.com/DATAVIZ](gcpeixoto.github.com/DATAVIZ)

# ## Introdução 
# 
# - Aproximação às diversas classes de RVs disponíveis em dataviz 
# - Preparação para as tecnicalidades de construção gráfica
# - O propósito é compreender a finalidade e a aplicabilidade dos _plots_. 

# ### Grupos de RVs
# 
# - Consideraremos _plots_ para representar:
#     - quantidades
#     - distribuições
#     - proporções
#     - correlações
#     - dados geoespaciais
#     - incertezas

# ## _Plots_ para visualizar quantidades
# 
# - Naturalmente ligados a valores numéricos associados a algumas categorias. 
# - Neste grupo encontram-se: 
#     - **gráfico de barras**, simples, empilhadas (_stacked_) ou agrupadas (_grouped_), dispostas horizontal ou verticalmente; 
#     - **gráfico de pontos**, uma versão simplificada dos gráficos de barras;
#     - **mapas de calor** (_heatmap_), que quantificam a informação pela cor;

# ### Barras (_bar plot_)
# 
# - Fonte de dados do cinema. 
# - Os _dataframes_ a seguir registram as 10 maiores bilheterias do cinema nos EUA a Brasil em mi US$.
# 
# Fonte: [Box Office Mojo](https://www.boxofficemojo.com)

# In[1]:


import pandas as pd

df_us = pd.read_csv('../data/top10-bilheteria-cinema-2022-us.csv')
df_br = pd.read_csv('../data/top10-bilheteria-cinema-2022-br.csv')
df_us


# In[2]:


df_br


# #### Barras simples (_bar plot_)
# 
# - A maneira mais direta de comparar esses números é plotando um gráfico de barras. 
# - Vamos testar a disposição vertical.

# In[5]:


import matplotlib.pyplot as plt
import seaborn as sb

fig, ax = plt.subplots(1,2,figsize=(12,3),constrained_layout=True)
g1 = sb.barplot(data=df_us,x='Filme',y='Bilheteria (M US$)',hue=None,ci=None,orient='v',ax=ax[0])
g2 = sb.barplot(data=df_br,x='Filme',y='Bilheteria (M US$)',hue=None,ci=None,orient='v',ax=ax[1])

g1.set_title('Top 10 do cinema 2022 - EUA')
g2.set_title('Top 10 do cinema 2022 - Brasil');


# - A pergunta é: quais são os filmes?! A identificação dos nomes dos filmes está prejudicada porque são legendas longas. 
# - Vamos testar com rotação.

# In[6]:


fig, ax = plt.subplots(1,2,figsize=(12,6),constrained_layout=True)
g1 = sb.barplot(data=df_us,x='Filme',y='Bilheteria (M US$)',hue=None,ci=None,orient='v',ax=ax[0])
g2 = sb.barplot(data=df_br,x='Filme',y='Bilheteria (M US$)',hue=None,ci=None,orient='v',ax=ax[1])

g1.set_title('Top 10 do cinema 2022 - EUA')
ax[0].tick_params(axis='x',rotation=90)
g2.set_title('Top 10 do cinema 2022 - Brasil')
ax[1].tick_params(axis='x',rotation=90);


# - O visual não parece bom porque os nomes ainda são difíceis de ler. 
# - Vamos tentar com barras horizontais.

# In[7]:


fig, ax = plt.subplots(1,2,figsize=(12,5),constrained_layout=True)
g1 = sb.barplot(data=df_us,y='Filme',x='Bilheteria (M US$)',hue=None,ci=None,orient='h',ax=ax[0])
g2 = sb.barplot(data=df_br,y='Filme',x='Bilheteria (M US$)',hue=None,ci=None,orient='h',ax=ax[1])

g1.set_title('Top 10 do cinema 2022 - EUA')
g2.set_title('Top 10 do cinema 2022 - Brasil');


# - Com as barras horizontais, os nomes dos filmes são melhor identificáveis. 
# - Melhorias a fazer no visual? 
# - Vamos discuti-las posteriormente.

# #### Barras agrupadas (_grouped bar plot_)
# 
# - Barras agrupadas são capazes de mostrar variação de quantidades em mais de uma categoria
# - No exemplo anterior, a categoria única era o nome dos filmes. 
# - Vamos criar um gráfico de barras agrupadas colocando lado a lado os filmes do TOP 10 internacional que também estiveram entre os TOP 10 do Brasil 
# - Criar categorização baseada na localização geográfica.

# - Primeiramente, vamos localizar os filmes intersectantes

# In[8]:


df_merge = pd.merge(df_us,df_br,how='inner',on='Filme'); 
df_merge


# - Vamos converter os valores das bilheterias em dólares para reais utilizando a taxa de câmbio PTAX 1:5.2171 (dezembro de 2022) e renomear as variáveis de dados.

# In[9]:


df_merge['Bilheteria - BR'] = df_merge['Bilheteria (M US$)_y']*5.2171
df_merge = df_merge.drop('Bilheteria (M US$)_y',axis=1)
df_merge['Bilheteria - US'] = df_merge['Bilheteria (M US$)_x']*5.2171
df_merge = df_merge.drop('Bilheteria (M US$)_x',axis=1)
df_merge


# - Em seguida, manipularemos os nossos dados para identificar cada filme e seu valor pela categoria "Local".

# In[10]:


# recria Dataframe para ter categoria 'Local'
s = []
for i in range(len(df_merge)):
    s.append( (df_merge['Filme'][i],df_merge['Bilheteria - US'][i],'US') )
    s.append( (df_merge['Filme'][i],df_merge['Bilheteria - BR'][i],'BR') )

f,v,p = [],[],[]
for si in s:
    f.append(si[0])
    v.append(si[1])
    p.append(si[2])

df_f = pd.DataFrame({'Filme':f,'Bilheteria':v,'Local':p})

# figura
g3 = sb.catplot(data=df_f, kind="bar", y='Filme', x='Bilheteria', hue='Local',orient='h')
g3.set_xlabels('Bilheteria (M R$)');


# #### Barras empilhadas (_stacked bar plot_)
# 
# - Barras empilhadas são adequadas para visualizar quantidades que produzem um total significativo a partir de parcelas que exibem, com clareza, suas proporções para este todo. 
# - Exemplo: 
#     - mostrar o peso das bilheterias dos filmes assistidos no Brasil/EUA
#     - cada barra representa a soma, em reais, angariada por cada filme nos dois países e cada segmento as parcelas desta soma por localidade
#     - interpretar resultados

# In[11]:


ax = sb.histplot(df_f,
    y='Filme', # use 'x' para vertical
    weights='Bilheteria', # pesos
    hue='Local',
    multiple='stack',
    #palette=['#aab1d1', '#ae24d1'], # paleta
    edgecolor='white',
    shrink=0.9 # fator de largura
)
ax.set_xlabel('Bilheteria (M R$)');


# ### Pontos (_dot plot_)
# 
# - Simplifica a escala representada visualmente por gráficos de barra. 
# - A posição do ponto marca a quantidade expressa no eixo correspondente. 
# - Na RV abaixo, utilizamos a mesma fonte de dados para plotar as áreas de uma amostra de 35 municípios. 
# - A escala logarítmica permite que tenhamos uma visão ampla da extensão em quilômetros quadrados por meio de potências de 10.

# In[12]:


from matplotlib.pyplot import subplots
from seaborn import set_palette, lineplot
from scipy.stats import zscore
from pandas import DataFrame
import cartopy.io.shapereader as shpreader

# recupera dados do shapefile
shp = shpreader.Reader('../data/PB_Municipios_2021/PB_Municipios_2021')
nmun = len(shp)
CD, NM, AREA = [], [], [] 
for rec in shp.records():
    CD.append(rec.attributes['CD_MUN'])
    NM.append(rec.attributes['NM_MUN'])
    AREA.append(rec.attributes['AREA_KM2'])
    
# converte dados de área para float e cálcula escore padronizado
df = DataFrame({'CD':CD,'NM':NM,'AREA':AREA})
df['AREA'] = df['AREA'].apply(lambda x: float(str(x).replace('.','')))
df = df.sort_values(by='AREA')

# amostra de municípios
df = df[50::5] 

# paleta de cores
set_palette("PiYG")

# figura
fig, ax = subplots(1,1,figsize=(2,6),constrained_layout=False)
f = lineplot(data=df,y='NM',x='AREA',marker='o',hue='AREA',markersize=7,linewidth=0,ax=ax)
f.set(xscale='log')
  
# decoração
ax.axis('tight'); 
ax.grid(axis='both',which='both',alpha=0.5,); 
ax.tick_params(axis='both', labelsize=6)
ax.set_xlim(7e4,1e6); 
ax.set_ylim(len(df)+0.1,-0.5)

ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.get_legend().remove()

ax.set_title('Área [km2]',fontsize=8)
ax.set_xlabel('Área',fontsize=8); 
ax.set_ylabel('Município - PB',fontsize=8);


# ### Mapas de calor (_heatmap_)
# 
# - Mapeiam valores em cores 
# - Exemplo: quantificação dde Crimes Violentos Letais Intencionais (CVLI) cometidos em João Pessoa entre 2015 e 2018 [Fonte](https://repositorio.ufpb.br/jspui/bitstream/123456789/16029/1/PMS09102019.pdf))
# - Constam nele a prevalência dos crimes além das tipologias de armas utilizadas entre 2015 e o primeiro semestre de 2019

# #### Prevalência
# 
# - Permite compreender o quanto é comum, ou rara, uma determinada ocorrência ou situação numa população. 
# 
# $$p = \dfrac{T}{P} \times 1000,$$
# 
# - $T$: quantidade de casos registrados de CVLI
# - $P$: população de um determinado bairro

# In[11]:


# dados do crime
dfc = pd.read_csv('../data/crimes-pb-2015-2018.csv'); 
dfc


# - Mapas de calor de coluna única:
#     - dados temporais originais agregam registros entre 2015 e 2018
#     - o primeiro mapa gera uma escala de cor sequencial para a prevalência
#     - o segundo mapa faz o mesmo para a quantidade de crimes realizados com arma de fogo 
# - Identificação dos bairros de maior/menor prevalência e de crimes com porte de arma de fogo

# In[12]:


dfc['Ano'] = ['2015-2018']*len(dfc)
dfc.sort_values('Prevalência',ascending=False)


# In[13]:


from pandas import pivot_table
from seaborn import heatmap,color_palette
from matplotlib.pyplot import subplots


dfp = pivot_table(dfc, index='Bairros', columns='Ano', values='Prevalência')
dfp = dfp.sort_values('2015-2018',ascending=False)

dfaf = pivot_table(dfc, index='Bairros', columns='Ano', values='Arma de fogo')
dfaf = dfaf.sort_values('2015-2018',ascending=False)

fig,ax = subplots(1,2,figsize=(8,4),constrained_layout=True)
fig.suptitle('Mapa de calor de crimes violentos em João Pessoa')


crime_p = heatmap(data=dfp,cmap=color_palette("YlOrRd"),annot=True,ax=ax[0])
crime_p.set_title('Prevalência',fontsize=10)
crime_p.set_yticklabels(crime_p.get_yticklabels(), fontsize = 8)
crime_p.set_xlim(0,1)

crime_af = heatmap(data=dfaf,cmap=color_palette("Oranges"),annot=True,fmt='d',ax=ax[1])
crime_af.set_title('Arma de fogo',fontsize=10)
crime_af.set_ylabel('')
crime_af.set_yticklabels(crime_af.get_yticklabels(), fontsize = 8);
crime_af.set_xlim(0,1);


# ## _Plots_ para visualizar distribuições
# 
# - Estatística descritiva limitada para resumir dados (dados com características completamente distintas podem ter os mesmos valores para média, mediana e variância, por exemplo)
# - Forma aprofundada de reconhecer as características dos dados é inspecionar a sua _distribuição_

# - No grupo das distribuições, consideraremos os seguintes _plots_:
#     - **histogramas**, com intervalo de classes uniforme;
#     - **densidades**, incluindo _densidade simples_;
#     - **cumulativos**, incluindo _densidade cumulativa empírica_;
#     - **quantis**, abrangendo o quantil-quantil (QQ-plot);

# - Exemplo: 
#     - Análise de processo de moldagem em uma linha de produção de uma indústria química do Rio Grande do Sul. 
#     - Propósito da análise: investigar inconsistências do processo. 
#     - Tabela registra massas de amostras extraídas de duas matrizes (2 e 7) ao longo de três dias a cada 30 minutos no período compreendido entre 07:00h e 13:00h
#     
# **Fonte**: Saldanha et al. _Analisando a aplicação do controle estatístico de processos na indústria química: um estudo de caso_. Espacios (Caracas), 34:1–18, 2013.

# In[14]:


from IPython.display import display, Markdown

# leitura
df_mq = pd.read_csv('../data/matriz-quimica.csv')
df_mq
# display
#display(Markdown(df_mq.to_markdown(index=False)))


# ### Histograma
# 
# - RV mais comumemente empregada para retratar distribuições. 
# - Gráfico de frequências de observação em _intervalos de classe_. 
# 
# - Exemplo: 
#     - Histogramas para as massas dos produtos processados em cada uma das matrizes. 
#     - Valores registrados ao longo dos 3 dias. 
#     - _Lacunas_ nos histogramas! Por quê?

# In[15]:


from seaborn import histplot
from matplotlib.pyplot import subplots

df_mq2 = df_mq[df_mq['Matriz'] == 2]
df_mq7 = df_mq[df_mq['Matriz'] == 7]

fig,ax = subplots(1,2,figsize=(8,2),constrained_layout=True,sharey=True)
fig.suptitle('Amostragem: Dias 1 a 3')
ax[0].set_ylabel('contagem')
ax[0].set_title('Matriz 2',fontsize=9)
ax[1].set_title('Matriz 7',fontsize=9)

hq_2 = histplot(data=df_mq2,x='Peso (g)',stat='count',binwidth=0.1,ax=ax[0],color='#ff8800')
hq_7 = histplot(data=df_mq7,x='Peso (g)',stat='count',binwidth=0.1,ax=ax[1])


# ### Densidade simples
# 
# - Versões contínuas dos histogramas
# - A frequência das quantidades é representada por uma curva suave que aproxima a distribuição de probabilidade fundamental 
# - A DBF explica o comportamento real (**desconhecido**)

# #### KDE
# 
# - Estimativa da curva de densidade por _kernel density estimator_ (_KDE_)
# - Recompõe a curva contínua através da mistura (combinação) de várias funções conhecidas 
# - São "núcleos" (_kernels_) em torno de cada ponto amostrado dentro de uma _largura de banda_ predefinida. 
# - Diversos tipos de _kernel_ (_exponencial_, _linear_, _epanechnikov_ e o mais popular,  _gaussiano_)
# - Exemplo: 
#     - plotagens da densidade de distribuição para cada matriz da indústria
#     - o último _plot_ contém as duas distribuições
#     - vê-se que a curva "imita" o comportamento já visualizado no gráfico 

# In[22]:


from seaborn import kdeplot

fig,ax = subplots(1,3,figsize=(8,2),constrained_layout=True,sharey=True)
fig.suptitle('Amostragem: Dias 1 a 3')
ax[0].set_ylabel('densidade (KDE)')
ax[0].set_title('Matriz 2',fontsize=9)
ax[1].set_title('Matriz 7',fontsize=9)
ax[2].set_title('Matrizes 2 e 7',fontsize=9)

bw=.8
hq_2 = kdeplot(data=df_mq2,x='Peso (g)',fill=True,ax=ax[0],bw_adjust=bw,color='#ff8800',label=f'larg. banda={bw}')
hq_2.legend(fontsize=6,loc='upper left')

bw2=0.7
hq_7 = kdeplot(data=df_mq7,x='Peso (g)',fill=True,ax=ax[1],bw_adjust=bw2,label=f'larg. banda={bw2}')
hq_7.legend(fontsize=6,loc='upper left')

kdeplot(data=df_mq2,x='Peso (g)',fill=True,ax=ax[2],bw_adjust=bw,color='#ff8800',label=f'larg. banda={bw}')
kdeplot(data=df_mq7,x='Peso (g)',fill=True,ax=ax[2],bw_adjust=bw,label=f'larg. banda={bw}');


# - No próximo exemplo, plotamos os histogramas juntamente com a curva estimada por _KDE_

# In[24]:


fig,ax = subplots(1,2,figsize=(8,2),constrained_layout=True,sharey=True)
fig.suptitle('Amostragem: Dias 1 a 3')
ax[0].set_ylabel('probabilidade')
ax[0].set_title('Matriz 2',fontsize=9)
ax[1].set_title('Matriz 7',fontsize=9)

hq_2 = histplot(data=df_mq2,x='Peso (g)',kde=True,stat='probability',binwidth=0.1,ax=ax[0],color='#ff8800')
hq_7 = histplot(data=df_mq7,x='Peso (g)',kde=True,stat='probability',binwidth=0.1,ax=ax[1])


# ### Densidade cumulativa
# 
# - Histogramas e _plots de densidade_ possuem o revés de dependerem de parâmetros que são escolhidos pelo usuário (_bins_, _bandwidth_). 
# - Podem ser livremente alterados
# - Desvantagem: eles são menos intuitivos.
# - _Plots_ de densidade simplesmente mostram os dados de uma só vez, sem uso de parâmetros.
# - Entender _densidade cumulativa_, ou _densidade cumulativa empírica_ (ECDF), 
# - Exemplo: 
#     - Notas auferidas por estudantes de uma classe de Engenharia formada por 60 pessoas na primeira avaliação

# In[25]:


df_est = pd.read_csv('../data/estudantes-notas.csv')

df_est      

# display
#display(Markdown(df_est.to_markdown(index=False)))


# - A distribuição cumulativa é uma RV que fornece dois caminhos de compreensão para os dados quantitativos em análise. 
#     1. Ponto de vista de contagem. Neste caso particular, a nota de cada estudante é disposta no eixo horizontal, enquanto que no eixo vertical consta um "ranqueamento ascendente" de estudantes. A curva cresce cumulativamente daquele(a) estudante que possui a nota mais baixa (ranqueamento 1) até o(a) estudante que possui a maior nota (ranqueamento 60).
# 
#     2. Sob o ponto de vista de proporção. Neste caso particular, a nota de cada estudante é disposta no eixo horizontal, enquanto que no eixo vertical consta a proporção de estudantes que atingiram determinada nota. A curva é idêntica, mas podemos verificar rapidamente o ranqueamento por percentuais. Por exemplo, o gráfico mostra que em torno de 25% da turma conseguiu nota, no máximo de 6,0.

# In[19]:


from seaborn import ecdfplot


fig,ax = subplots(1,2,figsize=(8,3),constrained_layout=True)
fig.suptitle('Distribuição cumulativa de notas da turma',fontsize=10)
ax[0].set_ylabel('ranqueamento (ascendente)',fontsize=9)
ax[0].set_title('ECDF por contagem',fontsize=9)

ax[1].set_ylabel('ranqueamento normalizado',fontsize=9)
ax[1].grid(axis='y')
ax[1].set_title('ECDF por proporção',fontsize=9)
fe1 = ecdfplot(data=df_est,x='Nota',stat='count',ax=ax[0])
fe2 = ecdfplot(data=df_est,x='Nota',stat='proportion',ax=ax[1])


# ### Quantis
# 
# - Espécie de "ranqueamento" dos dados. 
# - Divididos em frações de 100: percentis. 
# - Exemplo: jogador de futebol avaliado estatisticamete com percentil de 86% (14% melhores) 

# #### QQ plot
# 
# - _Plot_ chamado de quantil-quantil é bastante utilizado para testar se os dados observados seguem uma determinada distribuição teórica
# - Quando a distribuição teórica é a _normal_, chamamos o gráfico de _plot de probabilidades normal_ (veja também similaridades com o _plot de probabilidades_, PP-_plot_)
# - QQ-_plot_ é um plot de pontos geralmente com reta de referência
# - Para QQ-plots, deveremos instalar o módulo `seaborn-qqplot`

# In[20]:


from seaborn_qqplot import pplot
from numpy import random

random.seed(10)
dnormal = random.normal(df_est['Nota'].mean(),df_est['Nota'].std(ddof=1),len(df_est))
df_est['Nota teórica'] = dnormal

qq = pplot(data=df_est, x='Nota teórica',y='Nota',
           kind='qq',
           height=3, 
           aspect=1.5,
           display_kws={"identity":True})


# ## _Plots_ para visualizar proporções
# 
# - RVs de proporções devem levar em conta projetos gráficos que sejam capazes de mostrar como algum grupo, entidade ou quantidade pode ser "quebrada" em partes menores, 
# - Constituindo uma proporção do todo 
# - Classicamente, o gráfico de "torta" (_pie chart_) é o mais tradicionalmente aplicado quando o interesse é visualizar proporções
# - Mais genéricos (mosaicos, árvores estruturadas (_treemap_), diagramas de Venn, _donut_, dendrogramas e raios de sol (_sunburst_)

# ### Barras
# 
# - Visualizar proporções do sistema de vinhos e bebidas [SIVIBE/MAPA](https://mapa-indicadores.agricultura.gov.br/publico/extensions/SIVIBE/SIVIBE.html)
# 
# - Nota: para operacionalizar planilhas do Excel, poderá ser necessária a instalação do módulo `openpyxl`.

# In[21]:


from pandas import read_excel
from matplotlib.pyplot import subplots

df_parr = read_excel('../data/area-parreiral-uvas-sivibe.xlsx')
df_parr = df_parr.drop(df_parr[df_parr['Classificação'] == '-'].index).reset_index(drop=True)
df_parr


# In[22]:


df_parr_grp = df_parr.groupby('Classificação').sum()
df_parr_grp['Código propriedade'] = 'Parreiral'
df_parr_grp = df_parr_grp.sort_values(by='Área Parreiral (calc) ha',ascending=False)

fig,ax = subplots(1,1,figsize=(8,1.5),constrained_layout=True)

vin = sb.histplot(df_parr_grp,
    y='Código propriedade', # use 'x' para vertical
    weights='Área Parreiral (calc) ha', # pesos
    hue='Classificação',
    multiple='stack',
    palette=color_palette('magma',4),
    edgecolor='white',
    shrink=0.9, # fator de largura
    ax = ax)

vin.set_xlabel('Hectare (ha)');
vin.set_ylabel('');

sb.move_legend(vin,"upper right",ncol=4,frameon=False,bbox_to_anchor=(.8,1.7),fontsize=8)
sb.despine(ax=ax); ax.spines['left'].set_visible(False)


# ### Fatias

# In[23]:


labels = df_parr_grp.index.to_list()
sizes = df_parr_grp['Área Parreiral (calc) ha']/df_parr_grp['Área Parreiral (calc) ha'].max()*100

fig,ax = subplots(1,1,figsize=(4,4),constrained_layout=True)
explode = (0,0,0,0)
ax.pie(sizes,explode=explode,labels=labels,autopct='%.2f%%',startangle=90)
ax.axis('equal')
ax.set_title('Produção por classificação');


# ### Diagrama de Venn

# - Comparativo de um grupo de artistas que apenas cantam, apenas atuam ou cantam e atuam

# In[24]:


from matplotlib.pyplot import subplots
from matplotlib_venn import venn2

df_arts = pd.read_csv('../data/cantores-atores.csv')
df_arts


# - Para plotar diagramas de Venn, é necessário instalar o módulo `matplotlib_venn` (use `pip`). 

# In[25]:


sn = df_arts[(df_arts['Canta'] == 'sim') & (df_arts['Atua'] == 'não')]
ss = df_arts[(df_arts['Canta'] == 'sim') & (df_arts['Atua'] == 'sim')]
ns = df_arts[(df_arts['Canta'] == 'não') & (df_arts['Atua'] == 'sim')]

venn2(subsets=(len(sn),len(ss),len(ns)),
       set_labels=('Apenas canta','Apenas atua'));


# ### Árvore estruturada
# 
# - O diagrama de árvore estruturada (_treemap_) permite seccionar um todo em áreas representativas, como mostramos na apresentação deste curso (_treemap_)

# In[26]:


import plotly.graph_objects as go
from plotly.offline import plot
from IPython.display import display, HTML

labels = ['Visualização de Dados',
    'Módulo 1','Módulo 2','Módulo 3',
    'Conteúdo 1','Estudo de caso 1',
    'Conteúdo 2','Estudo de caso 2',
    'Conteúdo 3','Relatório Final']

parents = [''] +     3*['Visualização de Dados'] +     2*['Módulo 1'] +     2*['Módulo 2'] +     2*['Módulo 3'] 

values = [0] +     [.33,.33,.33] +     [.9,.1,.9,.1] +     [.7,.3]

f = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Greens'
))

f.update_layout(margin=dict(t=50, l=25, r=25, b=25))
plot(f, show_link=False,filename='course-treemap.html')
display(HTML('course-treemap.html'))


# ## _Plots_ para visualizar correlações
# 
# - Correlação é qualquer associação estatística entre um par de variáveis
# - Quanto mais correlacionadas estão duas variáveis, mais "alinhamento" há entre elas. 
# - Podemos interpretar a _correlação_ também pelo ponto de vista de "dependência linear". 
# 
# - Divisão enfática dos tipos de representações dada a sua variedade. 
#     - dispersão (_scatter plot_), bolhas (_bubble chart_), inclinação (_slopegraph_), linhas;
#     - contornos de densidade, classes 2D (_2D bins_), classes hexagonais (_hex bins_);
#     - correlograma.

# - Para grandes dados, plots de dispersão tornam-se pouco informativos devido ao emaranhado de pontos. 
# - Em um cenário como este, são preferíveis os _plots_ de contornos e classes. Para mais do que duas quantidades, correlogramas são recomendados.
# - Discutiremos apenas alguns exemplos.

# ### Dispersão
# 
# - Dispersão existente entre dois métodos que explicam o [crescimento fetal em função da semana gestacional](https://perinatology.com/calculators/Estimation%20of%20Fetal%20Weight%20and%20Age.htm). 
# - O gráfico à esquerda mostra a curva de Hadlock e de Duryea, ambas para o percentil 10. 
# - À direita, plotamos o gráfico de dispersão entre ambas as curvas para saber como elas se correlacionam. 
# - A existência de uma "barriga" abaixo da linha pontilhada mostra que elas, de fato, são diferentes

# In[27]:


from matplotlib import style
from matplotlib.pyplot import plot, subplots
from pandas import read_csv

df = read_csv('../data/gestacional-peso.csv')
X = df['week']
Y1 = df['hadlock-10th']
Y2 = df['duryea-10th']

fig,ax = subplots(1,2,figsize=(6,3),sharey=True,constrained_layout=True)
fig.suptitle('Correlações EFW')

ax[0].grid()
ax[0].plot(X,Y1,'-',c='#8EB353',label='Hadlock-10th')
ax[0].plot(X,Y2,'-',c='#BFDF53',label='Duryea-10th')
ax[0].set_xlabel('Semana gestacional')
ax[0].set_ylabel('Peso (g)')
ax[0].legend()

ax[1].grid()
ax[1].plot(Y1,Y1,'--',c='k',alpha=0.5)
ax[1].plot(Y1,Y2,'o',c='#117029')
ax[1].axis('equal')
ax[1].set_xlabel('Hadlock - 10th')
ax[1].set_ylabel('Duryea - 10th');


# ## _Plots_ para visualizar dados geoespaciais
# 
# - Dados geoespaciais são melhor dispostos através de mapas que projetam coordenadas do globo terrestre em superfícies planas
# - Geralmente, os mapas seguem o formato e as fronteiras de territórios
#     - coropletas, ou mapas coropléticos (_choropleth_), que colorem regiões do mapa para realizar associações com quantidades ou categorias
#     - cartogramas, que se constituem em representações distorcidas ou simplificadas das regiões. 
#         - Exemplo, associar estados da federação a formas retangulares menores arranjadas sobre uma forma poligonal maior próxima ao formato do Brasil.

# ## _Plots_ para visualizar incertezas
# 
# - Incertezas surgem de: 
#     - medições experimentais e laboratoriais
#     - cálculos que envolvem estimativas e previsões sobre ocorrências futuras. 
# - São representadas por barras ou áreas que se estendem em torno de um ponto ou linha de referência. 
# - Neste grupo, incluem-se os plots acompanhados de barras de erro e de intervalos de confiança

# In[28]:


import numpy as np
from matplotlib.pyplot import subplots

d_opts = {
    'Standard Deviation':'sd', # parametric / spread
    'Standard Error':'se', # parametric / uncertainty
    'Percentile Interval':'pi', # nonparametric / spread
    'Confidence Interval':'ci', # nonparametric / uncertainty
}

def plot_eb(eb, **kws):
    np.random.seed(100)
    x = np.random.normal(0, 1, 100)
    f, ax = subplots(figsize=(4, 2), sharex=True, layout="tight")
    sb.pointplot(data=df_parr,x='Classificação',y='Área Parreiral (calc) ha',
                 errorbar=eb, **kws, capsize=.2, ax=ax)


# In[29]:


for k,v in d_opts.items():
    plot_eb(v,color="#14d377")


# In[30]:


from matplotlib.pyplot import plot, fill_between
from numpy import std, sin


f, axs = subplots(figsize=(4, 2), sharex=True, layout="tight")
Y1m, Y1M = Y1u = Y1 - std(Y1), Y1 + std(Y1)
plot(X, Y1)
fill_between(X, Y1m, Y1M, alpha=.2)
plot(X, Y1 + (Y1M - Y1m)*np.random.normal(0, 0.2, len(X)),'o',mfc='w');

