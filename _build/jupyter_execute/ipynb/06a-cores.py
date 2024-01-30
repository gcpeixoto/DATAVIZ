#!/usr/bin/env python
# coding: utf-8

# # Cores

# Cores são constituintes fundamentais da aparência das representações visuais. Com elas, conseguimos enaltecer o estímulo visual da audiência e impactar a percepção visual dos espectadores. Variar matizes e colorações traz compreensões àquilo que desejamos mostrar. As cores, por sua vez, podem ser usadas para, principalmente:
# 
# - distinguir grupos de dados;
# - representar valores; e
# - produzir destaques (_highlights_).
# 
# Entretanto, antes de se preocupar com a decoração de nossas representações visuais, é preciso se dedicar ao significado delas {cite:p}`kirk2016data`.

# (sec:escalas-cor)=
# ## Escalas de cor
# 
# Como enunciamos, um dos objetivos de usar cores em visualização de dados é distinguir grupos através da plotagem de dados qualitativos categóricos. Para esta finalidade, podemos usar paletas de cores discretas, também chamadas de _escalas de cor qualitativas_. Essas paletas são compostas de uma quantidade limitada de cores que produzem uma percepção de "grupos finitos" de informação.
# 
# Usando a função `seaborn.color_palette()`, por exemplo, podemos invocar uma enorme quantidade de escalas de cores qualitativas do próprio módulo, ou qualquer outro _mapa de cores_ predefinido ou mesmo construído por nós. Entenderemos _mapas de cores_ mais à frente. 
# 
# A seguir, exibimos 3 escalas qualitativas com 6, 10 e 14 cores segundo a paleta padrão.

# In[18]:


from seaborn import color_palette
color_palette(n_colors=6)


# In[16]:


get_ipython().system('open /Users/gustavo/opt/anaconda3/envs/dataviz/lib/python3.9/site-packages/seaborn/palettes.py')


# In[2]:


color_palette(n_colors=10)


# In[3]:


color_palette(n_colors=14)


# Observe que neste exemplo de 14 cores, as últimas 4 são as mesmas que as primeiras 4. Isto acontece porque a paleta padrão que estamos utilizando possui apenas 10 cores. Quando solicitamos mais, ela simplesmente entra em um ciclo repetitivo. 
# 
# A paleta padrão utilizada pelo `seaborn`, chamada de `prop_cycle`, é herdada do `matplotlib 2.0`, quando passou a substituir a paleta circular anterior, baseada em 7 cores: azul, verde, vermelho, ciano, magenta, amarelo e preto (`bgrcmyk`). As cores da paleta padrão podem ser prontamente obtidas com as seguintes instruções.

# In[32]:


from matplotlib import rcParams
for c in rcParams['axes.prop_cycle'].by_key()['color']:
    print(c, end = ' ')


# A alteração das propriedades "circulares" de cor depende da API [`cycler`](https://matplotlib.org/cycler/), a qual serve para estilizações customizadas. Para maior detalhamento, consulte este [link](https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html). Para uma apresentação dos motivos por trás da escala padrão, assista este [vídeo](https://www.youtube.com/watch?v=xAoljeRJ3lU&t=1s).

# Podemos reduzir as saturações dessas paletas por uma certa proporção para criar cores menos vívidas incorporando o parâmetro `desat`. 

# In[4]:


color_palette(n_colors=6,desat=0.1)


# In[5]:


color_palette(n_colors=10,desat=0.5)


# In[6]:


color_palette(n_colors=14,desat=0.9)


# ### Paletas predefinidas
# 
# O `seaborn` possui algumas paletas de cores predefinidas que alteram as tonalidades das cores. São elas: 
# - `muted`;
# - `bright`;
# - `pastel`;
# - `dark`; e 
# - `colorblind`.

# In[7]:


color_palette('muted')


# In[8]:


color_palette('bright')


# In[9]:


color_palette('pastel')


# In[10]:


color_palette('dark')


# In[11]:


color_palette('colorblind')


# #### Paletas qualitativas

# O `matplotlib` também possui uma série de paletas de cores. Em particular, as qualitativas são:
# 
# - `Pastel1`, `Pastel2`;
# - `Paired`, `Accent`;
# - `Dark2`;
# - `Set1`, `Set2`, `Set3`; 
# - `tab10`, `tab20`, `tab20b`, `tab20c`.
# 
# Cada uma pode ser invocada pela função `seaborn.color_palette()` naturalmente:

# In[12]:


color_palette('Paired',n_colors=10)


# In[13]:


color_palette('Set1',n_colors=10)


# In[14]:


color_palette('tab20b',n_colors=10)


# ##### Exemplo de aplicação: dado qualitativo categórico
# 
# Para um exemplo aplicado, vamos plotar a malha geográfica de municípios do estado da Paraíba usando uma das escalas de cor disponíveis no `matplotlib`. Definiremos a função `plot_municipios_PB(escala)`; para trabalhar com sistemas de coordenadas existentes no módulo `cartopy`, a qual gerará uma paleta de 223 cores (uma para cada município) com base na `escala` escolhida pelo usuário e, em seguida, fará a representação visual dos dados categorizados.

# In[17]:


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from seaborn import color_palette

def plot_municipios_PB(plte):
    '''Plota a malha de municípios do estado da Paraíba a partir
       de uma escala de cores escolhida pelo usuário.'''

    # eixo e projeções
    ax = plt.axes([0, 0, .8, .8],projection=ccrs.LambertConformal())
    ax.set_extent([-35.5,-38.5,-6,-8.5], ccrs.Geodetic())  # (lat1,lat2,lon1,lon2); cobertura JPA
    ax.set_axis_off()

    # malha geográfica da PB (IBGE)
    # requer diretório de arquivos SHP
    # https://www.ibge.gov.br/en/geosciences/territorial-organization/territorial-meshes/18890-municipal-mesh.html?=&t=acesso-ao-produto
    shapename = '../data/PB_Municipios_2021/'
    shp = shpreader.Reader(shapename)
    nmun = len(shp) # no. municípios

    # plotagem dos polígonos dos municípios
    plt.title('Municípios da Paraíba',fontsize=10)
    cols = color_palette(plte,n_colors=nmun) # paleta de 223 cores

    for i,s in enumerate(shp.geometries()):    
        ax.add_geometries([s], ccrs.PlateCarree(),facecolor=cols[i], edgecolor='white');

    return shp


# In[18]:


# Plotagem com escala de cores escolhida pelo usuário
plot_municipios_PB('Paired');


