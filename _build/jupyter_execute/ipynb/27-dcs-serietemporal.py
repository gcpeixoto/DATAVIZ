#!/usr/bin/env python
# coding: utf-8

# # _Dataviz Code Session_: Séries Temporais

# ## Objetivos da DCS
# 
# - Aplicar técnicas de dataviz para plotagem e manipulação de séries temporais;
# - Manipular séries temporais (STs) relativas a dados de repasses da arrecadação federal efetivados pela Secretaria Especial da Receita Federal do Brasil a outras entidades e fundos;
# - Produzir representações visuais de STs e suas componentes fundamentais (tendência, sazonalidade e ruído);

# ## Ferramentas utilizadas
# 
# - Módulos Python
#     - `pandas`
#     - `sys`
#     - `matplotlib`
#     - `seaborn`
#     - `statsmodels`
#     - `numpy`

# ## Aplicação do modelo referencial
# 
# - Vide {numref}`Capítulo %s <cap:estetica>`.

# In[1]:


from matplotlib.patches import Patch
from statsmodels.tsa.seasonal import seasonal_decompose

import pandas as pd, matplotlib.pyplot as plt, seaborn as sb, numpy as np
import sys; sys.path.insert(1,'../dcs')
import dcs27

plt.style.use('../etc/gcpeixoto-datavis.mplstyle') # style sheet


# ## Dados de entrada pré-processados

# In[2]:


# carrega dados da RFB
df = dcs27.load_data(keep_orig=False,show_links=False)


# ### Processamento adicional

# - Listagem de entidades disponíveis para análise

# In[3]:


# lista de entidades disponíveis
df['Entidade'].unique()


# - Escolha de entidade e filtragem

# In[4]:


entity = 'INCRA'
df_e = df[df['Entidade'] == entity].reset_index(drop=True)


# ## Mapeamento
# 
# - Criação de _string_ representativa de temporalidade;
# - Conversão de _string_ para objeto `datetime`;
# - Plotagem direta de curvas em eixos cartesianos;
#     - Frequência mensal;
#     - Frequência anual;

# - Montagem de _string_ representativa da temporalidade (período)

# In[5]:


df_e['Período'] = pd.Series([v['Mês'] + '/' + v['Ano'] for i,v in df_e.iterrows()])


# - Plotagem simples
#     - Eixo emaranhado;
#     - Falta de controle de espaçamento;

# In[6]:


fig, ax = plt.subplots(figsize=(12,3),constrained_layout=True)
s1 = sb.lineplot(data=df_e,x='Período',y='Total Repassado',errorbar=None,ax=ax)
ax.tick_params(axis='x', rotation=90, labelsize = 8)


# - Transformação para objeto `datetime`

# In[7]:


# ver função 'map_my' auxiliar
df_e['Período'] = pd.to_datetime(df_e['Período'].apply(lambda x: dcs27.map_my(x)))


# ## Visualização

# ### Iterando em RVs primárias
# 
# - Plotagem com eixo automaticamente controlado
#     - Exploração de `seaborn.lineplot`
# - Quadro de STs (frequência mensal)

# In[8]:


fig, ax = plt.subplots(figsize=(12,3),constrained_layout=True)
s1 = sb.lineplot(data=df_e,
                 x='Período', y='Total Repassado',
                 color=plt.rcParams['axes.edgecolor'], # cor do estilo customizado
                 errorbar=None, ax=ax)
ax.set_title(f'Série histórica: repasse RFB para {entity}',fontsize=14);


# - Plotagem de séries por frequência mensal

# In[9]:


df_em = df_e.set_index('Ano')


# In[10]:


fig, ax = plt.subplots(figsize=(12,3),constrained_layout=True)

# paleta de cores
pal = sb.color_palette('Oranges',len(df_em.index.unique()))

