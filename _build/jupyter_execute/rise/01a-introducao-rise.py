#!/usr/bin/env python
# coding: utf-8

# # Introdução à Visualização de Dados
# 
# Prof. Gustavo Oliveira
# 
# CI/DCC/UFPB
# 
# 
# [gcpeixoto.github.com/DATAVIZ](gcpeixoto.github.com/DATAVIZ)

# Características essenciais para o desenvolvimento de habilidades na disciplina:
# 
# - Familiaridade com _estatística_;
# - _Vontade_ de aprender coisas novas; 
# - _Curiosidade_ para descobrir respostas;
# - Apetite por _princípios de design_;
# - Disposição para aumentar seu _rigor analítico_ e
# - _Conhecimento técnico_ de pelo menos uma ferramenta para plotagem.

# 
# ## Pontos de equilíbrio
# 
# 
# 1. É melhor aprender visualização de dados através de um guia ou manual, que discute princípios, conceitos e orientações, ou através de um tutorial, que contém exemplos de código e demonstrações de gráficos incríveis?
# 2. Devemos dissertar sobre as nuances artísticas, com toda a beleza do design, ou sobre a elegância simples e útil do cotidiano?
# 3. Faz sentido compreender conceitos teóricos da visualização de dados, ou ser apenas pragmático?
# 4. Vale seguir o exemplo dos livros pioneiros e clássicos históricos, ou avalizar o contemporâneo?
# 5. O que queremos com os dados: prover um arcabouço analítico de exploração e interatividade (visualização para análise), ou apenas comunicá-los a uma audiência para gerar impacto e atratividade (visualização para comunicação)?

# 
# ## Visão geral do curso
# 
# - **Fundamentos**: módulo dedicado ao estudo dos conceitos primários da visualização de dados, tais como seu desenvolvimento histórico, princípios, percepção, estética e cores.
# - **Técnicas**: módulo dedicado à discussão de técnicas diversas para representação visual de quantidades, proporções, tendências, redes e informações gerais, através de exemplos de códigos.
# - **Aplicações**: módulo dedicado à apresentação de ferramentas e plataformas modernas para construção de painéis analíticos (_dashboards_) e soluções de _data reporting_ com tutoriais simplificados.

# ## Arquitetura visual x engenharia visual
# 
# - _Arquitetura visual_: área profissional que cuida da especificação dos projetos de visualização de dados;
# 
# - _Engenharia visual_: área que executa tais projetos.
# 
# Este curso abrange majoritariamente a segunda área.
# 
# _Nota_: as definições são do professor.
# 

# ## Definindo _Visualização de Dados_
# 
# Neste curso, usaremo a seguinte definição, adaptada de [Andy Kirk](https://twitter.com/visualisingdata):
# 
# > _Visualização de dados é a arte de combinar representações visuais e apresentações para facilitar a compreensão dos dados._

# - _Representação visual_ (_chart_) como elemento que melhor se adéqua ao que se pretende comunicar. 
# - _Charts_ têm _marcadores_ e _atributos_ como fundamentos
# - A _apresentação visual_ concerne a todas as outras tomadas de decisão de design que constituem a anatomia da visualização:
#     - seleção da paleta de cores;
#     - composição da obra;
#     - características das anotações. 
# - Parcela artística do autor independe da ferramenta técnica.

# - A parte final da definição diz respeito à _compreensão facilitada_ dos dados,
# - Processo de captura da mensagem lançada pelo contador de história (_storyteller_) ao espectador (_viewer_) em 3 etapas cognitivas:
# 
# 1. _Percepção_ (o que vejo?)
# 2. _Interpretação_ (o que significa?)
# 3. _Compreensão_ (o que significa para mim?)

# ### As 3 fases da compreensão de uma representação visual
# 
# <img src="../figs/3-steps-cognition.png" width="1200" height="1200">
# 

# ### Figuras feias, ruins e erradas
# 
# Diferentes versões de figuras com a mesma representação visual subjacente podem existir.
# 
# - _feia_ é aquela que tem problemas estéticos, apesar de clara e informativa.
# - _ruim_ é aquela que tem problemas relacionados à percepção, tais como obscuridade, confusão, complicações e enganação.
# - _errada_ é aquela que tem problemas relacionados à matemática e é objetivamente incorreta.

# <img src="../figs/hists-lodo.png"  width="1200" height="1200">

# Comparação de figuras: 
# 
# - A) adequada, sem problemas aparentes graves; 
# - B) versão "feia", tecnicamente correta, mas colorida inutilmente; 
# - C) versão "ruim", também tecnicamente correta, mas com marcações e gradeado destoantes; 
# - D) versão "errada", sem escala explícita e aparentemente díspar em quantidade.