# #### Paletas contínuas e demais paletas predefinidas
# 
# O `matplotlib` dispõe de outras dezenas de paletas com características diversas. Em particular, _paletas contínuas_ são aquelas que geram uma percepção de continuidade e são bastante úteis para a plotagem de dados quantitativos numéricos e dados onde prevaleça algum ordenamento. As classes de paletas do `matplotlib` são:
# 
# 1. Sequenciais com percepção de uniformidade: `viridis`, `plasma`, `inferno`, `magma` e `cividis`
# 2. Sequenciais do grupo 1: `Greys`, `Purples`, `Blues`, `Greens`, `Oranges`, `Reds`, `YlOrBr`, `YlOrRd`, `OrRd`, `PuRd`, `RdPu`, `BuPu`, `GnBu`, `PuBu`, `YlGnBu`, `PuBuGn`, `BuGn` e `YlGn`;
# 3. Sequenciais do grupo 2: `binary`, `gist_yarg`, `gist_gray`, `gray`, `bone`, `pink`, `spring`, `summer`, `autumn`, `winter`, `cool`, `Wistia`, `hot`, `afmhot`, `gist_heat` e `copper`;
# 4. Divergentes: `PiYG`, `PRGn`, `BrBG`, `PuOr`, `RdGy`, `RdBu`, `RdYlBu`, `RdYlGn`, `Spectral`, `coolwarm`, `bwr` e `seismic`;
# 5. Cíclicas: `twilight`, `twilight_shifted`, `hsv`;
# 6. Qualitativas: já vistas anteriormente.
# 7. Genéricas: `flag`, `prism`, `ocean`, `gist_earth`, `terrain`, `gist_stern`, `gnuplot`, `gnuplot2`, `CMRmap`, `cubehelix`, `brg`, `gist_rainbow`, `rainbow`, `jet`, `turbo`, `nipy_spectral` e `gist_ncar`.
# 
# 
# ```{admonition} Curiosidade
# :class: dropdown
# A maioria das escalas de cor admitem uma versão "reversa" obtida adicionando-se o sufixo `_r` à _string_ que define a escala (`cividis_r`, `hsv_r` etc.).
# ```
# 
# Não é nossa intenção explorar cada uma das paletas aqui, mas mostrar algumas aplicações. É importante notar que a escolha de paletas de cores depende de inúmeros fatores tais como: 
# 
# - natureza dos dados (p.ex. qualitativo, quantitativo, discreto, contínuo);
# - destaque (p.ex. destacar valor médio e outliers);
# - intuição (p.ex. tons de verde para tratar parâmetros métricos de sustentabilidade);
# - necessidades especiais (p.ex. público com particularidades visuais); e
# - tradição do campo do conhecimento (p.ex. cores binárias em imagens médicas).
# 
# Segundo a documentação do `matplotlib`, as escalas de cor são explicadas da seguinte forma:
# 
# 1. Sequenciais: mudanças incrementais na luminosidade e na saturação de cor, muitas vezes usando um único matiz; deve ser usado para representar dados que possuam alguma ordenação.
# 2. Divergentes: mudança na luminosidade e possivelmente na saturação de duas cores diferentes que se encontram no meio a uma cor insaturada; deve ser usada quando a informação que está sendo plotada tem um valor médio crítico ou quando os dados se desviam em relação a zero.
# 3. Cíclicas: mudança na luminosidade de duas cores diferentes que se encontram no meio e início/fim em uma cor insaturada; deve ser usado para valores relativos a fenômenos cíclicos/periódicos, tais como ângulo de fase, direção do vento ou hora do dia.
# 4. Qualitativas: cores diversas; deve ser usada para representar informações que não possuem ordem ou relacionamentos.
# 
# A seguir mostramos o visual de algumas dessas escalas:

# ##### Sequenciais com percepção de uniformidade

# In[19]:


color_palette('viridis',n_colors=12)


# In[20]:


color_palette('magma',n_colors=12)


# ##### Sequenciais do grupo 1

# In[21]:


color_palette('Oranges',n_colors=12)


# In[22]:


color_palette('Blues',n_colors=12)


# In[23]:


color_palette('YlOrRd',n_colors=12)


# ##### Sequenciais do grupo 2

# In[24]:


color_palette('bone',n_colors=12)


# In[25]:


color_palette('hot',n_colors=12)


# In[26]:


color_palette('copper',n_colors=12)


# ##### Divergentes

# In[27]:


color_palette('RdBu',n_colors=12)


# In[28]:


color_palette('Spectral',n_colors=12)


# In[29]:


color_palette('seismic',n_colors=12)


# ##### Cíclicas

# In[30]:


color_palette('twilight',n_colors=12)


# In[31]:


color_palette('twilight_shifted',n_colors=12)


# In[32]:


color_palette('hsv',n_colors=12)


# ##### Genéricas

# In[33]:


color_palette('prism',n_colors=12)


# In[34]:


color_palette('terrain',n_colors=12)


# In[35]:


color_palette('rainbow',n_colors=12)


# ```{admonition} Curiosidade
# :class: dropdown
# Diversos pacotes que lidam com mapas de cores podem ser encontrados (https://matplotlib.org/mpl-third-party/#colormaps-and-styles)[aqui].
# ```

# (sec:aplicado-quantitativo)=
# ##### Exemplo aplicado: dado quantitativo numérico
# 
# Neste segundo exemplo aplicado, recuperamos os valores das áreas (em quilômetros quadrados) de todos os municípios do estado da Paraíba a partir dos arquivos de geolocalização e construímos um gráfico de dispersão ordenado. A representação visual mostra a variação do escore padronizado (também conhecido como Fator Z, ou _Z-score_) das áreas dos municípios. Um Fator Z igual a zero representa a média do conjunto. Valores de Fator Z negativos representam municípios cuja área é menor do que a média do estado; positivos, municípios com área acima da média. 
# 
# Além disso, escolhemos uma escala de cor divergente que muda a tonalidade consoante variação do Fator Z. Os dados ordenados permitem que detectemos rapidamente os municípios de menor e maior extensão territorial.Observa-se pelo visual que, Bonito de Santa Fé, Mãe D'Água e Araçagi parecem disputar a posição média, mas é evidente que Lucena e Pombal possuem, nesta ordem, a menor e maior variação em relação à média.

# In[42]:


from matplotlib.pyplot import subplots
from seaborn import set_palette, lineplot
from scipy.stats import zscore
from pandas import DataFrame
import cartopy.io.shapereader as shpreader

