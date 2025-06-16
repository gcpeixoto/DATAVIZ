#!/usr/bin/env python
# coding: utf-8

# # Introdução à Visualização de Dados

# A visualização de dados é interdisciplinar e agregadora a qualquer pessoa interessada em manusear ou apresentar dados de forma qualitativa ou quantitativa. Ela não se restringe a áreas de formação específica, mas algumas características essenciais para o desenvolvimento de habilidades na disciplina são:
# 
# - familiaridade com _estatística_;
# - _vontade_ de aprender coisas novas; 
# - _curiosidade_ para descobrir respostas;
# - apetite por _princípios de design_;
# - disposição para aumentar seu _rigor analítico_ e
# - _conhecimento técnico_ de pelo menos uma ferramenta para plotagem.

# 
# ## Pontos de equilíbrio
# 
# A visualização de dados gera diversas dicotomias em sua trilha de aprendizagem. Podemos enviesar seu estudo para uma direção ou outra, dependendo dos interesses. Algumas perguntas que suscitam a busca por pontos de equilíbrio são as seguintes:
# 
# 1. É melhor aprender visualização de dados através de um guia ou manual, que discute princípios, conceitos e orientações, ou através de um tutorial, que contém exemplos de código e demonstrações de gráficos incríveis?
# 2. Devemos dissertar sobre as nuances artísticas, com toda a beleza do design, ou sobre a elegância simples e útil do cotidiano?
# 3. Faz sentido compreender conceitos teóricos da visualização de dados, ou ser apenas pragmático?
# 4. Vale seguir o exemplo dos livros pioneiros e clássicos ou prezar pelo contemporâneo?
# 5. O que queremos com os dados: prover um arcabouço analítico de exploração e interatividade (visualização para análise), ou apenas comunicá-los a uma audiência para gerar impacto e atratividade (visualização para comunicação)?
# 
# As respostas para essas questões não são binárias. Futuros profissionais que farão uso de tudo o que a visualização de dados tem a oferecer devem ser suficientemente flexíveis para encontrar seus pontos de equilíbrio particulares para cada situação apresentada. 

# 
# ## Visão geral do curso
# 
# Levando em consideração a necessidade por pontos de equilíbrio, este curso pretende abordar a visualização de dados em três módulos:
# 
# - **Fundamentos**: dedicado ao estudo dos conceitos primários da visualização de dados, tais como desenvolvimento histórico, princípios, percepção, estética e cores.
# - **Técnicas**: focado na discussão de técnicas diversas para representação visual de quantidades, proporções, tendências, redes e outros tipos de dados através de exemplos de códigos.
# - **Aplicações**: dedicado à apresentação de ferramentas e plataformas modernas para construção de painéis analíticos (_dashboards_), soluções de _data reporting_ e inteligência de negócios (_business intelligence_) por meio de tutoriais simplificados ou _workshops_.

# ## Arquitetura visual x engenharia visual
# 
# A audiência deste curso não deve esperar que ele seja puramente técnico, tampouco integralmente teórico. Entretanto, os objetivos de formação miram estudantes com razoável conhecimento de técnicas estatísticas e de programação. Portanto, não haverá aprofundamento em temas inerentes à arte e ao _design_. Se chamássemos de _arquitetura visual_ a área profissional que cuida da especificação dos projetos de visualização de dados, e de _engenharia visual_ a área que executa tais projetos, diríamos que este curso abrange majoritariamente a segunda.