# ### _Dataviz_, o pensamento visual e o bom plot
# 
# - A visualização de dados (_dataviz_, de _data visualization_) é uma disciplina obrigatória para um novo modo de pensar: o _pensamento visual_ 
# - No mundo dos negócios, pensar visualmente é ser capaz de construir representações visuais com grande potencial atrativo. 
# - Para empresas competitivas, a mensagem clara e acessível transmitida graficamente é uma das grandes vantagens de _marketing_.

# #### _Matriz da Boa Representação Visual_
# 
# - Sugere que um plot considerado "bom" deve aproximar-se cada vez mais da quina superior direita, onde reside a perfeição.
# 
# <img src="../figs/good-chart-matrix.png" width="600" height="600">

# ## Princípios de Tufte
# 
# - apresentar dados;
# - induzir o espectador a pensar a substância da representação visual e não os métodos ou técnicas que a estruturaram;
# - evitar distorcer os dados;
# - apresentar muitos números em um espaço mínimo;
# - tornar grandes dados coerentes;
# - encorajar os olhos a compararem diferentes partes dos dados;
# - revelar os dados em vários níveis de detalhe, do mais amplo ao mais específico;
# - servir a um propósito claro: descrever, explorar, tabelar e decorar; e 
# - estar estreitamente vinculada às descrições estatísticas e verbais dos dados.
# 
# Ver [Edward Tufte](https://www.edwardtufte.com/tufte/)

# Alguns princípios fundamentais de Tufte incorporam todas as expectativas acima:
# 
# - _Integridade visual_: a figura não deve, de forma alguma, distorcer ou criar falsas interpretações dos dados.

# - Regras para a integridade:
#     1. Dizer a verdade sobre os dados;
#     2. Mostrar a variação dos dados, não do design;
#     3. Tornar grandes conjuntos de dados coerentes;
#     4. Revelar dados em vários níveis de detalhe.

# ### Exemplos de (falta de) integridade visual
# 
# - Número de camisas _jersey_ de alguns jogadores vendidas ([Fonte](https://www.linkedin.com/pulse/edward-tuftes-six-principles-graphical-integrity-radhika-raghu/))
# 
# <img src='../figs/integrity1.jpeg' width=500px>

# - Problema: desproporcionalidade entre quantidade e comprimento das barras!
# - Solução: criar proporções corretas; eliminar imagem do CR7; criar escala
# 
# <img src='../figs/integrity2.jpeg' width=500px>
# 

# - Gráfico com legendas incompletas/incoerentes, desordenadas, sem título e sem clareza
# 
# <img src='../figs/integrity3.png' width=900px>

# - Gráfico com duas diferentes escalas/perspectivas de análise (confuso)
# 
# <img src='../figs/integrity4.jpeg' width=500px>

# - _Maximização da razão "tinta-dados"_: para Tufte, o _storyteller_ precisa atentar para a quantidade de elementos agregados em uma representação visual. A equação para o que Tufte chamou de razão "tinta-dados" (_data-ink ratio_), aqui denotada por $\text{RTD}$ é: 
# 
# $$\text{RTD} = \dfrac{d - t}{T},$$
# 
# onde $d$, $t$, e $T$ denotam, nesta ordem, a quantidade de tinta usada para os dados, para os adereços e para ambos, no total. Maximizar a $\text{RTD}$ implica em eliminar do visual aquilo que é inútil ou não essencial.

# - As leis de Tufte para a "tinta":
#     1. Mostre os dados;
#     2. Maximize a RTD;
#     3. Remova elementos desnecessários;
#     4. Delete redundâncias;
#     5. Revise e edite.

# ### Exemplo de maximização da RTD
# 
# - Calorias/100g para diferentes "junk foods" ([Fonte](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/))
# 
# <img src='../figs/rtd1.png' width=600px>

# - Remove cores de background (figura e eixos), pois nada acrescentam
# 
# <img src='../figs/rtd2.png' width=560px>

# - Remove redundâncias (título; legenda; label X, label Y)
# 
# <img src='../figs/rtd3.png' width=560px>

# - Remove bordas (adicionam apenas tinta e nenhuma informação)
# 
# <img src='../figs/rtd4.png' width=560px>

# - Reduz cores (legendas sob barras indicam tipos; vermelho para destaque)
# 
# <img src='../figs/rtd5.png' width=520px>

# - RTD maximizada, porém podemos otimizar ainda mais retirando efeitos 3D e sombras
# 
# <img src='../figs/rtd6.png' width=520px>