# recupera dados do shapefile
shp = shpreader.Reader('../data/PB_Municipios_2021/')
nmun = len(shp)
CD, NM, AREA = [], [], [] 
for mun in range(nmun):
    CD.append(shp._data[mun]['CD_MUN'])
    NM.append(shp._data[mun]['NM_MUN'])
    AREA.append(shp._data[mun]['AREA_KM2'])
    
# converte dados de área para float e cálcula escore padronizado
df = DataFrame({'CD':CD,'NM':NM,'AREA':AREA})
df['AREA'] = df['AREA'].apply(lambda x: float(str(x).replace('.','')))
df['Z'] = zscore(df['AREA'])
df = df.sort_values(by='Z')

# paleta de cores
set_palette("PiYG")

# figura
fig, ax = subplots(1,1,figsize=(1,30),constrained_layout=False)
f = lineplot(data=df,y='NM',x='Z',marker='o',markersize=7,hue="Z",linewidth=0,ax=ax)

# linha média 
ax.axvline(x=0,color='#CE408E',lw=1.2,alpha=0.8)

# decoração
ax.axis('equal'); 
ax.grid(axis='both'); 
ax.tick_params(axis='both', labelsize=6)
ax.set_xlim(-3.5,3.5); 
ax.set_ylim(nmun+0.1,-0.5)

ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.get_legend().remove()

ax.set_title('Escore padronizado: área [km2]',fontsize=8)
ax.set_xlabel('Z-score',fontsize=8); 
ax.set_ylabel('Município - PB',fontsize=8);


# De fato, uma rápida investigação no _dataframe_ permite-nos asseverar o que foi dito sobre Lucena e Pombal e afirmar com mais certeza que Araçagi disputa, na verdade, com Solânea a extensão média, visto que a inflexão do Fator Z ocorre entre as duas localidades.

# In[192]:


df['NM'][df['Z'].idxmin()], df['AREA'][df['Z'].idxmin()]


# In[193]:


df['NM'][df['Z'].idxmax()], df['AREA'][df['Z'].idxmax()]


# In[209]:


df[(df['Z'] > -0.005) & (df['Z'] < 0.005)]


# ## Modelos de cor
# 
# As cores podem ser representadas de forma abstrata através de um modelo matemático baseado em ênuplas geralmente de 3 ou 4 coordenadas. Ou seja, de forma mais geral, uma cor é uma estrutura do tipo $c = (c_1,c_2,c_3)$, ou $c = (c_1,c_2,c_3,c_4)$. Quando cada uma das componentes $c_i$ são associadas a aspectos da percepção visual, elas podem ter diferentes interpretações e dar origens a um _espaço de cores_. Porém, antes de adentrarmos em particularidades, vamos entender brevemente o aspecto físico das cores e o que, de fato, é uma cor.

# (sec:optica-cor)=
# ### Óptica, ondas e cores
# 
# _Cor_ é o nome que damos à qualidade perceptiva da luz, que se dá por uma resposta subjetiva do cérebro quando a retina de nossos olhos é estimulada. A nossa percepção das cores baseia-se em nossa sensibilidade a ondas eletromagnéticas com frequencias distintas que se misturam para produzir respostas em nossos "cones visuais" (células receptoras localizadas na retina). O espectro de energia visível – gráfico de intensidade vs. comprimento de onda (ou frequencia) – é caracterizado por comprimentos de onda na faixa de 400 - 700 nm. Esta faixa de valores determina o que chamamos de "luz visível", que cobre matizes que vão do violeta ao vermelho. Valores abaixo do espectro visível constituem a chamada "luz ultravioleta" e acima, a "luz infravermelha".
# 
# Na retina, temos 3 "cones" (células fotoreceptoras) que respondem a estímulos em três regiões do espectro visível:
# 
# - Cone _S_ (_short_), que é sensível a ondas curtas com pico em torno de 440 nm (azul).
# - Cone _M_ (_medium_), que é sensível a ondas médias com pico em torno de 540 nm (verde).
# - Cone _L_ (_long_), que é sensível a ondas longas com pico em torno de 580 nm (vermelho).
# 
# Os cones _M_ e _L_ respondem a praticamente todos os comprimentos de onda do espectro visível, enquanto o cone _S_ é limitado a comprimentos de até 550 nm. Descrevendo-se por $(S,M,L)$ a tripleta de estímulos no em um espaço Euclidiano 3D, é possível definir o _espaço de cores dos triestimular_ (_tristimulus color space_), o qual determina o espaço de cores do olho humano. Como veremos adiante, cores e espaços de cor estão intimamente ligados ao conceito de _espaço vetorial_, estudados na disciplina Álgebra Linear.
# 
# As figuras abaixo simulam o comportamento do espectro e dos cones. A partir daí, algumas cores _monocromáticas_ (únicas) foram historicamente definidas, embora os comprimentos de onda de fronteira que as definem possuam variação. De acordo com o _CRC Handbook of Physics (1966)_, as 6 bandas de ondas do espectro que atribuem nomes a cores fundamentais que conhecemos são:
# 
# - Vermelho: 647 - 700;
# - Laranja: 585 - 647;
# - Amarelo: 575 - 585;
# - Verde: 491 - 575;
# - Azul: 424 - 491; e
# - Violeta: 400 - 424.

# ```{admonition} Curiosidade
# :class: dropdown
# As cores familiares citadas anteriormente são aquelas exibidas no fenômeno do arco-íris, também chamadas de _cores espectrais_. _Spectrum_ é a palavra latina para "aparência", usada por Isaac Newton no final do século XVII para caracterizar as cores produzidas pela luz visível. Essas cores são monocromáticas, no sentido de que existem por apenas um comprimento de onda único, possuem 100% de pureza e são completamente saturadas. Misturando as cores espectrais, podemos descrever qualquer cor. Os nomes das cores espectrais possuem raízes históricas anglo-saxãs e provêm de monossílabos. Uma discussão interessante sobre as cores pode ser encontrada [aqui](https://physics.info/color/).
# ```

# In[56]:


from numpy import linspace, random
import matplotlib.pyplot as plt, matplotlib.ticker as mticker
from seaborn import kdeplot
from scipy import signal

# faixa de comprimento de onda (nm)
x = linspace(250, 1000, 500)

# figura do espectro
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(211, facecolor='k')
ax.set_xlim(250,1000); ax.set_ylim(-2,2)