# ## Definindo _Visualização de Dados_
# 
# A disciplina _visualização de dados_ é considerada recente sob o prisma teórico. Existem muito mais recomendações de princípios a serem seguidos do que, efetivamente, uma organização estruturada de conhecimento para lhe dar sustentação científica. A maioria dos praticantes na área entende que visualizar dados é um misto entre arte e técnica, até porque a humanidade é composta de seres substancialmente visuais. Não por acaso o clichê _"uma imagem vale mais que mil palavras"_ tornou-se popular.
# 
# ```{admonition} Curiosidade
# :class: dropdown
# A origem da expressão _"uma imagem vale mais que mil palavras"_ ([_"a picture is worth a thousand words_"](https://en.wikipedia.org/wiki/A_picture_is_worth_a_thousand_words)) deriva de um provérbio chinês supostamente propagado pelo filósofo Confúcio (551 - 479 AEC). Na América do século XX, a forma moderna desse adágio é atribuída a Fred Barnard, anunciante que viveu na década de 1920.
# ```
# 
# Saber encontrar a dosagem entre arte e técnica (ou ciência) é fundamental para que dados sejam comunicados com máxima precisão e eficiência, assim evitando equívocos e distorções. De certa forma, a representação visual da informação deve ser suficientemente agradável aos olhos de seu espectador sem, no entanto, interferir na mensagem que ela retrata. Um pouco mais adiante, discutiremos melhor esse contraste.
# 
# Neste curso, usaremos a seguinte definição, adaptada de [Andy Kirk](https://twitter.com/visualisingdata):
# 
# > _Visualização de dados é a arte de combinar representações visuais e apresentações para facilitar a compreensão dos dados._
# 
# A _representação visual_ (_chart_), ou simplesmente RV, é o elemento que melhor se adéqua ao que se pretende comunicar. _Charts_ têm _marcadores_ e _atributos_ como seus fundamentos, como veremos em capítulos posteriores. A _apresentação visual_ concerne a todas as outras tomadas de decisão de design que constituem a anatomia da visualização, tais como a seleção da paleta de cores, a composição da obra e as características das anotações. Ambas constituem a parcela artística do autor e o âmago da disciplina. A execução disso tudo independe da ferramenta técnica utilizada. Existem diversos sistemas, pacotes, bibliotecas e linguagens disponíveis, sendo R e Python as linguagens de programação preferidas dos analistas de dados.
# 
# Por outro lado, a parte final da definição, que diz respeito à _compreensão facilitada_ dos dados, tem a ver com o processo de captura da mensagem lançada pelo contador de história (_storyteller_) ao espectador (_viewer_). Este processo envolve 3 etapas cognitivas ({numref}`fig-comprehension`, adaptada de {cite:p}`kirk2016data`):
# 
# 1. _Percepção_ (o que vejo?)
# 2. _Interpretação_ (o que significa?)
# 3. _Compreensão_ (o que significa para mim?)
# 
# 
# ```{figure} ../figs/3-steps-cognition.png
# ---
# name: fig-comprehension
# alt: As 3 fases da compreensão de uma representação visual.
# align: center
# width: 550px
# ---
# As 3 fases da compreensão de uma representação visual. Preparada por: G.P. Oliveira.
# ```

# ### Figuras feias, ruins e erradas
# 
# Diferentes versões de figuras com a mesma RV subjacente podem existir ({numref}`fig-ugly`, adaptada de {cite:p}`wilke2019fundamentals`). Porém, uma delas pode ser _feia_, outra pode ser _ruim_ e outra pode ser _errada_. Esse mecanismo tripartite é um exemplo de como podemos fazer julgamentos de trabalhos visuais. Segundo Claus Wilke, uma figura:
# 
# - _feia_ é aquela que tem problemas estéticos, apesar de clara e informativa.
# - _ruim_ é aquela que tem problemas relacionados à percepção, tais como obscuridade, confusão, complicações e enganação.
# - _errada_ é aquela que tem problemas relacionados à matemática e é objetivamente incorreta.
# 
# 
# ```{figure} ../figs/hists-lodo.png
# ---
# name: fig-ugly
# alt: Comparação de figuras.
# align: center
# width: 750px
# ---
# Comparação de figuras: A) adequada, sem problemas aparentes graves; B) versão "feia", tecnicamente correta, mas colorida inutilmente; C) versão "ruim", também tecnicamente correta, mas com marcações e gradeado destoantes; D) versão "errada", sem escala explícita e aparentemente díspar em quantidade. Preparada por: G.P. Oliveira.
# ```
# 
# 
# ```{admonition} Curiosidade
# :class: dropdown
# [_The Good, the Bad and the Ugly_](https://pt.wikipedia.org/wiki/The_Good,_the_Bad_and_the_Ugly), em português "Três homens em conflito", filme clássico de _western_ lançado em 1966 que consagrou [a trilha sonora do "assobio"](https://www.youtube.com/watch?v=1AyxDVBX2o0) de Ennio Morricone, conta a história de três homens, Tuco, Lourinho e Angel Eyes, que procuram por um tesouro. Dois deles (Tuco e Lourinho) apenas têm conhecimento de uma parte da sua localização, ao passo que Angel Eyes somente persegue os outros dois por não ter informação nenhuma. No final, o _Bom_ é o "mais ético", o _Feio_ é o "mais rude e de aparência tosca" e o "mau" é o "mais displicente".
# ```

