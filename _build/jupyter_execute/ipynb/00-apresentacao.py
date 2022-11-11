#!/usr/bin/env python
# coding: utf-8

# # Apresentação do curso
# 
# ## Objetivos

# ## Estrutura
# 
# O curso é composto de 3 módulos subdivididos em duas partes, conteúdo e avaliação, segundo a seguinte estrutura:
# 
# - Módulo 1 (20h)
#     - Conteúdo (18h)
#     - Avaliação: Estudo de caso 1 (2h)
# - Módulo 2 (20h)
#     - Conteúdo (18h)
#     - Avaliação: Estudo de caso 2 (2h)
# - Módulo 3 (20h)
#     - Conteúdo (14h)
#     - Avaliação: Estudo de caso 2 (6h)
# 
# A divisão geral acima pode ser visualizada graficamente pelo _treemap_ abaixo.

# In[35]:


import plotly.graph_objects as go
from plotly.offline import plot
from IPython.display import display, HTML

labels = ['Visualização de Dados',
    'Módulo 1','Módulo 2','Módulo 3',
    'Conteúdo 1','Estudo de caso 1',
    'Conteúdo 2','Estudo de caso 2',
    'Conteúdo 3','Relatório Final']

parents = [''] +     3*['Visualização de Dados'] +     2*['Módulo 1'] +     2*['Módulo 2'] +     2*['Módulo 3'] 

values = [0] +     [.3,.3,.4] +     [.9,.1,.9,.1] +     [.7,.3]

f = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Greens'
))

f.update_layout(margin=dict(t=50, l=25, r=25, b=25))
plot(f, show_link=False,filename='course-treemap.html')
display(HTML('course-treemap.html'))


# ## Conteúdo 
# 
# 
# 
# ### Módulo 1: Fundamentos (20h)
# 
# - Conteúdo (18h)
#     - Apresentação do curso (1h)
#     - [História da Visualização de Dados](01-historia.ipynb) (1h)
# - Avaliação (2h)
#     - Relatório de estudo de caso 1 (2h)
# 
# <!--
# ### Módulo 2: Técnicas (20h)
# 
# - Conteúdo (18h)
#     - 
#     - 
# - Avaliação (2h)
#     - Relatório de estudo de caso 2 (2h)
# 
# ### Módulo 3: Aplicações (20h)
# 
# - Conteúdo (14h)
#     - 
#     - 
# - Avaliação (6h)
#     - Relatório Final (6h)
# -->

# ## Metodologia de avaliação

# 
# A metodologia de avaliação será guiada pela <a href="https://github.com/gcpeixoto/DATAVIZ/blob/main/assess/criterio-notas.pdf" download="https://github.com/gcpeixoto/DATAVIZ/blob/main/assess/criterio-notas.pdf"> Rubrica de Avaliação</a>.
# 
# ### Templates 
# 
# Para elaborar os mini-artigos avaliativos, pode-se usar o template em formato _.ODT_ disponibilizado <a href="https://github.com/gcpeixoto/DATAVIZ/blob/main/templates/short-paper/odt/main.odt" download="https://github.com/gcpeixoto/DATAVIZ/blob/main/templates/short-paper/odt/main.odt"> aqui</a>, ou, preferencialmente, o uso do template _.TEX_ disponibilizado <a href="https://github.com/gcpeixoto/DATAVIZ/tree/main/templates/short-paper/tex"> aqui</a>.
# 
# ### Projeto final
# 
# O relatório de projeto final deve ser enviado em formato _.PDF_ utilizando como base o [Modelo de Relatório Final](capstone-template.ipynb).
# 
# ### Atribuição de notas
# 
# - Notas dos módulos 1 ($N_1$) e 2 ($N_2$): média aritmética das notas dos elementos de avaliação do módulo.
#   
# - Nota do módulo 3 ($N_3$): nota do projeto final
# 
# - Nota final: $0,3N_1 + 0,3N_2 + 0,4N_3$