# regiões do espectro
ax.text(275, 0.0, 'ultra violeta', color='w', fontdict={'fontsize': 10})
ax.text(550, 0.0, 'visível', color='k', fontdict={'fontsize': 10})
ax.annotate('', (400, -0.3), (750, -0.3), arrowprops={'arrowstyle': '<|-|>', 'color': 'w', 'lw': 2})
ax.text(810, 0.0, 'infra vermelha', color='w', fontdict={'fontsize': 10})
ax.axvline(400, -2, 2, c='w', ls='--')
ax.axvline(750, -2, 2, c='w', ls='--')

# legendas de eixos
ax.yaxis.set_visible(False)
ax.set_xlabel(r'$\lambda/\mathrm{nm}$')

# simulação de intervalos de cores
rainbow_rgb = { (400, 440): '#8b00ff', (440, 460): '#4b0082',
                (460, 500): '#0000ff', (500, 570): '#00ff00',
                (570, 590): '#ffff00', (590, 620): '#ff7f00',
                (620, 750): '#ff0000'}
for wv_range, rgb in rainbow_rgb.items():
    ax.axvspan(*wv_range, color=rgb, ec='none', alpha=1)

# Baseado em: https://scipython.com/book/chapter-7-matplotlib/examples/a-depiction-of-the-electromagnetic-spectrum/

# simulacro dos cones S,M,L
# considera distribuições normais com média nos picos de sensibilidade
# desvio de 70 e sampling de 1000
random.seed(1)
S = random.normal(440,70,1000) 
L = random.normal(540,70,1000) 
M = random.normal(580,70,1000) 

# plotagem das curvas dos cones
ax2 = fig.add_subplot(212)
kdeplot(S,ax=ax2,color='blue',fill=True,label='cone S')
kdeplot(L,ax=ax2,color='green',fill=True,label='cone L')
kdeplot(M,ax=ax2,color='red',fill=True,label='cone M')

# decoração: legenda e eixos
yt = ax2.get_yticks().tolist()
ax2.yaxis.set_major_locator(mticker.FixedLocator(yt))
ax2.set_yticklabels([f'{i:.1f}' for i in linspace(0,1.4,len(yt))]);
ax2.set_xlabel(r'$\lambda/\mathrm{nm}$')
ax2.set_ylabel('sensibilidade')
ax2.legend(fontsize=8);


# A cor da luz que emana de objetos origina-se por processos físicos. Podemos citar, por exemplo
# 
# - _emissão_, quando o objeto é uma fonte de luz com cor determinada pelo seu espectro;
# - _reflexão_, quando algumas frequencias são refletidas pelo objeto;
# - _transmissão_, quando algumas frequencias são transmitidas através do objeto;
# - _interferência_, quando algumas frequencias são amplificadas e outras atenuadas;

# ### Modelos aditivos e subtrativos
# 
# #### RGB
# 
# O modelo de cor _RGB_ assume que uma cor é identificada por uma tripleta do tipo $c = (r,g,b)$, em que $r$, $g$ e $b$ correspondem a proporções de vermelho, verde e azul, respectivamente, que são consideradas cores primárias. Quando $0 \leq r,g,b \leq 1$, podemos representar cada cor no modelo _RGB_ por um vetor do espaço 3D com origem em $(0,0,0)$ e extremidade imersa no "cubo unitário" formado pelos eixos $r$, $g$ e $b$. 
# 
# Geometricamente, a cor preta seria então representada justamente pelo vetor $\vec{o} = (r=0,g=0,b=0)$, o que remete à ausência de luz, em certo sentido, razão pela qual preto não é considerada uma cor propriamente dita. Analogamente aos vetores canônicos $\vec{i}$, $\vec{j}$ e $\vec{k}$ do espaço 3D, os vetores $(1,0,0)$, $(0,1,0)$ e $(0,0,1)$ formariam uma base para que, a partir de tonalidades das cores vermelho, verde e azul. A partir disso, é imeditado reconhecer que, segundo o modelo _RGB_, qualquer cor é dada por uma combinação linear de tonalidades de $r$, $g$ e $b$, ou seja:
# 
# $$\vec{c} = r(1,0,0) + g(0,1,0) + b(0,0,1)$$
# 
# Nestes termos, o vetor $\vec{c_0} = (0,0,0)$ seria a cor "preto", o vetor $\vec{c_1} = (1,1,1)$ seria "branco", a família de vetores $\vec{c_g} = k\vec{c_0}, \ \ 0 < k < 1$, determinaria os "tons de cinza", e qualquer outra combinação, as demais cores. Entretanto, vale ressaltar que o olho humano é limitado. Ele consegue distinguir cerca de 7 - 10 milhões de cores. Embora seja uma quantidade extremamente grande, isso impõe, de certa forma, finitude sobre os valores de $r$, $g$ e $b$. 
# 
# Nos sistemas digitais modernos, os valores de $r$, $g$ e $b$ limitam-se aos números inteiros positivos entre 0 e 255, inclusive. Isto é, em termos de "voxels" discretos ("pixels volumétricos"), o nosso "cubo unitário" de cores infinitas seria reduzido a uma espécie de cubo mágico capaz de identificar, no máximo 256 x 256 x 256 = 16.777.216 cores (aproximadamente 16 milhões!). A {numref}`fig-rgb-cube` (veja [aqui](https://social.technet.microsoft.com/wiki/contents/articles/20990.vb-net-generate-color-sequences-using-rgb-color-cube.aspx)), traz uma representação geométrica do cubo RGB.
# 
# ```{figure} ../figs/rgb-cube.jpg
# ---
# name: fig-rgb-cube
# alt: Cubo RGB.
# align: center
# width: 550px
# ---
# Cubo de cores RGB: representação geométrica do espectro de cores possíveis para valores 0 - 255.
# ```
# 
# 
# ```{admonition} Curiosidade
# As mais de 16 milhões de cores _RGB_ que vemos em qualquer tela _True Color_ moderna equivalem a ter imagens processadas com 8 bits por canal, i.e. $(2^8)^3$ cores. Veja uma discussão interessante entre _bits_ e cores neste [post](https://docs.krita.org/en/general_concepts/colors/bit_depth.html).
# ```
# 
# RGB é um _modelo aditivo_ ({numref}`fig-cores-aditivas`), significando que a cor percebida pode ser representada pela soma de valores numéricos de suas componentes, como já fizemos acima. Neste modelo, vermelho, verde e azul são chamadas _cores primárias_. Como a cor preta equivale a um "elemento neutro", pelo modelo aditivo, podemos escrever, algebricamente,
# 
# - preto + vermelho = vermelho
# - preto + verde = verde
# - preto + azul = azul.
# 
# Entretanto,
# 
# - vermelho + verde = amarelo
# - verde + azul = ciano
# - azul + vermelho = magenta
# - vermelho + verde + azul = branco
# 
# ```{figure} ../figs/cores-aditivas.png
# ---
# name: fig-cores-aditivas
# alt: Cores aditivas.
# align: center
# width: 550px
# ---
# Modelo fundamental de mistura aditiva de cores RGB.
# ```
# 
# #### CMYK
# 
# Diferentemente do modelo _RGB_, o modelo de cor _CMYK_ assume que uma cor é identificada por uma quadripleta do tipo $c = (c,m,y,k)$, em que $c$, $m$, $y$, e $k$ correspondem a proporções de ciano, magenta, amarelo e preto, respectivamente. As três primeiras são consideradas _cores subtrativas primárias_ e preto uma quarta componente que gera tonalidades escuras. Por isso, este modelo também é conhecido como _CMY_. 
# 
# As cores subtrativas ({numref}`fig-cores-subtrativas`) agem em complementaridade às aditivas primárias e servem como filtros que as absorvem. Assim, ciano, magenta e amarelo são cores complementares a vermelho, verde e azul, nesta ordem. O modelo CMYK é preferível para impressão porque o espectro de cores CMYK é significativamente menor e composto por pigmentos, ao passo que RGB é preferível para telas e dispositivos eletrônicos por ser composto por luz.
# 
# A ausência de pigmentos é o papel branco. Isto significa que o papel permanece "branco" quando iluminado pela luz branca. Adicionar pigmentos a ele é como subtrair certos comprimentos de onda. Então, algebricamente:
# 
# - branco - vermelho = ciano
# - branco - verde = magenta
# - branco - azul = amarelo.
# 
# Porém,
# 
# - vermelho + ciano = branco
# - verde + magenta = branco
# - azul + amarelo = branco
# 
# e 
# 
# - ciano + magenta = azul
# - magenta + amarelo = vermelho
# - amarelo + ciano = verde
# - ciano + magenta + amarelo = preto
# 
# ```{figure} ../figs/cores-subtrativas.png
# ---
# name: fig-cores-subtrativas
# alt: Cores subtrativas.
# align: center
# width: 550px
# ---
# Modelo fundamental de mistura subtrativa de cores CMY/K.
# ```