# In[2]:


# JSON TAG: remove-cell

import matplotlib.pyplot as plt, numpy as np, pandas as pd

np.random.seed(100)
x = np.random.randint(0,50,20)

fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(10,6))
plt.suptitle('Lodo tratado por tipo')

# (0,0)
n, bins, patches = ax[0,0].hist(x,bins=5,width=5)
ax[0,0].set_xticks(bins[:-1]+2.5)
ax[0,0].set_xticklabels(['Comp','Inc','DigA','DigAn','Bio'],fontsize=8)

ax[0,0].spines['top'].set_visible(False)
ax[0,0].spines['right'].set_visible(False)
ax[0,0].spines['left'].set_visible(False)

ax[0,0].grid(axis='y',color='w',alpha=0.8,ls='-')
ax[0,0].set_ylabel('volume',fontsize=10) 
ax[0,0].yaxis.label.set_color('k')

ax[0,0].set_title('A',fontsize=10)

# (0,1)
n, bins, patches = ax[0,1].hist(x,bins=5,width=5)
ax[0,1].set_xticks(bins[:-1]+2.5)
ax[0,1].set_xticklabels(['Comp','Inc','DigA','DigAn','Bio'],fontsize=8)

ax[0,1].spines['top'].set_visible(False)
ax[0,1].spines['right'].set_visible(False)
ax[0,1].spines['left'].set_visible(False)

ax[0,1].grid(axis='y',color='y',alpha=1.0,ls='-')
ax[0,1].set_ylabel('volume',fontsize=10) 
ax[0,1].tick_params(axis='y', colors='gray') 
ax[0,1].yaxis.label.set_color('gray')

cm = ['#EE2C2C','#E8A75A','#1590B2','#580080','#56887D']
for c, p in zip(np.arange(5), patches):
    plt.setp(p, 'facecolor', cm[c])

ax[0,1].set_title('B',fontsize=10)

# (1,0)
n, bins, patches = ax[1,0].hist(x,bins=5,width=5)
ax[1,0].set_xticks(bins[:-1]+2.5)
ax[1,0].set_xticklabels(['Comp','Inc','DigA','DigAn','Bio'],fontsize=8)

ax[1,0].spines['top'].set_visible(False)
ax[1,0].spines['right'].set_visible(False)
ax[1,0].spines['left'].set_visible(False)

ax[1,0].grid(axis='y',color='k',alpha=0.5,ls='--')
ax[1,0].set_ylabel('volume',fontsize=10) 
ax[1,0].yaxis.label.set_color('k')
ax[1,0].tick_params(axis='y', colors='r') 

xt = bins[:-1]+2.5
yt1 = [4,3,4,5,4]
dy1 = [-0.12,0.2,-0.14,0.15,0.16]

#yt2 = [2,2,2,2,2]
#dy2 = [-0.16,-0.11,0.14,0.08,-0.16]

for i in range(len(xt)):
    ax[1,0].annotate(f'{yt1[i]}',(xt[i],yt1[i] + dy1[i]),c='r')
    #ax[1,0].annotate(f'{yt2[i]}',(xt[i],yt2[i] + dy2[i]))

ax[1,0].set_title('C',fontsize=10)

# (1,1)
np.random.seed(140)
x = np.random.randint(0,50,20)
n, bins, patches = ax[1,1].hist(x,bins=5,width=5)
ax[1,1].set_xticks(bins[:-1]+2.5)
ax[1,1].set_xticklabels(['Comp','Inc','DigA','DigAn','Bio'],fontsize=8)

