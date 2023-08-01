#!/usr/bin/env python
# coding: utf-8

# # Percepção Visual
# 
# Prof. Gustavo Oliveira
# 
# CI/DCC/UFPB
# 
# [gcpeixoto.github.com/DATAVIZ](gcpeixoto.github.com/DATAVIZ)

# ## Introdução
# 
# - Humanos captam 70% da informação pela visão e 30% pelos demais receptores sensoriais (audição, olfato, paladar e tato);
# - Saber sobre a mecânica da visão é útil para construir RVs melhores
# - _Insight_, _iluminação_ e _esclarecimento_, são conceitos relacionados à visão
#     - Dão sentido de recebimento de informação
#     - Trazem descrições apuradas sobre algo 
# - Percepção visual e visualização de dados são assuntos vinculados

# ## A mecânica da visão
# 
# Dividida em dois estágios principais:
# 
# 1. _Sensação_ (processo físico): ocorre quando nossos olhos são estimulados por um objeto emissor ou refletor de luz.
# 2. _Percepção_ (processo cognitivo): ocorre com a entrada de luz pelos olhos
#     - Absorção por células nervosas;
#     - Tradução dos sinais neurais (pulsos eletroquímicos)
#     - Transmissão para o cérebro, tornando aquilo que foi sentido torna-se percebido

# <img src="../figs/globo-ocular.png" width="600" height="600">
# 
# 
# [Fonte](https://fisica.netspa.com.br/2020/10/01/fisica-otica-da-visao/)

# - _Fóvea_: reconhecimento de espectros de cor (vermelho, azul ou verde) e onde a acuidade visual é máxima. 
# - Capaz de focar em apenas uma área limitada durante um intervalo de tempo. 
# - Olhos fixados em um ponto particular / eventos não percebidos pelo campo de visão. 
# - RVs abarrotadas de cores e elementos dispersam os olhos do espectador e atrapalham o foco

# ### Tipos de memória
# 
# - A neurologia hoje reconhece várias memórias (episódica, semântica, icônica (MI), háptica, entre outras)
# - Quanto à temporalidade, duas classes importantes: 
#     - _memória de curto prazo (MCP)_
#     - _memória de longo prazo (MLP)_
# - Informação recebida pelos olhos roteada pelo nervo óptico para a MI (_registro sensorial_)
# - Informação permanece na MI (< 1s) antes de passar para a MCP. 
# - MCP similar à memória RAM (temporária e limitada)
# - Cérebro lida com pedaços da informação visual (parte armazenada; parte esquecida)

# #### Equilíbrio de estímulos
# 
# - Trabalhar com RVs é equilibrar estímulos para a recepção da informação ser absorvida adequadaemente
# - Lado negativo é a "exploração" visual através do _marketing_ coercitivo (máxima atratividade). 
# > A finalidade do projeto visual dará a direção a ser seguida, mas **sempre a audiência deve ter sua cognição minimamente respeitada**

# ### Percepção não controlada 
# 
# - _Percepção não controlada_ (_pre-attentive perception_) refere-se a propriedades visuais detectadas rapidamente (em frações de segundo) antes do processo da percepção propriamente dita. 
# - Manifesta-se durante a identificação imediata de elementos visuais

# <img src="../figs/wordcloud.png" width="600" height="600">
# 

# ### Propriedades não controladas
# 
# - Podem ser postas em quatro categorias: 
#     - _cor_
#     - _formato_
#     - _movimento_
#     - _posição espacial_
#    

# ### Quanto à cor
# 
# - Há três atributos principais, que definem o espaço primário de cores chamado de _HSL_ 
# 
# | Atributo    | Descrição |
# |:-------------|:---- |
# |Matiz (_Hue_)|Caracteriza o comprimento de onda dominante da cor (também chamado de tonalidade cromática)|
# |Saturação (_Saturation_)|Medida de pureza da cor, isto é, a quantidade de luz branca|
# |Luminância (_Lightness_)|Grau de brilho de uma imagem, em escala de branco a preto (também chamada de intensidade luminosa)|

# <img src="../figs/hsv-cone.png" width="700" height="700">
# 