# - Grade não auxilia tanto (podemos indicar valores exatos e removê-la, chegando a uma RV minimalista)
# 
# <img src='../figs/rtd7.png' width=500px>

# - _Estética_: a elegância visual só pode ser atingida ao se equilibrar a complexidade dos dados com a simplicidade do design.
# 
#     - A grade pode ajudar ou esconder
#     
# <div style="width:1000px">
#     <figure class="left" style="float:left">
#     <img class="top" src="../figs/aesthetics1a.jpg" width="400" height="300"/>
#     </figure>
#     <figure class="left" style="float:left">
#     <img class="top" src="../figs/aesthetics1b.jpg" width="400" height="300"/>
#     </figure>
# </div>
# 
# [Fonte:](https://jcsites.juniata.edu/faculty/rhodes/ida/graphicalIntRedes.html)

# - Escala desequilibrada
# 
# <img src='../figs/aesthetics2.jpg' width=500px>

# - Distorção de _baseline_ (fixe a baseline em zero, em RVs de barra!)
# - Gráficos a seguir possuem diferentes baselines.
# 
# <img src='../figs/aesthetics3.png' width=500px>

# ### Fator de Lie ($L$)
# 
# $L$ = tamanho do efeito mostrado na RV / tamanho do efeito nos dados
# 
# - Na figura abaixo, $L =783/53=14.8$ (há 53% de aumento na economia de combustível, mas a linha de 27.5 aumentou 783%).
# - Desejável: $L \approx 1.0$.
# 
# <img src='../figs/lieFactor.jpg' width=600px>

# #### Exemplo de cálculo de $L$
# 
# Suponha uma RV em que 20 unidades são representadas por 1 cm de comprimento visual e 30 unidades são representadas por 5 cm. Tem-se (mudança relativa):
# 
# - tamanho do efeito no gráfico = (5 - 1)/1 = 4 
# - tamanho do efeito nos dados = (30 - 20)/20 = 10/20 = 0.5
# - $L = 4/0.5 = 8$

# ### _Chartjunks_
# 
# - RVs contaminadas por "elementos estranhos" que distraem o _viewer_ da mensagem central.
# - Trazem extradimensionalidade, decoração excessiva e coloração não informativa
# 
# <img src='../figs/chartjunk.jpg' width=500px>
# 
# 
# [Fonte](https://idratherbewriting.com/2010/11/01/what-is-chartjunk-visual-imagination-2/)

# ## Ferramentas técnicas do curso
# 
# - Python 3.x como linguagem de programação básica
# - Diversidade de pacotes para construção de plotagens e utilidades. 
# - Recomendação: ambiente virtual `conda` 

# ### Criação do novo ambiente
# 
# - Execute o comando: 
# 
# ```
# conda env create --file dataviz.yml
# ```
# 
# - Habilite o ambiente:
# 
# ```
# conda activate dataviz
# ```
# dataviz.yml

name: dataviz
channels:
  - defaults
  - conda-forge
dependencies:
  - numpy
  - scipy
  - dash
  - bokeh
  - hvplot
  - datashader
  - dask
  - h5py
  - geoviews
  - pandas
  - matplotlib
  - seaborn
  - plotly
  - geopandas
  - networkx
# ### Exemplo aplicado
# 
# - Visualizando a variação do preço por litro, em R$, de 6 tipos de combustíveis comercializados no estado da Paraíba por 8 operadoras durante o primeiro semestre de 2022. 
# 
# - Para a plotagem, usamos parte do [_dataset_](https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda/resource/a1e1955b-f340-415d-83bf-bbce710d142b) correspondente disponibilizado pela ANP no portal [Dados Abertos](https://dados.gov.br) do Governo Federal.

# In[2]:


from pandas import read_csv
from matplotlib.pyplot import subplots
import seaborn as sns

# pandas
df = read_csv('../data/preco-combs-pb-2022-02.csv')

# matplotlib
fig, ax = subplots(figsize=(14,5))
ax.set_title('Preço de combustíveis - PB - Semestre 2022/01. Fonte: ANP')
ax.set_ylabel('litro (R$)')

# seaborn
sns.set_style("whitegrid")
g = sns.boxplot(data=df, x="Bandeira", y="Valor de Venda",
    hue='Produto',palette="deep",ax = ax)
sns.move_legend(g, "upper center", title='', ncol=1,
    frameon=True, bbox_to_anchor=(1.11, .8))
sns.despine(offset=5,trim=True)
sns.set_style()