ax[1,1].set_yticklabels([])
ax[1,1].set_yticks([])

ax[1,1].spines['top'].set_visible(False)
ax[1,1].spines['right'].set_visible(False)
ax[1,1].spines['left'].set_visible(False)

ax[1,1].grid(axis='y',color='k',alpha=0.5,ls='--')
ax[1,1].set_ylabel('volume',fontsize=10) 
ax[1,1].yaxis.label.set_color('k')
ax[1,1].set_yticks = []

ax[1,1].set_title('D',fontsize=10)

plt.savefig('../figs/hists-lodo.png',dpi=300);


# ### _Dataviz_, o pensamento visual e o bom plot
# 
# A era da informação hoje entende que a visualização de dados, comumente conhecida pelo pseudônimo _dataviz_ (de _data visualization_), é uma disciplina obrigatória para um novo modo de pensar: o _pensamento visual_. No mundo dos negócios, pensar visualmente é ser capaz de construir representações visuais com grande potencial atrativo. Para empresas competitivas, a mensagem clara e acessível transmitida graficamente é uma das grandes vantagens de _marketing_.
# 
# Como já dissemos, adjetivar um plot com características visuais apreciáveis como "bom" é uma questão de seguir princípios que ajudam a definir por que construi-lo de um jeito e não de outro. A _Matriz da Boa Representação Visual_ ({numref}`fig-good-charts`, adaptada de {cite:p}`berinato2019harvard`), sugere que um plot considerado "bom" deve aproximar-se cada vez mais da quina superior direita, onde reside a perfeição.
# 
# ```{figure} ../figs/good-chart-matrix.png
# ---
# name: fig-good-charts
# alt: Matrix da Boa Representação Visual.
# align: center
# width: 400px
# ---
# Matrix da Boa Representação Visual. Preparada por: G.P. Oliveira.
# ```

# ### Os princípios de Tufte
# 
# [Edward Tufte](https://www.edwardtufte.com/tufte/), um estatístico americano reconhecido como o maior expert em visualização de dados estatísticos da atualidade, escreveu diversos livros sobre excelência visual, visualização da informação quantitativa e arte em imagens. Tufte destaca uma série de critérios que, se obedecidos, garantirão excelentes plots e gráficos. Ele defende que uma RV eficaz mistura substância, estatística e arte (design), caracterizando-se como uma apresentação bem elaborada de dados interessantes. Para Tufte, o espectador deve compreender o maior número de ideias em um intervalo de tempo curto olhando para algo que usa pouca tinta e ocupa o menor espaço possível. 
# 
# Na visão de Tufte ({cite:p}`tufte1985visual`,{cite:p}`tufte1990envisioning`), a RV excelente deve:
# 
# - apresentar dados;
# - induzir o espectador a pensar a substância da RV e não os métodos ou técnicas que a estruturaram;
# - evitar distorcer os dados;
# - apresentar muitos números em um espaço mínimo;
# - tornar grandes dados coerentes;
# - encorajar os olhos a compararem diferentes partes dos dados;
# - revelar os dados em vários níveis de detalhe, do mais amplo ao mais específico;
# - servir a um propósito claro: descrever, explorar, tabelar e decorar; e 
# - estar estreitamente vinculada às descrições estatísticas e verbais dos dados.
# 
# Alguns princípios fundamentais de Tufte incorporam todas as expectativas acima:
# 
# - _Integridade visual_: a figura não deve, de forma alguma, distorcer ou criar falsas interpretações dos dados. Isto significa que quantidades numéricas devem ser proporcionais aos elementos contidos na superfície da figura. Variações nos dados são permitidas, mas variações da figura não. Adicionalmente, deve-se manter o número de dimensões da imagem em quantidade igual ou inferior as contidas nos dados. Legendas devem ser usadas sem distorção ou ambiguidade. Tufte enfatiza que representações visuais de excelência projetadas por artistas sem nenhuma competência estatística são raras, já que a tendência de se produzir artefatos artísticos ambíguos é consideravelmente alta.
# - _Maximização da razão "tinta-dados"_: para Tufte, o _storyteller_ precisa atentar para a quantidade de elementos agregados em uma RV. Sobrecarregar a interpretação do leitor com elementos geométricos, bordas, cores de fundo, efeitos 3D, entre outros adereços, é um ponto negativo para a compreensão final. A maneira sugerida de controlar a superfluidade visual é calcular a quantidade de tinta necessária para representar os dados reais sem ambiguidade e comparar com a quantidade de tinta utilizada para enriquecer a figura com decorações. A equação para o que Tufte chamou de razão "tinta-dados" (_data-ink ratio_), aqui denotada por $\text{RTD}$ é: 
# 
# $$\text{RTD} = \dfrac{d - t}{T},$$
# 
# onde $d$, $t$, e $T$ denotam, nesta ordem, a quantidade de tinta usada para os dados, para os adereços e para ambos, no total. Maximizar a $\text{RTD}$ implica em eliminar do visual aquilo que é inútil ou não essencial.
# - _Estética_: a elegância visual só pode ser atingida ao se equilibrar a complexidade dos dados com a simplicidade do design. Para criarmos representações visuais com alto nível de profisssionalismo, é preciso muita dedicação, atenção e esmero de projeto. Ou seja, a estética perfeita só é atingida com pleno domínio do ferramental técnico e criatividade. 

