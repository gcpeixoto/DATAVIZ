#!/usr/bin/env python
# coding: utf-8

# # Apresentação
# 
# Este repositório digital concentra o material relativo à componente curricular _Visualização de Dados_, que integra o rol obrigatório do Bacharelado em Ciência de Dados e Inteligência Artificial da Universidade Fedaral da Paraíba.
# 
# ## Objetivos
# 
# Os objetivos da disciplina são:
# 
# - Elencar os marcos históricos de desenvolvimento do campo do conhecimento denominado _visualização de dados_;
# - Reconhecer conceitos de representação visual, percepção, estética, cores e seus impactos ao observador;
# - Discutir técnicas diversas para representação visual de quantidades, proporções, tendências, dados geoespaciais e informações gerais, bem como de _storytelling_ e _business storytelling_;
# - Desenvolver códigos agnósticos para visualização de dados multidimensionais, mas com particular ênfase a objetivos negociais, técnicos ou científicas;
# - Experimentar ferramentas e plataformas modernas para construção de painéis analíticos (_dashboards_); e
# - Propor soluções de _data reporting_ para geração de relatórios automatizados e casos de negócio dos diversos setores da economia.

# ## Estrutura
# 
# A disciplina é composta por 3 módulos. Cada módulo é subdividido em duas partes, conteúdo e avaliação, na seguinte estrutura resumida:
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
# A divisão geral acima pode ser visualizada graficamente pelo _treemap_ abaixo, em que as áreas dos retângulos representam, proporcionalmente, a carga horária total de 60h.

# In[1]:


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
plot(f, show_link=False,filename='../temp/course-treemap.html')
display(HTML('../temp/course-treemap.html'))


# ## Conteúdo 
# 
# O conteúdo principal do curso está estruturado no formato de _ebook_, cujas seções e capítulos estão dispostos abaixo:
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
#     - Análise de Caso de Visualização de Dados (ACVD) (2h)
# 
# ### Módulo 2: Técnica (20h)
# 
# - Conteúdo (18h)
#     - [_Dataviz Code Session_: Quantidades](20-dcs-quantidade.ipynb)
#     - [_Dataviz Code Session_: Distribuições](21-dcs-distribuicoes.ipynb)
#     <!--- _Dataviz Code Session_: Proporções-->
#     - [_Dataviz Code Session_: Dados Geoespaciais](23-dcs-geoespacial.ipynb)
#     - [_Dataviz Code Session_: Dados Multidimensionais](24-dcs-multidimensional.ipynb)
#     - [_Dataviz Code Session_: Redes Complexas](25-dcs-redes.ipynb)
#     - [_Dataviz Code Session_: Visualização Científica](26-dcs-cientifica.ipynb)
#     - [_Dataviz Code Session_: Séries Temporais e Tendências](27-dcs-serietemporal.ipynb)
# 
# - Avaliação (2h)
#     - Estudo de Caso de Visualização de Dados (ACVD) (2h)
# 
# ### Módulo 3: Aplicações (20h)
# 
# - Conteúdo (14h)
#     - _Dashboarding_ (6h)
#         - [Objetos gráficos e _Plotly Express_](28-dw-plotly.ipynb) (2h)
#         - [_Dashboarding_ com _Dash_](30-dw-dash.ipynb) (4h)
#     - _Reporting_ (4h)
#         - [_Data Reporting_ com HTML/PDF](31-dw-reporting.ipynb)
#         - [_Data Reporting_ com _reportlab_](32-dw-reportlab.ipynb)
#     - _Business Intelligence_ (4h)
#         - Seminários e demonstrações
# 
# - Avaliação (6h)
#     - Projeto Final de Visualização de Dados (PFVD) (6h)
# 
# ### Suplemento
# 
# - [Guia rápido de plotagem: _seaborn_](A-quick-guide-seaborn.ipynb)
# - [Guia rápido de plotagem: _matplotlib_](B-quick-guide-matplotlib.ipynb)
# 
# <!--**Obs./(*):** capítulos não linkados estão em construção.-->

# ## Metodologia de avaliação
# 
# ### Tipificações, critérios e fórmulas 
# 
# A metodologia de avaliação em sua forma plena está explicada no [Sílabo](https://drive.google.com/file/d/1NCVxgIqjqwB03r-3mAVewQZSf-yr3_-a/view?usp=share_link).
# 
# ### Modelo para ECVD
# 
# Para elaborar o ECVD, pode-se usar o template em formato `.ODT` ou `.TEX` disponíveis [aqui](https://drive.google.com/drive/folders/1dQMw7TwcPNMPULJYQgACOMi4Uo3sqdqN?usp=share_link0).

# ## Inspirações para projetos
# 
# Veja este [post](https://pt.venngage.com/blog/estudo-de-caso/).
# 
# ### Temas baseados nos ODS (Agenda 2030)
# 
# - https://sdgs.un.org/goals
# 
# ### Temas gerais
# 
# - Agricultura, pecuária, pesca
# - Artes, entretenimento (cinema, teatro, música)
# - Biotecnologia, materiais avançados
# - Clima, meio ambiente, recursos naturais
# - Economia, renda, desigualdade social, finanças, mercados
# - Direito, legislação, justiça, segurança pública, computação forense
# - Educação, ciência, tecnologia, inovação
# - Energias, transição energética
# - Gestão, administração, pessoas
# - Geopolítica, relações internacionais, comércio exterior
# - Infraestrutura, saneamento, cidades inteligentes
# - Indústria 4.0, transformação digital, IoT
# - Política, ética, cidadania
# - Saúde, esportes, qualidade de vida
# - Trivium e Quadrivium
# - Turismo, lazer
# 
# 
# ### Temas de pesquisa do professor
# 
# - Descarbonização:
# 	- transição energética (setor industrial e de energia), particularmente óleo e gás;
# 	- hubs e clusters de CCUS, análise de dados geospacial;
# 	- mercados de carbono;
# - Engenharia computacional: 
# 	- métodos numéricos e variacionais; 
# 	- dinâmica dos fluidos computacional;
# 	- aprendizagem de máquina científico;
# 	- redes neurais informadas por (e conscientes da)  física;
# 	- métodos computacionais em saúde digital;
# 	- _research software engineering_;
# 	- modelagem de dados;
# 	- protocolos de reprodutibilidade;
# 	- aplicações _SAVE_: ciência, análise, visualização e engenharia de dados;

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
