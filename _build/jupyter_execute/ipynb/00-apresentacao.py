#!/usr/bin/env python
# coding: utf-8

# # Apresentação do curso
# 
# Este curso integra o rol obrigatório do Bacharelado em Ciência de Dados e Inteligência Artificial da Universidade Fedaral da Paraíba.
# 
# ## Objetivos
# 
# - Elencar os marcos históricos de desenvolvimento da área denominada _visualização de dados_;
# - Reconhecer conceitos de representação visual, percepção, estética, cores e seus impactos ao observador;
# - Discutir técnicas diversas para representação visual de quantidades, proporções, tendências, redes e informações gerais, bem como de _storytelling_ e _business storytelling_;
# - Desenvolver códigos para visualização de dados multidimensionais e científicos;
# - Experimentar ferramentas e plataformas modernas para construção de painéis analíticos (_dashboards_) e geração de relatórios automatizados;
# - Propor soluções de _data reporting_ para cases de negócio aplicáveis aos diversos setores da economia. 

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
#     - Avaliação: Projeto de visualização (6h)
# 
# A divisão geral acima pode ser visualizada graficamente pelo _treemap_ abaixo, em que as áreas dos retângulo representam, proporcionalmente, a carga horária total de 60h dedicada ao curso.

# In[4]:


import plotly.graph_objects as go
from plotly.offline import plot
from IPython.display import display, HTML

labels = ['Visualização de Dados',
    'Módulo 1','Módulo 2','Módulo 3',
    'Conteúdo 1','Estudo de caso 1',
    'Conteúdo 2','Estudo de caso 2',
    'Conteúdo 3','Projeto de visualização']

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


# ## Conteúdo 
# 
# ### Módulo 1: Fundamentos (20h)
# 
# - Conteúdo (18h)
#     - [Introdução à Visualização de Dados](01a-introducao.ipynb) 
#     - [Marcos Históricos da Visualização de Dados](02a-historico.ipynb) 
#     - [Criação de Representações Visuais e Estética](03a-estetica.ipynb) 
#     - [Eixos, Escalas e Sistemas de Coordenadas](04a-eixos.ipynb) 
#     - [Percepção Visual](05a-percepcao.ipynb) 
#     - [Cores](06a-cores.ipynb)
#     - [_Lounge_ das Representações Visuais](07a-lounge.ipynb)
#     - [Técnicas de _Storytelling_](08a-storytelling.ipynb)
#     - [Imersão em _matplotlib_](09a-matplotlib-imersao.ipynb)
# - Avaliação (2h)
#     - [Estudo de Caso de Visualização de Dados (ECVD1)](10a-ecvd1.ipynb) (2h)
# 
# ### Módulo 2: Técnica (20h)
# 
# - Conteúdo (18h)
#     - _Dataviz Code Session_: Quantidades
#     - _Dataviz Code Session_: Distribuições
#     - _Dataviz Code Session_: Proporções
#     - _Dataviz Code Session_: Dados Geoespaciais
#     - [_Dataviz Code Session_: Dados Multidimensionais](24-dcs-multidimensional.ipynb)
#     - [_Dataviz Code Session_: Redes Complexas](25-dcs-redes.ipynb)
#     - [_Dataviz Code Session_: Visualização Científica](26-dcs-cientifica.ipynb)
#     - [_Dataviz Code Session_: Séries Temporais e Tendências](27-dcs-serietemporal.ipynb)
# 
# - Avaliação (2h)
#     - [Estudo de Caso de Visualização de Dados (ECVD2)](20a-ecvd2.ipynb) (2h)
# 
# ### Módulo 3: Aplicações (20h)
# 
# - Conteúdo (14h)
#     - _Dashboarding_ (6h)
#     - _Reporting_ (4h)
#     - _Business Intelligence_ (4h)
# 
# - Avaliação (6h)
#     - [Projeto Final de Visualização de Dados (PFVD)](capstone-template.ipynb) (6h)
# 
# ### Suplemento
# 
# - [Guia rápido de plotagem: _seaborn_ *](A-quick-guide-seaborn.ipynb)
# - [Guia rápido de plotagem: _matplotlib_ *](B-quick-guide-matplotlib.ipynb)
# 
# **Obs./(*):** capítulos não linkados estão em construção.

# ## Metodologia de avaliação

# 
# A metodologia de avaliação será guiada pela <a href="https://github.com/gcpeixoto/DATAVIZ/blob/main/assess/criterio-notas.pdf" download="https://github.com/gcpeixoto/DATAVIZ/blob/main/assess/criterio-notas.pdf"> Rubrica de Avaliação</a>, salvo adaptações pontuais e previamente informadas.
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

# ## Autoria
# 
# Este material é desenvolvido e mantido pelo Prof. Gustavo Oliveira (DCC/CI/UFPB). Acesse a página pessoal pelo link:
# 
# - [Website pessoal](http://gcpeixoto.github.io/)
# 
# Para saber sobre demais ações em ensino e pesquisa, projetos e oportunidades, consulte o site do grupo de pesquisa em Engenharia Computacional pelo link: 
# 
# - [TRIL Lab](http://tril.ci.ufpb.br)
# 
# 
# <hr>

# ## Outros livros e apostilas do professor
# 
# ### Grupo 1
# - [Fundamentos de Matemática e Estatística para Ciência de Dados](https://gcpeixoto.github.io/FMECD/ipynb/00-apresentacao.html), com Andrea Rocha (UFPB)
#     - Curso elementar para alunos de primeiro ano em áreas afins à Matemática, Estatística e Ciência de Dados que buscam aprimorar conhecimentos do ensino médio e desenvolvê-los sob a ótica computacional.
# 
# - [Introdução à Ciência de Dados](https://gcpeixoto.github.io/ICD)
#     - Curso para alunos do primeiro período de CDIA/UFPB contendo uma visão geral sobre os principais temas abordados ao longo do curso.
# 
# ### Grupo 2
# - [Introdução a Python para Ciências Computacionais e Engenharia](https://gcpeixoto.github.io/lecture-ipynb/indice.html), traduzido de Hans Fanghor (Southampton/UK)
#     - Apostila suplementar de aprendizagem de linguagem Python para alunos de cursos de ciências exatas, com ênfase em aplicações de engenharia.
# 
# - [Laboratório Virtual de Métodos Numéricos](https://gcpeixoto.github.io/ipynb-lab-metodos-numericos/conteudo.html)
#     - Laboratório de aplicações computacionais diversas para suporte a cursos de cálculo numérico, ou métodos numéricos, aplicável a todos os nichos de exatas. Contém miscelânea de estudos de caso, códigos práticos e materiais de consulta.
# 
# - [Métodos Computacionais](https://gcpeixoto.github.io/METCOMP/)
#     - Curso elaborado para atendimento a estudantes do primeiro ano de Engenharia de Produção, com conteúdo misto herdado dos cursos básicos dos Grupos 1 e 2. Diferencia por adentrar em conceitos particulares de álgebra linear e otimização.