# #### Integridade ou falta dela?
# 
# A {numref}`fig-integrity1` é uma representação visual que mistura gráficos de barras com a fotografia do ilustre Cristiano Ronaldo. Nada contra o lendário "CR7", mas, será que, em termos de integridade visual, seria necessária a estampa gigantesca de sua imagem ali? Ela é útil para os dados. Torna-se evidente que há muito mais peso de _marketing_ do que de dados.
# 
# Em segundo lugar, você consegue notar que a escala de valores é grosseiramente desproporcional? A barra indicadora de 10.000 unidades vendidas para o nosso "brazuca" Neymar está bastante esticada em relação às outras duas, não é?
# 
# ```{figure} ../figs/integrity1.jpeg
# ---
# name: fig-integrity1
# alt: Exemplo de falta de integridade em dados.
# align: center
# width: 400px
# ---
# Número de camisas _jersey_ de alguns jogadores vendidas. Fonte: clique [aqui](https://www.linkedin.com/pulse/edward-tuftes-six-principles-graphical-integrity-radhika-raghu/).
# ```
# 
# Diante desse problema de desproporcionalidade e marketing apelativo, há duas coisas a fazer para darmos integridade visual à nossa representação visual: elminar a imagem do jogador e corrigir a escala. Um gráfico _clean_, porém íntegro, seria como o da 
# A {numref}`fig-integrity2`
# 
# ```{figure} ../figs/integrity2.jpeg
# ---
# name: fig-integrity2
# alt: Gráfico corrigido com integridade em dados.
# align: center
# width: 500px
# ---
# Número de camisas _jersey_ de alguns jogadores vendidas. Versão corrigida para integridade visual.
# ```

