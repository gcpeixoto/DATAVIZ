#!/usr/bin/env python
# coding: utf-8

# # Marcos Históricos da Visualização de Dados

# ## Cronologia
# 
# Mapear os fatos históricos de uma determinada área da ciência de forma meticulosa é uma tarefa quase impossível. Neste capítulo, faremos um breve resumo dos principais eventos que marcaram época no desenvolvimento da visualização de dados. O material baseia-se em um capítulo escrito por Michael Friendly {cite:p}`friendly2005`, Professor da Universidade de York, Canadá.
# 
# Registros da informação quantitativa técnica mais especializada são conhecidos desde o século XV, principalmente motivados pela cartografia e pelo pensamento estatístico. Entretanto, os relatos são incompletos e organizados em obras de autores fortemente ligados à matemática, astronomia e estatística. 
# 
# Na presente cronologia, consideramos apenas eventos ocorridos a partir do século XVII. 

# ### Período de 1600 - 1699
# 
# No início deste século, preponderou o interesse em medir quantidades físicas, tais como tempo, distância e espaço, para finalidades de navegação, expansão territorial e estudo dos astros. Vimos a ascenção da geometria analítica, da teoria dos erros e estimações, da teoria da probabilidade e da estatística demográfica. Um nome que ressalta desta época é Michael Florent van Langren, astrônomo da corte espanhola que supostamente foi quem criou a primeira representação visual de dados estatísticos em 1644 ({numref}`fig-langren`). 
# 
# ```{figure} ../figs/langren.png
# ---
# name: fig-langren
# alt: Carte Figurative de Minard. Original.
# align: center
# width: 600px
# ---
# Gráfico de van Langren (1644) para determinação de distância, em longitude, da cidade de Toledo a Roma.
# ```

# ### Período de 1700 - 1799
# 
# Durante o século XVIII, formas gráficas mais elaboradas passaram a enriquecer os mapas até então conhecidos. Caminhos foram abertos para isolinhas e isocontornos, mapeamento temático de dados físicos, geológicos, econômicos e médicos. Gráficos abstratos e os primeiros gráficos de funções matemáticas foram introduzidos, bem como novas formas visuais que "falavam por si". 
# 
# [William Playfair](https://en.wikipedia.org/wiki/William_Playfair) (1759 - 1823) é considerado o principal inventor da época e o pioneiro da construção das representações visuais que utilizamos até hoje, tais como o gráfico de linhas e de barras (1786), o de setores ("pizza") e circular (1801).

# ### Período de 1800 - 1850
# 
# No curso da primeira metade deste século explodiram os gráficos estatísticos e os mapas temáticos modernos a uma taxa de produção sem precedentes, tais como histogramas, séries temporais, gráficos de dispersão e atlas compreensivos. Diversas formas de simbolismo em tópicos econômicos, sociais, morais, entre outros, progrediram em massa. Um autor proeminente desta época é [Charles Minard](https://en.wikipedia.org/wiki/Charles_Joseph_Minard) (1781 - 1870).

# ### Período de 1850 - 1900
# 
# Na segunda metade do século XIX, o cenário já estava pronto para que os mecanismos para visualização de dados se consolidassem. Escritórios oficiais sobre análises estatísticas foram estabelecidos por toda a Europa em resposta ao reconhecimento da relevância da informação numérica para ações de planejamento social, comercial e de mobilidade. A teoria estatística encabeçada por Gauss e Laplace foram responsáveis por difundir grandes quantidades de dados, fazendo com que este período fosse conhecido como a era de ouro dos gráficos estatísticos.

# ### Período de 1900 - 1950
# 
# Houve pouca inovação neste período para os gráficos estatísticos, que foram ofuscados pelo crescimento dos modelos formais. As figuras passaram a ser meras ilustrações. Opostamente ao período anterior, esta fase da história da visualização de dados ficou conhecida como a _era das trevas_. Apesar disso, neste período as representações visuais tornaram-se populares, passando a compor livros didáticos, currículos escolares. Elas também instauraram o padrão visual em instituições governamentais, comerciais e científicas. 

# ### Período de 1950 - 1975
# 
# O espírito numérico e formal estabelecido em meados da década de 1930 induziu o renascimento da visualização de dados por volta de 1960. Os desenvolvimentos mais significativos responsáveis por reanimar a área após cerca de 50 anos de apatia foram os seguintes:
# 
# - Nos EUA, [John Tukey](https://en.wikipedia.org/wiki/John_Tukey) (1915 - 2000) configura-se como patrono da _Análise Exploratória de Dados_. Além de atuar em outras frentes, foi durante o trabalho com [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) que Tukey introduziu o termo _bit_ como designador de _binary digit_ (dígito binário).
# 
# - Na França, [Jacques Bertin](https://en.wikipedia.org/wiki/Jacques_Bertin) (1918 - 2010) publicou a conhecida obra _Sémiologie Graphique_ (Semiologia Gráfica) em 1967, onde estabeleceu as variáveis visuais estruturantes para se construir imagens gráficas. As 8 variáveis de Bertin revolucionaram a ciência da percepção visual.
# 
# - O desenvolvimento da computação permitiu que gráficos de alta resolução pudessem ser elaborados. Ao mesmo tempo, evoluções paralelas ocorreram, tais como o desenvolvimento de linguagens de programação no Bell Labs, da análise exploratória de dados, da tecnologia de impressão e de periféricos (plotters, terminais gráficos, mouse etc.). Esse encadeamento de fatos implicaram em novos paradigmas de expressão de ideias estatísticas e técnicas avançadas de implementação de visualização de dados.