# ### Modelos geométricos
# 
# Outros diversos modelos de cor tridimensionais em formatos cônicos, cilíndricos ou esféricos foram desenvolvidos ao longo do tempo, tais como HSL, HSV, HSI, HCL, HSB, NCS, XYZ, entre outros. A {numref}`fig-color-solid-comparison` (disponível [aqui](https://commons.wikimedia.org/wiki/File:Color_solid_comparison_hsl_hsv_rgb_cone_sphere_cube_cylinder.png)) exibe os modelos HSL e HSV em formas geométricas diferentes. Desses, o HSL (_Hue_, _Saturation_, _Luminosity_) é considerado um dos mais acessíveis para aplicação em visualização de dados. Ele é uma representação cilíndrica do modelo RGB. Portanto, nós o consideraremos para estudo.
# 
# ```{figure} ../figs/color-solid-comparison.png
# ---
# name: fig-color-solid-comparison
# alt: Comparador de modelos.
# align: center
# width: 550px
# ---
# Modelos HSL e HSV com variadas representações geométricas.
# ```

# #### HSL
# 
# O modelo HSL também é tridimensional. Suas componentes são:
# 
# - _Hue_ (matiz), que varia na direção azimutal do cilindro e define a cor "verdadeira". Para o modelo CIECAM02 de colorimetria, o matiz é tecnicamente definido como _"o grau com que um estímulo pode ser descrito como semelhante ou diferente de estímulos descritos como vermelho, laranja, amarelo, verde, azul ou violeta"_. No sistema cilíndrico de coordenadas, a cor vermelha primária (matiz puro) está na coordenada 0 grau, a cor verde primária em 120 graus e a azul em 240 graus. O matiz é um atributo qualitativo da cor porque é definido por diferença e não por escala. Não existem _tints_, _shades_ ou _tints_ (vide {numref}`Seção %s <sec:misturas-cor>`).
# - _Saturation_ (saturação), que varia na direção radial do cilindro e define a pureza do matiz. A cor plenamente saturada é _vívida_ (_vivid_). À medida que a insaturamos até o estado de tons de cinza, ou _acromaticidade_, ou _neutralidade_ (eixo central do cilindro), a cor torna-se _muda_ (_muted_). Portanto, um matiz com 0% de saturação neutro (mudo), ao passo que um matiz com 100% de saturação é puro (vívido). A saturação é um parâmetro quantitativo da cor.
# - _Luminosity_ (luminosidade), que define a direção axial do cilindro e define o contraste do matiz. A luminosidade, tecnicamente, não é sinônimo de brilho, mas ela pode ser entendida como um controlador entre tons claros e escuros. Assim como a saturação, a luminosidade também é um parâmetro quantitativo da cor.
# 
# Abaixo, utilizamos as funções `seaborn.palplot()` e `seaborn.hls_palette` para demonstrar variações dos valores das componentes $h$, $s$, e $l$ no modelo de HSL, no qual a cor é uma tripleta em coordenadas cilíndricas dada por $c=(h,s,l)$.
# 
# - Variação de matizes com 100% de saturação e luminosidade média.

# In[57]:


from seaborn import palplot, hls_palette
# cores puras do arco-íris
palplot(hls_palette(n_colors=5, h=0, s=1, l=0.5)) 


# In[58]:


# matiz 33%
palplot(hls_palette(n_colors=5, h=0.5, s=1, l=0.5)) 


# In[59]:


# matiz 66%
palplot(hls_palette(n_colors=5, h=0.1, s=1, l=0.5)) 


# - Matiz 100% com variação de saturação e luminosidade média.

# In[60]:


# saturação 80%
palplot(hls_palette(n_colors=5, h=1, s=.75, l=0.5)) 


# In[61]:


# saturação 50%
palplot(hls_palette(n_colors=5, h=1, s=.5, l=0.5)) 


# In[62]:


# saturação 10%
palplot(hls_palette(n_colors=5, h=1, s=.1, l=0.5)) 


# - Matiz e saturação 100% e luminosidade variável.

# In[63]:


# luminosidade 90%
palplot(hls_palette(n_colors=5, h=1, s=1, l=.9)) 


# In[64]:


# luminosidade 40%
palplot(hls_palette(n_colors=5, h=1, s=1, l=.4)) 


# In[65]:


# luminosidade 10%
palplot(hls_palette(n_colors=5, h=1, s=1, l=.1)) 