# #### Maximizando a razão tinta-dados na prática
# 
# Maximizar a RTD é um processo puramente experimental e iterativo. Só chegamos a bom termo em uma RV após alterações, remoções, adições, reestruturações. O gráfico de barras da {numref}`fig-rtd1` mostra a distribuição calórica de algumas comidas "sujas". Em sua versão original, a RV é abarrotada de cores e redundâncias.
# 
# ```{figure} ../figs/rtd1.png
# ---
# name: fig-rtd1
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV 1. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```
# 
# Consideremos agora um processo iterativo que gerará uma RV minimalista a partir do melhoramento sucessivo das anteriores. Os passos são os seguintes:
# 
# - {numref}`fig-rtd2`: removemos as cores de _background_ (figura e eixos), pois nada acrescentam.
# 
# ```{figure} ../figs/rtd2.png
# ---
# name: fig-rtd2
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV 2. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```
# 
# - {numref}`fig-rtd3`: removemos redundâncias (título, legenda e designações de eixo).
# 
# ```{figure} ../figs/rtd3.png
# ---
# name: fig-rtd3
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV 3. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```
# 
# - {numref}`fig-rtd4`: removemos bordas, visto que adicionam apenas tinta.
# 
# ```{figure} ../figs/rtd4.png
# ---
# name: fig-rtd4
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV 4. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```
# 
# - {numref}`fig-rtd5`: reduzimos as cores e damos destaque a uma comida específica. No caso, _bacon_.
# 
# ```{figure} ../figs/rtd5.png
# ---
# name: fig-rtd5
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV 5. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```
# 
# - {numref}`fig-rtd6`: neste ponto, a RTD aumentou consideravelmente. Porém, podemos otimizá-la retirando efeitos 3D e sombras.
# 
# ```{figure} ../figs/rtd6.png
# ---
# name: fig-rtd6
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV 6. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```
# 
# - {numref}`fig-rtd7`: por fim, retiramos o gradeado, já que podemos indicar valores embutidos. Enfim, chegamos a uma RV minimalista.
# 
# ```{figure} ../figs/rtd7.png
# ---
# name: fig-rtd7
# alt: Exemplo de maximização da razão tinta-dados.
# align: center
# width: 400px
# ---
# Exemplo de maximização da razão tinta-dados em dados sobre comidas "sujas" - RV final. Fonte: clique [aqui](https://www.codeconquest.com/blog/data-ink-ratio-explained-with-example/).
# ```

# #### Estética: quem ajuda não deve atrapalhar
# 
# A elegância visual só pode ser atingida ao se equilibrar a complexidade dos dados com a simplicidade do design. Nas RVs representadas na {numref}`fig-aesthetics1a` e
# {numref}`fig-aesthetics1b`, o gradeado é um elemento adicional que agrava a estética dos dados representados. Porém, se ele for retirado, juntamente com outros dados, nada pode ser dito sobre as curvas. Removê-lo ajuda em algo, mas também implica em obscurecimento do que se pretende comunicar.
# 
# ```{figure} ../figs/aesthetics1a.jpg
# ---
# name: fig-aesthetics1a
# alt: Exemplo de estética.
# align: center
# width: 400px
# ---
# Exemplo de estética depauperada - com gradeado. Fonte: clique [aqui](https://jcsites.juniata.edu/faculty/rhodes/ida/graphicalIntRedes.html).
# ```
# 
# ```{figure} ../figs/aesthetics1b.jpg
# ---
# name: fig-aesthetics1b
# alt: Exemplo de estética.
# align: center
# width: 400px
# ---
# Exemplo de estética depauperada - sem gradeado. Fonte: clique [aqui](https://jcsites.juniata.edu/faculty/rhodes/ida/graphicalIntRedes.html).
# ```
# 
# O caso da {numref}`fig-aesthetics2` já é de desequilíbrio nas escalas dos eixos de lateralidade e de profundidade em virtude da visualização tridimensional. O gráfico lembra uma cidade infestada de prédios. A questão é: dá para ver o que tem atrás dos "arranha-céus" alaranjados? Este é um exemplo de visualização multidimensional que poderia ser melhor representada menor dimensão.
# 
# ```{figure} ../figs/aesthetics2.jpg
# ---
# name: fig-aesthetics2
# alt: Exemplo de estética.
# align: center
# width: 400px
# ---
# Exemplo de estética depauperada - gráfico de barras em 3D com dadoos obscuros.
# ```
# 