# ### Período de 1975 em diante
# 
# No final do século XX, a ciência multidisciplinar intermediou o florescimento da visualização de dados. Métodos computacionais hoje estão disponíveis para qualquer sistema operacional, preferidos por cientistas e analistas provenientes das mais diversas áreas de conhecimento. Alguns pontos de destaque são:
# 
# - Desenvolvimento de sistemas interativos;
# - Novos paradigmas de manipulação de dados;
# - Métodos inovadores para representação multidimensional de dados;
# - Reinvenção de técnicas gráficas para dados discretos e categóricos;
# - Visualização de dados suportada por estruturas de dados de alta complexidade;
# - Domínio de conhecimento sobre aspectos cognitivos e de percepção da representação de dados;
# - Crescimento da infraestrutura tecnológica e computacional para visualização (códigos abertos, engenharia de software gráficos, computação paralela, _streaming_ de dados em tempo real).

# ### Fatos emblemáticos
# 
# A seguinte tabela mostra uma cronologia breve sobre fatos emblemáticos da dataviz.
# 
# | Período     | Evento |
# |:------------|:--------------------------------------------------------------------------------------------------------------------------------------|
# | 1750 - 1800 | William Playfair produz os primeiros gráficos modernos.                                                                               |
# | 1858        | Florence Nightingale cria o seu “diagrama Coxcomb” (circular) para ilustrar frações de mortalidade por doenças no exército britânico. |
# | 1861        | Charles Minard publica a Carte Figurative.                                                                                            |
# | 1914        | Willard Brinton publica o primeiro livro sobre visualização para negócios: Graphic Methods for Presenting Facts.                      |
# | 1952        | Mary Eleanor Spear publica Charting Statistics, um livro de melhores práticas de criação de gráficos.                                 |
# | 1967        | Jacques Bertin publica Sémiologie Graphique.                                                                                          |
# | 1970 - 1980 | John Tukey inaugura a visualização de dados por meio de computadores e populariza os conceito de análise exploratória de dados.       |
# | 1983        | Edward Tufte publica The Visual Display of Quantitative Information.                                                                  |
# | 1984        | William Cleveland e Robert McGill publicam o primeiro de vários trabalhos de pesquisa que tentam medir a “percepção gráfica”.         |
# | 1986        | Jock Mackinlay publica uma influente tese de doutorado que levou o trabalho de Jacques Bertin para a era digital.                     |
# | 1990 - 2000 | Abordagens divergentes surgem entre agentes da visualização científica de dados e jornalistas orientados por design.                  |
# | 2010        | Dataviz torna-se democrática por causa da internet.                                                                                   |
# | Hoje        | Dataviz se expande por um amplo espectro de disciplinas com gráficos dinâmicos e alta interatividade.                                 |                               |

# ## Cronologia gráfica
# 
# - _Carte Figurative_ de [Charles J. Minard](https://en.wikipedia.org/wiki/Charles_Joseph_Minard) (1781 - 1870). Versões ({numref}`fig-minard1`, {numref}`fig-minard2`). Ver {cite:p}`friendly2002visions`.
# 
# ```{figure} ../figs/minard1.png
# ---
# name: fig-minard1
# alt: Carte Figurative de Minard. Original.
# align: center
# width: 600px
# ---
# _Carte Figurative_ de Minard: ilustra a campanha militar de 1812 de Napoleão Bonaparte.  Original: ENPC, Multimedia Library
# ```
# 
# ```{figure} ../figs/minard2.png
# ---
# name: fig-minard2
# alt: Carte Figurative de Minard. Revision.
# align: center
# width: 600px
# ---
# _Carte Figurative_ de Minard: ilustra a campanha militar de 1812 de Napoleão Bonaparte. Revisão: Friendly, M.
# ```

# - Gráficos de [William Playfair](https://en.wikipedia.org/wiki/William_Playfair) (1759 - 1823) sobre a economia da Inglaterra ({numref}`fig-playfair1`, {numref}`fig-playfair2`, {numref}`fig-playfair3`), disponíveis [aqui](https://www.datavis.ca/gallery/historical.php).
# 
# ```{figure} ../figs/playfair1.png
# ---
# name: fig-playfair1
# alt: Balança Comercial da Inglaterra.
# align: center
# width: 600px
# ---
# Balança comercial da Inglaterra.
# ```
# 
# ```{figure} ../figs/playfair2.png
# ---
# name: fig-playfair2
# alt: Série temporal de preços e salários.
# align: center
# width: 600px
# ---
# Série temporal tripla: variação de preço do trigo, do salário semanal e do monarca reinante ao longo de 250 anos (1565 - 1820).
# ```
# 
# ```{figure} ../figs/playfair3.png
# ---
# name: fig-playfair3
# alt: Dívida pública inglesa.
# align: center
# width: 200px
# ---
# Dívida pública inglesa.
# ```

# ## Referências
# 
# ```{bibliography}
# :filter: docname in docnames
# ```