# ### Cores em código HEX
# 
# A representação de cores por código hexadecimal (_hex codes_) emergiu como um sistema prático para trabalhar com desenvolvimento _web_. Entretanto, passou a ser utilizado para diversos fins em visualização de dados devido à sua simplicidade de uso e facilidade de compreensão. Uma tripleta HEX é um número de 6 dígitos (3 bytes) hexadecimais do tipo `AABB00` bastante utilizada em linguagens HTML e CSS para estilizar páginas da internet e também em artes gráficas. Em geral, usa-se uma tralha (`#`) antes do código por razões sintáticas.
# 
# O código HEX nada mais é do que uma representação implícita do modelo RGB. Os dígitos 1 e 2 (byte 1) controlam a proporção de vermelho, 3 e 4 a proporção de verde (byte 2), e 5 e 6 a proporção de azul (byte 3). Como o sistema hexadecimal admite os dígitos de 0 a 9 e as letras de A a F (equivalentes aos dígitos de 10 a 15), existem exatamente 16 possibilidades por dígito de _hex code_, ou seja até $16^6 = 16.777.216$ cores representáveis.
# 
# Para se converter valores RGB em HEX, devemos adotar as coordenadas discretas de 0 a 255 ou converter a escala 0 - 1 para 0 - 255 multiplicando o número por 255 e, então realizar a divisão inteira por 16. O quociente da divisão equivale ao primeiro dígito, o resto ao segundo. Fazendo o mesmo para cada coordenada, obteremos o _hex code_ correspondente.
# 
# #### Exemplo de conversão RGB > HEX
# 
# Para a cor RGB(1,0.5,0.3): 
# 
# - multiplicamos por 255 para ter RGB(255,127,76). _Obs.: se a tupla já for inteira, este passo é ignorado._
# - realizamos a divisão inteira por componente para obter a tupla de quocientes (15,7,4);
# - tomamos o resto da divisão inteira por componente para obter a tupla de restos (15,15,12);
# - convertemos os dígitos maiores do que 9 para letras nas tuplas para obter (F,7,4) e (F,F,C);
# - juntamos as tuplas elemento a elemento para formar os bytes chegando ao _hex code_ FF7F4C
# 
# Abaixo, plotamos dois retângulos especificando as cores por tupla RGB e código HEX para compararmos o resultado.

# In[111]:


from matplotlib.pyplot import subplots
from matplotlib.patches import Rectangle

fig, ax = subplots(1,2,figsize=(8,1),constrained_layout=True)

# tupla de cor (r,g,b,a), com a = opacidade
ax[0].add_patch(Rectangle(xy=(0,0),width=1, height=1, color=(1,0.5,0.3,1.0)))
ax[0].text(0.35,0.5,'RGB(255,127,76)',fontdict={'color':'k'})
ax[0].set_axis_off()

# cor com hex code
ax[1].add_patch(Rectangle(xy=(0,0),width=1, height=1, color='#FF7F4C'))
ax[1].text(0.4,0.5,'#FF7F4C',fontdict={'color':'k'})
ax[1].set_axis_off()


# Uma função para converter tuplas RGB em código HEX poderia ser codificada conforme abaixo. Você pode aperfeiçoá-la para tratar a exceção do caso em que o usuário entra com valores numéricos válidos, porém misturados entre tipos `int` e `float`, ou modificar os argumentos de entrada para a forma `(r: int, g: int, b: int)`.

# In[112]:


def rgb2hex(rgb : tuple):
    '''Conversor simples de cor RGB para HEX code'''

    from numpy import asarray, array

    rgb = asarray(rgb)

    # checking
    if all((rgb >= 0) & (rgb <= 1)):
        rgb = array(rgb*255,dtype=int)

    elif all((rgb/255 >= 0) & (rgb/255 <= 1)): #TODO caso (int,float,float)
        pass

    else:
        raise ValueError('Tupla RGB deve conter valores entre [0,1] ou [0,255].')

    # conversão
    q = rgb // 16
    q = [hex(qi).removeprefix('0x') for qi in q]

    r = rgb % 16
    r = [hex(ri).removeprefix('0x') for ri in r]

    # string
    hex_ = '#'
    for i in range(3):
        hex_ += q[i] + r[i]

    return hex_   


# Pelos testes abaixo, conseguimos verificar que a função se comporta como esperaríamos tanto para tuplas de valores fracionados quanto para tuplas de valores inteiros (0 - 255).

# In[113]:


# teste 1
rgb = (1,0.5,0.3)
rgb2hex(rgb)


# In[114]:


# teste 2
rgb = (255,127,76)
rgb2hex(rgb)


# #### Exemplos de cores CSS
# 
# A seguir plotamos um mosaico das cores CSS predefinidas do `matplotlib` e seus _hex codes_.

# In[66]:


from matplotlib.colors import CSS4_COLORS
from matplotlib.pyplot import subplots
from matplotlib.patches import Rectangle

fig, ax = subplots(37,4,figsize=(10,8),constrained_layout=True)
fig.suptitle('Cores CSS predefinidas do matplotlib e seus hex codes',fontsize=8)

# cores CSS
css = CSS4_COLORS
ck,cv = list(css.keys()),list(css.values())

# mosaico de cores: len(css)/4 = 37 x 4
for k in range(1,5):
    nms = ck[(k-1)*37:k*37]
    cols = cv[(k-1)*37:k*37]
    for a in range(37):         
        ax[a,k-1].add_patch(Rectangle(xy=(0,0),width=0.1, height=1, color=cols[a]))
        s = f'\'{nms[a]}\': {cols[a]}'
        ax[a,k-1].text(0.15,0.5,s,fontdict={'color':'k','fontsize':8,'va':'center'})
        ax[a,k-1].set_axis_off()
    


# (sec:misturas-cor)=
# ### Misturas de cor
# 
# Alguns termos utilizados para fazer referência a misturas de cor decorrentes de _cores puras_ (cores que não podem ser obtidas a partir de outras) são empregados pelos teóricos da cor. Esses termos não possuem tradução imediata para o português, mas podem ser especificados com auxílio de prefixo "tons de". São eles:
# 
# - _Tints_ (tons de branco): são cores que, misturadas com branco, produzem variações de luminosidade;
# - _Shades_ (tons de preto): são cores que, misturadas com preto, produzem variações de escuridão;
# - _Tones_ (tons): são cores misturadas com cinza, preto ou branco.
# 
# O diagrama da {numref}`fig-tint-tone-shade` descreve a relação entre esses termos.
# 
# ```{figure} ../figs/tint-tone-shade.png
# ---
# name: fig-tint-tone-shade
# alt: Cores aditivas.
# align: center
# width: 450px
# ---
# Diagrama de termos relativos a tonalidades de cor.
# ```