# ### Quanto ao formato
# 
# - Há pelo menos dez atributos reconhecíveis
# 
# | Atributo    | Exemplo |
# |:-------------|:---- |
# |Orientação |Linha destacando-se de outras por ter orientação diferente|
# |Comprimento|Gráfico com barras de comprimentos variáveis|
# |Largura|Largura de uma linha usada para destaque|
# |Tamanho|Tamanho de uma forma geométrica para destacar quantidade (elemento visual)|
# |Colinearidade|Linhas paralelas|
# |Curvatura|Contornos de formas|
# |Agrupamento|Objetos dispostos em grupos (clusters)|
# |Marcações|Anotações em objetos por meio de marcações|
# |Formato|Triângulo entre quadrados|
# |Numerosidade|Número de objetos (cardinalidade) em um grupo|

# <img src="../figs/atributos-preattentive.png" width="500" height="500">

# ### Quanto à posição espacial
# 
# - Podemos detectar três atributos
# 
# | Atributo    | Descrição |
# |:-------------|:---- |
# |Posição 2D |Codifica dados quantitativos em representações visuais|
# |Profundidade estereoscópica|Permite termos uma noção de profundidade espacial em uma imagem plana (ver [estereoscopia](https://pt.wikipedia.org/wiki/Estereoscopia)).|
# |Concavidade/convexidade|Cria efeitos de superfície através de sombreamentos.|

# ### Concavidade/convexidade
# 
# - Efeito produzido através de sombreamentos
# 
# <img src="../figs/convexidade.png" width="500" height="500">

# ### Quanto ao movimento
# 
# - Há dois atributos: _flickering_ e _motion_. 
# 
# - _Flickering_ pode ser abusivamente utilizado em páginas da internet. Quando monitores tremulam, alguns efeitos adversos aos olhos são cansaço, irritação e lacrimação. 
# - _Motion_ é a característica básica de deslocamento de objetos em tela.
# 
# | Atributo    | Descrição |
# |:-------------|:---- |
# |_Flickering_ |Objetos "tremidos" em websites com forte apelo visual ou _dashboards_|
# |_Motion_|Objetos em movimento.|

# ### Flickering
# 
# <img src="../figs/flickering.jpeg" width="400" height="400">
# 
# [Fonte](https://www.dpreview.com/forums/thread/3964319)

# <img src="../figs/flickering2.jpg" width="500" height="500">
# 
# [Fonte](https://hondatheotherside.com/dash-lights-flickering-car-wont-start/)

# ### Combinação de atributos _preattentive_
# 
# - A combinação desses atributos (imagem, luminosidade, formaDificultam
# 
# <img src="../figs/combinacao-preattentive.png" width="500" height="500">

# ### Percepção controlada
# 
# - A percepção controlada é consciente, sequencial, e lenta. 
# - Dá-se pela procura de foco. 
# - Para acentuar a diferença entre percepções, vejamos a figura abaixo. 
# - Ambas as sequências de dígitos são idênticas.
#     - 1a. linha exige controle focal (percepção controlada)
#     - 2a. linha, não (percepção não controlada)

# In[3]:


import aux05a


# ### Cegueira à mudança (_change blindness_)
# 
# - O fenômeno ocorre quando, visualmente, somos incapazes de notar mudanças sensíveis no ambiente quando reposicionamos nosso foco instantaneamente de um objeto para outro. 
# - Moldes de um "jogo de 7 erros".

# <img src="../figs/Globe_and_high_court_(Spot_the_difference).jpg" width="1000" height="700">
# 
# 
# Atribuição: Globe_and_high_court.jpg, WikiCantona, CC BY-SA 3.0, via Wikimedia Commons.

# ### Relação entre adequabilidade de atributos e categoria de dados
# 
# - Varia de acordo com a categoria dos dados
# - Os símbolos `-`, `+` e `++`, nesta ordem, significam _adequação insuficiente_, _adequação limitada_, _adequação suficiente_.
# 
# |Categoria do atributo| Atributo | Quantitativo | Qualitativo categórico | Qualitativo não categórico  | 
# |:-------------|:-----------|:-----------|:---------|:-----------|
# |Cor|Matiz| - | - | ++ |
# |Cor|Luminância| + | ++ | - |
# |Forma|Orientação| + | + | - |
# |Forma|Comprimento| ++ | + | - |
# |Forma|Largura| + | + | - |
# |Forma|Tamanho| + | + | - |
# |Forma|Colinearidade| - | - | - |