# ## Ferramentas técnicas do curso
# 
# Neste curso, trabalharemos essencialmente com Python 3.x como a linguagem de programação básica e com uma diversidade de pacotes para construção de plotagens e utilidades. A forma recomendada de prosseguir com a instalação das ferramentas é criando um ambiente virtual `conda` a partir do arquivo de configurações disponibilizado pelo professor e trabalhar as tarefas como um projeto de desenvolvimento.
# 
# ### Criação do novo ambiente
# 
# Para criar um ambiente mínimo para o curso, execute o comando: 
# 
# ```
# conda env create --file dataviz.yml
# ```
# 
# ```{admonition} Dica
# :class: tip
# Crie um novo arquivo chamado `dataviz.yml`, então copie o conteúdo do arquivo YAML abaixo e cole nele.
# ```
# 
# ```yaml
# # "dataviz.yml" é um arquivo-modelo YAML para construir o ambiente "dataviz".
# # Para a sua correta execução, é necessário que a variável de ambiente "CONDA_PREFIX" seja configurada
# # para apontar para o diretório padrão físico em seu computador onde "dataviz" será criado.
# 
# name: dataviz
# channels:
#   - anaconda
#   - conda-forge
#   - defaults
# dependencies:
#   - python=3.13
#   - numpy
#   - pandas
#   - matplotlib
#   - seaborn
#   - plotly
#   - scipy
#   - dash
#   - h5py
#   - statsmodels
#   - geopandas
#   - networkx
#   - pip
#   - pip:
#     - matplotlib-venn
#     - xhtml2pdf
#     - reportlab 
# prefix: ${CONDA_PREFIX}/dataviz
# ```
# 
# Por fim, habilite o ambiente:
# 
# ```
# conda activate dataviz
# ```
# 
# As dependências constituem pacotes essenciais para carregamento, limpeza, análise e visualização de uma enorme gama de dados. O resumo de cada um pode ser rapidamente localizado na internet. Os pacotes mais básicos para análise e visualização de dados são `numpy`, para manipulação de _arrays_ e computação vetorizada, `pandas`, para manipulação de séries e _datasets_,  e `matplotlib`, para plotagem estática de dados. Os demais são utilizados para tarefas especializadas. `seaborn` é útil para análise exploratória de dados e para visualização de dados estatísticos. `plotly` serve para propósitos de visualização interativa. `scipy` é um pacote de computação científica, com diversos métodos numéricos. `h5py` manipula arquivos no formato HDF5 (_Hierarchical Data Format_), bastante utilizados em visualização científica e armazenamento de grandes estruturas de dados. `dash` é uma API para construção de _dashboards_. `geopandas` suportam a visualização de dados geográficos. `networkx` oferece meios de plotagem de grafos e de redes complexas. `matplotlib-venn` gera diagramas de Venn. `xhtml2pdf` e `reportlab` são dedicados à manipulação de PDFs e úteis para geração de relatórios.
# 
# O ferramental Python disponível para visualização de dados é bastante vasto. Já existem hoje muitos outros pacotes baseados na linguagem para trabalhar com _big data_ multipropósito (e.g. `polars`, `hvplot`, `datashader`, `xarray`, `dask` etc.) e cada um possui pontos positivos e negativos. Em sua atividade profissional, uma ferramenta poderá ser mais adequada do que outra e será você quem dará o veredito final.
# 
# Para manter uma linha mínima de ação no escopo técnico, neste curso utilizaremos `numpy`, `pandas`, `matplotlib` e `seaborn` para a visualização estática de dados, e `plotly` para a visualização interativa. Os demais pacotes serão utilizados sob demanda ao discutirmos aplicações e exemplos mais elaborados.

# ### Exemplo aplicado
# 
# O código abaixo usa comandos do `pandas`, `matplotlib` e `seaborn` para produzir um tipo de plot conhecido em Estatística como _boxplot agrupado_ para visualizarmos a variação do preço por litro, em R$, de 6 tipos de combustíveis comercializados no estado da Paraíba por 8 operadoras durante o primeiro semestre de 2022. 
# 
# Para a plotagem, usamos parte do [_dataset_](https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda/resource/a1e1955b-f340-415d-83bf-bbce710d142b) correspondente disponibilizado pela ANP no portal [Dados Abertos](https://dados.gov.br) do Governo Federal.

# In[16]:


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


# ```{admonition} Exercício
# :class: important
# Siga as etapas propostas por Kirk ({numref}`fig-comprehension`) e faça uma análise do plot acima. O que ele diz? Ele é "feio", "ruim"? O que você interpreta a partir dos dados apresentados? A representação visual pode ser aperfeiçoada?
# ```