# ## Outros esquemas de cor
# 
# As escalas de cor que estudamos na {numref}`Seção %s <sec:escalas-cor>` às vezes são chamadas de _esquemas de cor_. Existem diversos esquemas com aplicações e usos específicos (p.ex. triádico, tetrádico, análogo) que não exploraremos com detalhes neste capítulo.Porém, vale ressaltar ainda alguns deles, que também sugerem terminologias úteis:
# 
# - _Esquema monocromático_: composto por cores derivadas de um único matiz adicionadas de branco, cinza ou preto, isto é, seus _tints_, _tones_ e _shades_.
# - _Esquema complementar_: composto pelas cores que cancelam os matizes de outras, segundo o princípio subtrativo.
# - _Esquema acromático_: composto por cores insaturadas, acromáticas, ou aproximadamente neutras. Cores acromáticas puras incluem preto, branco, cinzas e beges. Cores aproximadamente neutras incluem marrons, tons canelados, pastéis e escurecidos. Cores neutras podem ser produzidas pela mistura de cores puras com preto, branco, cinza, ou com duas cores complementares.
# 
# Outros termos úteis neste contexto são relacionados a paletas de cores, a exemplo de _color swatch_ e _color wheel_.

# ### Esquemas de propriedade comercial
# 
# No cenário internacional, muitas empresas disputam o "mercado da cor" e das artes gráficas. Algumas delas possuem sistemas de classificação de cor próprios e patenteados. Uma parte delas é bastante conhecida no Brasil, outra nem tanto. Para efeito de expansão de conhecimento, seguem abaixo links para algumas marcas devotadas às cores:
# 
# - [Faber-Castell(c)](https://www.faber-castell.com) (veja tabela de cores [aqui](https://www.faber-castell.com/-/media/Faber-Castell-new/PDF/en/Farbtabelle-AG-ENG-0214.ashx)
# - [Pantone(c)](https://www.pantone.com/) (veja sistemas de cores [aqui](https://www.pantone.com/color-systems/pantone-color-systems-explained))
# - [Prisma Color(c)](https://www.prismacolor.com)
# - [Spectrum Noir(c)](https://www.spectrumnoir.com)
# - [Stabilo(c)](https://www.stabilo.com/)
# - [Staedtler(c)](https://www.staedtler.com/intl/en/)
# - [Tombow(c)](https://www.tombowusa.com)
# 
# Uma tabela de conversão de cores entre alguns dos sistemas acima pode ser encontrada nesta [página](https://www.colourwithclaire.com/latest/pantoner-spring-2018-colour-conversion-chart).

