#!/usr/bin/env python
# coding: utf-8

# # Guia rápido de plotagem - `seaborn`
# 
# - Base de construção: `matplotlib`
# - Integração de dados: `pandas`

# ## Receita de bolo
# 
# 1. importar pacote
# 2. escolher tema
# 3. carregar dataset
# 4. criar plot

# In[35]:


# passo 1
import matplotlib.pyplot as plt, pandas as pd, seaborn as sns

# passo 2
sns.set_theme() # default

# passo 3
df = pd.read_csv('../data/preco-combs-pb-2022-02.csv')
bay_etanol = df[ (df['Municipio'] == 'BAYEUX') & (df['Produto'] == 'ETANOL')]

# passo 4
fig, ax = plt.subplots(figsize=(7,2))
f = sns.barplot(x='Bandeira',y='Valor de Venda',data=bay_etanol,palette="Paired");


# ## Classes de funções de plotagem
# 
# São de dois tipos:
# 
# - Funções em nível de figura (FNF): criam interface com matplotlib (retorna `seaborn.axisgrid.FacetGrid` ou `seaborn.axisgrid.PairGrid` (mosaico) ou `seaborn.axisgrid.JointGrid` (bivariados));
# - Funções em nível de eixo (FNE): plotam dados em eixo único (retorna `matplotlib.pyplot.Axes`)
# 
# Organização de plots:
# 
# - **Correlação**
#     - FNF:
#         - `relplot` - interface para FNEs com `kind` = `scatter` | `line` 
#     - FNEs:
#         - `scatterplot` - dispersão
#         - `lineplot` - linhas gerais
# - **Distribuição**
#     - FNF:
#         - `displot` - interface para FNEs com `kind` = `hist` | `kde` | `ecdf` 
#     - FNEs:
#         - `histplot` - histogramas
#         - `kdeplot` - densidade por curva de kernel
#         - `ecdfplot` - distribuição cumulativa empírica
#     - FNE complementar:    
#         - `rugplot` - densidade por traços no eixo (adicionável ao plot das demais)
# - **Categoria**
#     - FNF:
#         - `catplot` - interface para FNEs com `kind` = `strip` | `swarm` | `box` | `violin` | `boxen` | `point` | `bar` | `count` 
#     - FNEs para dispersão:
#         - `stripplot` - dispersão com _jitter_ (tremor)
#         - `swarmplot` - dispersão sem sobreposição de pontos
#     - FNEs para distribuição
#         - `boxplot` - quartis e outliers em "caixa"
#         - `violinplot` - KDE em forma de "violino"
#         - `boxenplot` - aperfeiçoamento do boxplot para grandes dados
#     - FNEs para estimação:
#         - `pointplot` - pontos com _errorbar_
#         - `barplot` - barras com _errorbar_
#         - `countplot` - histograma para dados categóricos
# - **Regressão**:
#     - FNF:
#         - `lmplot` - regressão linear: combina `regplot` e `FacetGrid`
#     - FNE:
#         - `regplot` - regressão linear
#         - `residplot` - resíduos de regressão         
# - **Outras**:
#     - `heatmap` - mapa de calor
#     - `clustermap` - matriz com clusterização hierárquica
#     - `pairplot` - interface mosaico para visualização de pareamentos
#     - `jointplot` - plot bivariado genérico para mistura de pareamentos 