# ## Terminologias
# 
# 
# ### Termos para pessoas
# 
# - _Storyteller_: você, que está construindo o produto de visualização (cf. _visualiser_, _analyst_,_visualist_, _designer_).
# - _Viewer_: a pessoa que visualiza o produto construído (cf. _consumer_, _reader_, _user_).
# - _Audiência_: um grupo de espectadores ou coorte social a quem o produto de visualização é direcionado (cf. _audience_).

# ### Termos para dados
# 
# - _Dado bruto_: estado inicial de um dado coletado, recebido ou baixado de um repositório ainda não tratado ou sujeito a análises (cf. _raw data_).
# - _Fonte_: origem do dado bruto utilizado para a visualização (cf. _data source_).
# - _Dataset_: uma tabela ou coleção de tabelas dispostas como um _array_ computacional e organizadas em linhas (registros, instâncias ou itens) e colunas (variáveis, detalhes dos itens).
# - _Tipo_: a especificação de uma variável de tabela. Geralmente, um dado é _ordinal_ (obedece a uma relação de ordem), _numérico_ (manipulável por operações aritméticas) ou _categórico_ (identificado por um atributo que o difere de outro).
# - _Série_: sequência de valores assumidos por uma mesma variável em um _dataset_.

# ### Termos para visualização
# 
# - _Projeto de visualização_: conjunto de etapas progressivas que culminam na geração de um produto de visualização.
# - _Produto de visualização_: entregável de um projeto de visualização. Em geral, será uma _representação visual de dados_.
# - _Representação visual de dados_: termo genérico que abrange as diversas formas de disposição visual de dados, que chamaremos de _plot_. Um _plot_ pode ser um traçado representativo de uma quantitidade matemática univariada (gráfico), ou a aplicação de figuras geométricas planas ou espaciais, ou ainda a impressão de formas e símbolos para fins quantitativos ou qualitativos em várias dimensões. Assim, _plots_ incorporarão diagramas, fluxogramas, dendrogramas, superfícies, dispersões, correlações, mapas etc.
# - _Outlier_: valores em uma representação visual que escapam do intervalo normal e chamam atenção do espectador por serem ou muito menores ou muito maiores do que o esperado.

# ## Representações visuais para análise

# ### Indústria global da música 
# 
# <img src='../figs/streaming-revenue.jpeg' width=600px>
# 
# [Fonte](https://www.statista.com/chart/4713/global-recorded-music-industry-revenues/)

# ### Uso da terra para bioplásticos (2017-2022)
# 
# <img src='../figs/Land_use_estimation.jpg' width=600px>
# 
# [Fonte](https://www.european-bioplastics.org/how-much-land-do-we-really-need-to-produce-bio-based-plastics/)
# 

# ### Ranqueamento universitário (2020)
# 
# <img src='../figs/u-multirank.png' width=600px>
# 
# [Fonte](https://www.umultirank.org/export/sites/default/press-media/media-center/universities/2020/country-reports/US-Country-report-2020.pdf)
# 

# ### Tipologia biofísica do mangue na América do Norte, Central e Caribe 
# 
# <img src='../figs/mangrove-america.png' width=600px>
# 
# [Fonte](https://www.nature.com/articles/s41598-020-71194-5)
# 

# ### Potencial de soluções baseadas em carbono azul
# 
# <img src='../figs/blue-carbon-potential.png' width=600px>
# 
# [Fonte](https://www.mckinsey.com/capabilities/sustainability/our-insights/blue-carbon-the-potential-of-coastal-and-oceanic-climate-action)
# 

# ### Uso de navegadores para internet
# 
# <img src='../figs/browsers.jpeg' width=600px>
# 

# ### Corrida por usuários de serviços remotos
# 
# <img src='../figs/chat-gpt.jpeg' width=600px>
# 
# [Fonte](https://www.statista.com/chart/29174/time-to-one-million-users/)
# 

# ### Importadores de gás natural
# 
# <img src='../figs/gas-natural-importadores.png' width=600px>
# 
# [Fonte](https://www.ibp.org.br/observatorio-do-setor/snapshots/maiores-importadores-de-gas-natural/)

# ### Reservas hoteleiras
# 
# <img src='../figs/reservas-hoteleiras.jpeg' width=600px>
# 
# [Fonte](https://www.panrotas.com.br/hotelaria/mercado/2020/05/centro-oeste-e-sul-puxam-crescimento-de-reservas-hoteleiras-no-brasil_173356.html)

# ### Momentum do mercado financeiro global
# 
# <img src='../figs/global-market-momentum.png' width=600px>
# 
# [Fonte](https://blog.mipimworld.com/investment/resurgent-asia-a-top-source-of-cross-border-investment-capital/attachment/mipim-asia-blog-bubble-chart-171003/#prettyPhoto)
# 