# 
for i,y in enumerate(df_em.index.unique()):
    sy = sb.lineplot(data=df_em,
                     x=df_em.loc[y]['Mês'],
                     y=df_em.loc[y]['Total Repassado'],
                     marker='o',
                     color=pal[i],
                     errorbar=None, ax=ax, label=y)

ax.legend(loc='best', bbox_to_anchor=(1.1,1.1), title='Ano')
ax.grid(axis='x')
ax.set_title(f'Série histórica (mensal): repasse RFB para {entity}',fontsize=14);


# - Identificação de componentes
# 
# **Nota 1**: STs podem ou não apresentar padrões. Padrões comuns são: i) tendência (comportamento monotônico); ii) sazonalidade (comportamento alternado devido a fatores sazonais); iii) híbrido (comportamento que apresenta tendências e efeitos sazonais combinados).
# 
# **Nota 2**: uma ST pode ser [descrita](https://cmapskm.ihmc.us/rid=1052458821502_1749267941_6906/components.pdf) por uma soma ou um produto de componentes:
# 
# - `statsmodels.tsa.seasonal_decompose` reproduz a ST observada e outras 3 componentes.

# - ST aditiva: _valor = tendência + ciclo + sazonalidade + irregularidade_

# In[11]:


# componentes por modelo aditivo
df_add = seasonal_decompose(x=df_em.set_index('Período')['Total Repassado'], 
                            model='additive', 
                            extrapolate_trend='freq')

# figura
fig, ax = plt.subplots(4,1,figsize=(6,4),sharex=True,constrained_layout=True)

# plotagem das componentes
ax[0].plot(df_add.observed,color=pal[2])
ax[1].plot(df_add.trend,color=pal[4])
ax[2].plot(df_add.seasonal,color=pal[6])
ax[3].plot(df_add.resid,'o',color=pal[8])

# decoração
ax[0].set_title('Série temporal observada',fontsize=10)
ax[1].set_title('Componente: tendência',fontsize=10)
ax[2].set_title('Componente: sazonalidade',fontsize=10)
ax[3].set_title('Componente: irregularidade',fontsize=10)
ax[3].set_xlabel('Período',fontsize=10)
fig.suptitle('Componentes da ST: modelo aditivo');


# - ST multiplicativa: _valor = tendência x ciclo x sazonalidade x irregularidade_

# In[12]:


# componentes por modelo multiplicativo
df_mul = seasonal_decompose(x=df_em.set_index('Período')['Total Repassado'], 
                            model='multiplicative', 
                            extrapolate_trend='freq')

# figura
fig, ax = plt.subplots(4,1,figsize=(6,4),sharex=True,constrained_layout=True)

# plotagem das componentes
ax[0].plot(df_mul.observed,color=pal[2])
ax[1].plot(df_mul.trend,color=pal[4])
ax[2].plot(df_mul.seasonal,color=pal[6])
ax[3].plot(df_mul.resid,'o',color=pal[8])

# decoração
ax[0].set_title('Série temporal observada',fontsize=10)
ax[1].set_title('Componente: tendência',fontsize=10)
ax[2].set_title('Componente: sazonalidade',fontsize=10)
ax[3].set_title('Componente: irregularidade',fontsize=10)
ax[3].set_xlabel('Período',fontsize=10)
fig.suptitle('Componentes da ST: modelo multiplicativo');


# - Mecanismo de plotagem direta

# In[13]:


dp = df_add.plot()


# ## RV finalística
# 
# - Define função para plotar ST(s) específica(s) com alguma decoração.

# In[14]:


# entidades do sistema S
S = ['SENAI', 'SESI', 'SENAC']

fig, ax = plt.subplots(figsize=(12,3),constrained_layout=True)

# plotagens individuais
for i,s in enumerate(S):
    s1 = dcs27.plot_ts_rfb(df,s,ax,pal[i+3]) # função auxiliar

ax.set_title(f'Série histórica: repasses anuais da RFB para entidades do Sistema S',fontsize=14);