# |Categoria do atributo| Atributo | Quantitativo | Qualitativo categórico | Qualitativo não categórico  | 
# |:-------------|:-----------|:-----------|:---------|:-----------|
# |Forma|Curvatura| + | + | - |
# |Forma|Agrupamento| - | - | - |
# |Forma|Marcações| - | - | ++ |
# |Forma|Formato| - | - | ++ |
# |Forma|Numerosidade| ++ | ++ | - |
# |Posição|Posição 2D| ++ | ++ | + |
# |Posição|Profundidade estereoscópica| - | - | - |
# |Posição|Concavidade<br>convexidade| + | + | - |
# |Movimento|Flickering| - | - | + |
# |Movimento|Motion| + | + | - |

# ## Princípios da Gestalt
# 
# - _Gestalt_, palavra alemã que, em tradução aproximada, seria algo como "forma total", é a alcunha de uma teoria também conhecida como _psicologia da forma_. 
# - Explica que, como o ser humano enxerga o "todo" e não as "partes" do todo, aquilo que vemos é compreendido de forma diferente pela mente
# - Por esta razão, antes precisamos entender a totalidade, para então compreender a particularidade
# - A composição de elementos e formas induz concepções distintas daquilo que vemos

# <img src="../figs/gestalt.png" width="700" height="700">

# <img src="../figs/gestalt-row1.png" width="500" height="500">
# 
# Na primeira linha, o que vemos? 
# 
# - Ao analisar seus elementos, podemos ter diversas percepções. 
# - Na primeira linha, o primeiro objeto é um mero quadrado; 
# - O segundo é um quadrado "picotado" em quatro; (abajur; minka japonesa ?)
# - O terceiro é o mesmo quadrado picotado em quatro partes, porém com vãos largos (vemos apenas um "X"?); 
# - O último é um quadrado inserido em outro (vemos um  "losango circunscrito"?), porém girado. 

# <img src="../figs/gestalt-row2.png" width="500" height="500">
# 
# Na segunda linha, o que vemos? 
# 
# - O primeiro objeto representa um abajur? Uma minka (casa japonesa)? 
# - O segundo objeto representa uma casinha com neve no telhado? 
# - O terceiro uma casinha com janelas? 
# - O último uma fábrica com chaminé? 

# > Alguns ou todos esses conceitos podem ter passado à mente, mas percebemos que todos os elementos gráficos são apenas composições de triângulos e quadrados?? 
# 
# > Esse efeito provocado pelas formas, que nos faz ver o todo e não as partes, à primeira vista, é o que a teoria da _Gestalt_ explica. Os princípios da Gestalt são aplicados ao _design_ até hoje para facilitar a comunicação das informações e, muitas vezes, de forma intuitiva.

# ### 6 princípios da Gestalt
# 
# 1. _Figura/Fundo_: o olho humano é capaz de distinguir entre o objeto núcleo e a área que o rodeia.
# 2. _Continuidade_: o olho humano é compelido a "seguir" o objeto, movendo-se do início dele ao fim.
# 3. _Proximidade_: quando dois objetos são postos juntos, o olho humano tende a percebê-los como um único grupo.

# 4. _Similaridade_: quando vários objetos tem aparência similar, o olho humano os percebe como um grupo ou padrão.
# 5. _Fechamento_: o olho humano tende a perceber um objeto "completo" ou "fechado", mesmo quando é "incompleto" ou não perfeitamento "fechado".
# 6. _Simetria e ordem_: também chamado de princípio da "boa figura" ou "pregnância" (do alemão _prägnanz_), manifesta-se quando o olho humano percebe formas ambíguas da maneira mais simples possível.

# ### Aplicações dos princípios da Gestalt 
# 
# <img src="../figs/gestalt-principles.png" width="800" height="800">
# 
# [Fonte](https://www.simplypsychology.org/what-is-gestalt-psychology.html)
# 