# ## Terminologias
# 
# Qualquer campo do conhecimento científico é dotado de conceitos, definições, taxonomias e glossários, constituindo terminologias próprias. Em visualização de dados, pelo fato de muitos termos procederem da língua inglesa, suas traduções para a língua portuguesa podem gerar sinonímia confusa. A fim de evitar percalços semânticos, utilizaremos, neste curso, alguns termos próprios (embora não desvinculados do uso comum) separados em diferentes grupos.
# 
# ### Termos para pessoas
# 
# - _Storyteller_: você, que está construindo o produto de visualização (cf. _visualiser_, _analyst_, _visualist_, _designer_).
# - _Viewer_: a pessoa que visualiza o produto construído (cf. _consumer_, _reader_, _user_).
# - _Audiência_: um grupo de espectadores ou coorte social a quem o produto de visualização é direcionado (cf. _audience_).
# 
# (sec:termos-dados)=
# ### Termos para dados
# 
# - _Dado bruto_: estado inicial de um dado coletado, recebido ou baixado de um repositório ainda não tratado ou sujeito a análises (cf. _raw data_).
# - _Fonte_: origem do dado bruto utilizado para a visualização (cf. _data source_).
# - _Dataset_: uma tabela ou coleção de tabelas dispostas como um _array_ computacional e organizadas em linhas (registros, instâncias ou itens) e colunas (variáveis, detalhes dos itens).
# - _Tipo_: a especificação de uma variável de tabela. Geralmente, um dado é _ordinal_ (obedece a uma relação de ordem), _numérico_ (manipulável por operações aritméticas) ou _categórico_ (identificado por um atributo que o difere de outro).
# - _Série_: sequência de valores assumidos por uma mesma variável em um _dataset_.
# 
# ```{admonition} Curiosidade
# :class: dropdown
# 
# A taxonomia de dados para fins de visualização da informação proposta por Ben Schneiderman em seu artigo
# científico [_The eyes have it: a task by data type taxonomy for information visualizations_](https://ieeexplore.ieee.org/document/545307), de 1996, oferece 7 tipos de dados: unidimensional, bidimensional, tridimensional, temporal, multidimensional, árvore e rede. Uma versão em PDF está disponível na [página](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf) do autor.
# ```
# 
# ### Termos para visualização
# 
# - _Projeto de visualização_: conjunto de etapas progressivas que culminam na geração de um produto de visualização.
# - _Produto de visualização_: entregável de um projeto de visualização. Em geral, será uma _representação visual de dados_.
# - _Representação visual de dados_: termo genérico que abrange as diversas formas de disposição visual de dados, que chamaremos de _plot_. Um _plot_ pode ser um traçado representativo de uma quantitidade matemática univariada (gráfico), ou a aplicação de figuras geométricas planas ou espaciais, ou ainda a impressão de formas e símbolos para fins quantitativos ou qualitativos em várias dimensões. Assim, _plots_ incorporarão diagramas, fluxogramas, dendrogramas, superfícies, dispersões, correlações, mapas etc.
# - _Outlier_: valores em uma representação visual que escapam do intervalo normal e chamam atenção do espectador por serem ou muito menores ou muito maiores do que o esperado.
# 
# ```{admonition} Curiosidade
# :class: dropdown
# Na língua inglesa, _chart_, _graph_ e _plot_ são considerados sinônimos, apesar de serem encontrados em contextos distintos. O _gráfico de barras_, por exemplo, é comumente chamado de _bar chart_ e não de _bar graph_. Todavia, _chart_ e _graph_ são ambos costumeiramente traduzidos para português como "gráfico". Além disso, _graph_ também é traduzido como "grafo", um conceito matemático que destoa da simples aplicação à visualização. O _gráfico de dispersão é outro exemplo que causa imprecisão semântica, visto que, em inglês, ele é conhecido como _scatter plot_ e não como _scatter graph_. Enquanto algumas representações possuem traduções imediatas, isto não é o caso para outras. Por esta razão, usar _plot_, ou _plotagem_, como hiperônimo para todas as representações discutidas neste curso é uma escolha justificada. Discussões sobre diferenças desses termos em inglês podem ser encontradas [aqui](https://www.wallstreetmojo.com/graphs-vs-charts/) e [aqui](https://english.stackexchange.com/questions/43027/whats-the-difference-between-a-graph-a-chart-and-a-plot).
# ```

# ## Referências
# 
# ```{bibliography}
# :filter: docname in docnames
# ```
# 