# ## Teoria dos espaços de cor
# 
# 
# ### Espaços de cor CIE
# 
# Modelos de cor e espaços de cor às vezes são terminologias que se confundem, embora existam propriedades intrínsecas a serem destacadas para que um espaço de cor seja realmente definido. Um _espaço de cor_, compreendido de maneira direta, é uma estrutura de organização de cores. Porém, esta resposta pode ser pouco esclarecedora, levando-nos a adentrar um pouco mais no conhecimento teórico.
# 
# O que separa um modelo de cor, como o RGB, por exemplo, de um espaço de cor, como o CIELAB, é uma espécie de _função de mapeamento de cor_ que está vinculada à percepção real do olho humano das cores. Em 1931, a [_International Commission on Illumination_](http://cie.co.at) (em francês, _Commission Internationale de l'Éclairage_ - CIE), a autoridade internacional em matéria de padrões para luz e cor, estabeleceu o _observador padrão (colorimétrico)_ como a função de mapeamento. Uma vez que os cones triestimulares S, M, L (veja a {numref}`Seção %s <sec:escalas-cor>`) dependem do campo de visão do observador, o observador padrão é uma ponderação das respostas aos estímulos da visão considerando parâmetros experimentais e a ciência da colorimetria, que forma a base para descrever uma cor como três numeros.
# 
# No princípio, o experimento do observador padrão tratou as componentes de cromaticidade formadoras da cor como $L^{*}$, $a^{*}$ e $b^{*}$, representando nesta ordem, a luminosidade, a resposta a estímulos de verde/vermelho e a resposta a estímulos de azul-amarelo. Da junção de CIE com as iniciais utilizadas decorre o nome _CIELAB_, ou espaço _CIE 1931_, que é um espaço de cor _independente de dispositivo_. Na prática, monitores, telas e dispositivos eletrônicos para visualização de imagens coloridas representam as cores de maneira diferente, razão pela qual a necessidade por um padrão emergiu.
# 
# Relacionados ao espaço _CIELAB_, estão os espaços _CIEXYZ_ e _CIERGB_. No espaço CIEXYZ, $Z$ é a componente da luminosidade, $Z$ é a componente "quase-azul" (equivalente a azul no CIERGB) e $X$ é a componente das misturas das cores RGB.
# 
# ### Espectro e componentes
# 
# A energia física (radiância) é expressa em um espectro de 31 componentes representando bandas de 10 nanômetros, o que leva à faixa do espectro visível de aproximadamente 400 - 700 nm. Isto significa que, a rigor, uma cor seria representada por 31 componentes. Uma vez que isso é irrazoável, a ponderação dessas componentes no espectro permite que reduzamos sua complexidade a apenas 3 componentes.
# 
# As 3 componentes geralmente utilizadas dependerão, por sua vez, do espectro de energia. Nos experimentos primários da CIE, as funções de mapeamento – também chamadas de _color matching functions_ (CMFs) – para o observador padrão foram definidas como superposições de curvas gaussianas dadas pela expressão
# 
# $$
# \mathcal{G}(\lambda;\mu,\sigma_1,\sigma_2) = 
# \begin{cases}
# e^{-\frac{1}{2}\left(\frac{ \lambda - \mu}{\sigma_1}\right)^2}, \ \ \text{se} \ \ \lambda \le \mu \\
# e^{-\frac{1}{2}\left(\frac{ \lambda - \mu}{\sigma_2}\right)^2}, \ \ \text{se} \ \ \lambda \geq \mu
# \end{cases},
# $$
# 
# onde $\lambda \, [nm]$ é o comprimento de onda, $\mu$ o valor médio da distribuição, $\sigma_1$ o desvio à esquerda da média e $\sigma_2$ o desvio à direita da média. 
# 
# Por sua vez, as CMFs para as respostas triestimulares XYZ para o espaço CIEXYZ, foram dadas pelas ponderações a seguir:
# 
# $$
# \bar{x}(\lambda) = 1.056\mathcal{G}(\lambda;599.8,37.9,31.0) + 0.362\mathcal{G}(\lambda;442.0,16.0,26.7) - 0.065\mathcal{G}(\lambda;501.1,20.4,26.2)
# $$
# 
# $$
# \bar{y}(\lambda) = 0.821\mathcal{G}(\lambda;568.8,46.9,40.5) + 0.286\mathcal{G}(\lambda;530.9,16.3,31.1)
# $$
# 
# $$
# \bar{z}(\lambda) = 1.217\mathcal{G}(\lambda;437.0,11.8,36.0) + 0.681\mathcal{G}(\lambda;459.0,26.0,13.8) \\
# $$
# 
# A partir daí, definindo-se o espectro de energia por uma função $p(\lambda)$, uma cor é definida pelo vetor
# 
# $$
# \vec{c} = \left( 
#     \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) \bar{x}(\lambda) \, d\lambda,
#     \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) \bar{y}(\lambda) \, d\lambda,
#     \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) \bar{z}(\lambda) \, d\lambda
#     \right),
# $$
# para o espectro compreendido entre comprimentos de onda no intervalo $[\lambda_{min},\lambda_{max}]$.
# 
# ### Relacionamento com a Álgebra Linear
# 
# Tendo em vista que a interpretação triestimular dependerá do espaço de cor considerado, haja vista os parâmetros que o definem, uma cor, genericamente, é função de um espectro de distribuição da luz, $p(\lambda)$, e da sensibilidade dos 3 cones de percepção visual. Escrevendo a função de sensibilidade do i-ésimo cone como $s_i(\lambda)$ para um espaço de cor $E$, podemos expressar as componentes de uma cor $c$ em $E$ como
# 
# $$
# c_i = \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) s_i(\lambda) \, d\lambda
# $$
# 
# Notemos, porém, que o vetor $\vec{c}$ do qual $c_i$ são suas componentes, é, na verdade, um vetor que possui integrais definidas com integrandos "contínuos". Na prática, as cores são representadas por _pixels_ e _canais de cor_ discretos, sendo necessário trabalhar com _arrays_ de dimensão até 3, o que nos remete a operações matriz-vetor.
# 
# Assim, em termos de matemática discreta, a cor, grosso modo, é representada por uma operação algébrica do tipo
# 
# $$
# \mathbf{c} = \mathbf{S}^T \mathbf{p},
# $$
# 
# com $\mathbf{c} \in \mathbb{R}^3$, $\mathbf{S} \in \mathbb{R}^{n \times 3}$ e $\mathbf{p} \in \mathbb{R}^n$.
# 
# De igual modo, a conversão entre espaços de cor dá-se por meio de operações matriciais, porque, no final das contas, cada cor é identificada como um vetor $c$ de 3 coordenadas identificado com uma posição de um subespaço vetorial tridimensional $\mathcal{E}$. Por exemplo, para converter cores do sistema RGB para XYZ, devemos resolver uma equação matricial do tipo:
# 
# $$
# \begin{bmatrix}
# X \\
# Y \\
# Z \\
# \end{bmatrix}
# = \mathbf{M}
# \begin{bmatrix}
# R \\
# G \\
# B \\
# \end{bmatrix},
# $$
# 
# onde $[X \, Y \, Z]^T$ é o vetor de coordenadas da cor no sistema XYZ, $[R \, G \, B]^T$ o vetor equivalente no sistema RGB e $\mathbf{M}$ a matriz de transformação. A conversão no sentido inverso depende da inversa de $\mathbf{M}$. Entretanto, como existem diversos espaços RGB, as matrizes $\mathbf{M}$ e $\mathbf{M}^{-1}$ também diferirão caso a caso. 
# 
# A seguir, mostramos os pares de matrizes para conversão RGB-XYZ para dois espaços RGB comuns considerando a referência de cor branca $D_{65}$ (chamada de _reference white_):
# 
# - Adobe RGB (1998)
# 
# $$
# \begin{array}{cc}
# \mathbf{M}=
# \begin{bmatrix}
# 0.5767309 & 0.1855540 & 0.1881852 \\
# 0.2973769 & 0.6273491 & 0.0752741 \\
# 0.0270343 & 0.0706872 & 0.9911085 \\
# \end{bmatrix}
# &
# \mathbf{M}^{-1}=
# \begin{bmatrix}
# 2.0413690  &-0.5649464 & -0.3446944 \\
# -0.9692660 & 1.8760108 & 0.0415560 \\
# 0.0134474  &-0.1183897 & 1.0154096
# \end{bmatrix}
# \end{array}
# $$
# 
# - Apple RGB
# 
# $$
# \begin{array}{cc}
# \mathbf{M}=
# \begin{bmatrix}
# 0.4497288 & 0.3162486 & 0.1844926 \\
# 0.2446525 & 0.6720283 & 0.0833192 \\
# 0.0251848 & 0.1411824 & 0.9224628
# \end{bmatrix}
# &
# \mathbf{M}^{-1}=
# \begin{bmatrix}
# 2.9515373  & -1.2894116 & -0.4738445 \\
# -1.0851093 & 1.9908566  & 0.0372026 \\
# 0.0854934  & -0.2694964 & 1.0912975
# \end{bmatrix}
# \end{array}
# $$

# ## Referências
# 
# ```{bibliography}
# :filter: docname in docnames
# ```

# ## Referências complementares
# 
# - [Color space](https://en.wikipedia.org/wiki/Color_space)
# - [CIE Color Space, Gernot Hoffmann](http://docs-hoffmann.de/ciexyz29082000.pdf)
# - [A Guided Tour of Color Space, Charles Poynton](https://poynton.ca/PDFs/Guided_tour.pdf)
# - [Mathematics and Colour, Nick Higham](https://www.maths.manchester.ac.uk/~higham/talks/digphot_long.pdf)
# - [Colour spaces - perceptual, historical and applicational background, Tkalcic M. e Tasic, J.](https://web.archive.org/web/20090306063001/http://ldos.fe.uni-lj.si/docs/documents/20030929092037_markot.pdf)
# - [Color Spaces, Rolf Kuehni](https://web.archive.org/web/20090306062959/http://www4.ncsu.edu/~rgkuehni/PDFs/ColSp.pdf)
# - [Bruce Lindbloom.com](http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html)
# - [coloria](https://github.com/coloria-dev/coloria)
