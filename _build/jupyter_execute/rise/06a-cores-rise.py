#!/usr/bin/env python
# coding: utf-8

# # Cores
# 
# Prof. Gustavo Oliveira
# 
# CI/DCC/UFPB
# 
# [gcpeixoto.github.com/DATAVIZ](https://gcpeixoto.github.com/DATAVIZ)

# ## Introdução
# 
# - Cores são constituintes fundamentais da aparência das RVs
# - Utilidade: 
#     - enaltecer estímulo e percepção visuais da audiência
#     - distinguir grupos de dados;
#     - representar valores; e
#     - produzir destaques (_highlights_)

# ## Escalas de cor
# 
# - Objetivo específico: distinguir grupos através da plotagem de dados qualitativos categóricos. 
# - Para esta finalidade: 
#     - usar paletas de cores discretas (_escalas de cor qualitativas_)
#     - dar percepção de "grupos finitos" de informação

# ### `seaborn.color_palette()`
# 
# - Várias escalas de cores qualitativas ou _mapas de cores_ (ex. 6, 10 e 14 cores segundo a paleta padrão)

# In[1]:


from seaborn import color_palette
color_palette(n_colors=6)


# In[2]:


color_palette(n_colors=10)


# In[3]:


color_palette(n_colors=14)


# ### Insaturação proporcional com `desat`

# In[4]:


color_palette(n_colors=6,desat=0.1)


# In[5]:


color_palette(n_colors=10,desat=0.5)


# In[14]:


color_palette(n_colors=14,desat=.0)


# ### Paletas predefinidas
# 
# - O `seaborn` possui algumas paletas de cores predefinidas que alteram as tonalidades das cores:
#     - `muted`
#     - `bright`
#     - `pastel`
#     - `dark`
#     - `colorblind`

# In[15]:


color_palette('muted')


# In[16]:


color_palette('bright')


# In[17]:


color_palette('pastel')


# In[18]:


color_palette('dark')


# In[19]:


color_palette('colorblind')


# ### Paletas qualitativas
# 
# - O `matplotlib` também possui uma série de paletas de cores. As qualitativas são:
#     - `Pastel1`, `Pastel2`;
#     - `Paired`, `Accent`;
#     - `Dark2`;
#     - `Set1`, `Set2`, `Set3`; 
#     - `tab10`, `tab20`, `tab20b`, `tab20c`.
# 
# 

# Cada uma pode ser invocada pela função `seaborn.color_palette()` naturalmente:

# In[20]:


color_palette('Paired',n_colors=10)


# In[21]:


color_palette('Set1',n_colors=10)


# In[22]:


color_palette('tab20b',n_colors=10)


# ### Exemplo aplicado: dado qualitativo categórico
# 
# - Plotar a malha geográfica de municípios da PB usando uma das escalas de cor disponíveis no `matplotlib`.
#     - Definir função `plot_municipios_PB(escala)`
#     - Trabalhar com sistemas de coordenadas existentes no módulo `cartopy`
#     - Gerar paleta de 223 cores (uma para cada município) com base na escala escolhida pelo usuário 
#     - Fazer a RV dos dados categorizados.

# In[15]:


import matplotlib.pyplot as plt, cartopy.crs as ccrs, cartopy.io.shapereader as shpreader
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
    shapename = '../data/PB_Municipios_2021/PB_Municipios_2021'
    shp = shpreader.Reader(shapename)
    nmun = len(shp) # no. municípios

    # plotagem dos polígonos dos municípios
    plt.title('Municípios da Paraíba',fontsize=10)
    cols = color_palette(plte,n_colors=nmun) # paleta de 223 cores

    for i,s in enumerate(shp.geometries()):    
        ax.add_geometries([s], ccrs.PlateCarree(),facecolor=cols[i], edgecolor='white');

    return shp


# In[16]:


# Plotagem com escala de cores escolhida pelo usuário
plot_municipios_PB('Paired');


# ### Paletas contínuas e demais paletas predefinidas
# 
# - O `matplotlib` dispõe de outras dezenas de paletas com características diversas
# - Em particular, _paletas contínuas_ são aquelas que geram uma percepção de continuidade
# - PCs são úteis para a plotagem de dados quantitativos numéricos e dados onde prevaleça algum ordenamento

# ### Classes de paletas do `matplotlib`
# 
# 1. Sequenciais com percepção de uniformidade: `viridis`, `plasma`, `inferno`, `magma` e `cividis`
# 2. Sequenciais do grupo 1: `Greys`, `Purples`, `Blues`, `Greens`, `Oranges`, `Reds`, `YlOrBr`, `YlOrRd`, `OrRd`, `PuRd`, `RdPu`, `BuPu`, `GnBu`, `PuBu`, `YlGnBu`, `PuBuGn`, `BuGn` e `YlGn`;
# 3. Sequenciais do grupo 2: `binary`, `gist_yarg`, `gist_gray`, `gray`, `bone`, `pink`, `spring`, `summer`, `autumn`, `winter`, `cool`, `Wistia`, `hot`, `afmhot`, `gist_heat` e `copper`;

# 4. Divergentes: `PiYG`, `PRGn`, `BrBG`, `PuOr`, `RdGy`, `RdBu`, `RdYlBu`, `RdYlGn`, `Spectral`, `coolwarm`, `bwr` e `seismic`;
# 5. Cíclicas: `twilight`, `twilight_shifted`, `hsv`;
# 
# 6. Qualitativas: já vistas anteriormente.
# 7. Genéricas: `flag`, `prism`, `ocean`, `gist_earth`, `terrain`, `gist_stern`, `gnuplot`, `gnuplot2`, `CMRmap`, `cubehelix`, `brg`, `gist_rainbow`, `rainbow`, `jet`, `turbo`, `nipy_spectral` e `gist_ncar`.

# ### Fatores de escolha da paleta
# 
# - natureza dos dados (p.ex. qualitativo, quantitativo, discreto, contínuo);
# - destaque (p.ex. destacar valor médio e outliers);
# - intuição (p.ex. tons de verde para tratar parâmetros métricos de sustentabilidade);
# - necessidades especiais (p.ex. público com particularidades visuais); e
# - tradição do campo do conhecimento (p.ex. cores binárias em imagens médicas).

# ### Escalas de cor do `matplotlib`
# 
# 1. Sequenciais: mudanças incrementais na luminosidade e na saturação de cor, muitas vezes usando um único matiz; deve ser usado para representar dados que possuam alguma ordenação.

# 2. Divergentes: mudança na luminosidade e possivelmente na saturação de duas cores diferentes que se encontram no meio a uma cor insaturada; deve ser usada quando a informação que está sendo plotada tem um valor médio crítico ou quando os dados se desviam em relação a zero.

# 3. Cíclicas: mudança na luminosidade de duas cores diferentes que se encontram no meio e início/fim em uma cor insaturada; deve ser usado para valores relativos a fenômenos cíclicos/periódicos, tais como ângulo de fase, direção do vento ou hora do dia.

# 4. Qualitativas: cores diversas; deve ser usada para representar informações que não possuem ordem ou relacionamentos.

# ### Sequenciais com percepção de uniformidade

# In[23]:


color_palette('viridis',n_colors=12)


# In[24]:


color_palette('magma',n_colors=12)


# ### Sequenciais do grupo 1

# In[25]:


color_palette('Oranges',n_colors=35)


# In[26]:


color_palette('Blues',n_colors=35)


# In[27]:


color_palette('YlOrRd',n_colors=35)


# ### Sequenciais do grupo 2

# In[28]:


color_palette('bone',n_colors=12)


# In[29]:


color_palette('hot',n_colors=12)


# In[30]:


color_palette('copper',n_colors=12)


# ### Divergentes

# In[36]:


color_palette('RdBu',n_colors=17) 


# In[37]:


color_palette('Spectral',n_colors=15)


# In[39]:


color_palette('seismic',n_colors=15)


# ### Cíclicas

# In[40]:


color_palette('twilight',n_colors=25)


# In[41]:


color_palette('twilight_shifted',n_colors=12)


# In[42]:


color_palette('hsv',n_colors=25)


# ### Genéricas

# In[43]:


color_palette('prism',n_colors=12)


# In[44]:


color_palette('terrain',n_colors=12)


# In[45]:


color_palette('rainbow',n_colors=12)


# ### Exemplo aplicado: dado quantitativo numérico
# 
# - Recuperar os valores das áreas (em km2) de todos os municípios da PB
# - Construir gráfico de dispersão ordenado
# - Fazer RV da variação do escore padronizado (Fator Z, ou _Z-score_) das áreas dos municípios
#     - Fator Z = 0 => média do conjunto
#     - Fator Z < 0 => municípios com área abaixo da média do estado
#     - Fator Z > 0 => municípios com área acima da média do estado
# - Escolher escala de cor divergente que muda a tonalidade consoante variação do Fator Z
# - Detectar rapidamente municípios de menor e maior extensão territorial

# In[34]:


from matplotlib.pyplot import subplots
from seaborn import set_palette, lineplot
from scipy.stats import zscore
from pandas import DataFrame
import cartopy.io.shapereader as shpreader

# recupera dados do shapefile
shp = shpreader.Reader('../data/PB_Municipios_2021/PB_Municipios_2021')
nmun = len(shp)
CD, NM, AREA = [], [], [] 

for rec in shp.records():
    CD.append(rec.attributes['CD_MUN'])
    NM.append(rec.attributes['NM_MUN'])
    AREA.append(rec.attributes['AREA_KM2'])


# **NOTA:** se loop anterior não funcionar, checar versão do cartopy e tentar
# 
# ```python
# for mun in range(nmun):
#     CD.append(shp._data[mun]['CD_MUN'])
#     NM.append(shp._data[mun]['NM_MUN'])
#     AREA.append(shp._data[mun]['AREA_KM2'])
# ```

# In[56]:


# converte dados de área para float e cálcula escore padronizado
df = DataFrame({'CD':CD,'NM':NM,'AREA':AREA})
df['AREA'] = df['AREA'].apply(lambda x: float(str(x).replace('.','')))
df['Z'] = zscore(df['AREA']); df = df.sort_values(by='Z')

# paleta de cores
set_palette("PiYG")


# In[37]:


# figura
fig, ax = subplots(1,1,figsize=(1,30),constrained_layout=False)
f = lineplot(data=df,y='NM',x='Z',marker='o',markersize=7,hue="Z",linewidth=0,ax=ax)

# linha média 
ax.axvline(x=0,color='#CE408E',lw=1.2,alpha=0.8)

# decoração
ax.axis('equal'); ax.grid(axis='both'); ax.tick_params(axis='both', labelsize=6)
ax.set_xlim(-3.5,3.5); ax.set_ylim(nmun+0.1,-0.5)
ax.spines['bottom'].set_visible(False); ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False); ax.spines['right'].set_visible(False); ax.get_legend().remove()
ax.set_title('Escore padronizado: área [km2]',fontsize=8)
ax.set_xlabel('Z-score',fontsize=8); ax.set_ylabel('Município - PB',fontsize=8);


# > De fato, uma rápida investigação no _dataframe_ permite-nos afirmar que Araçagi disputa com Solânea a extensão média, visto que a inflexão do Fator Z ocorre entre as duas localidades.

# In[38]:


df['NM'][df['Z'].idxmin()], df['AREA'][df['Z'].idxmin()]


# In[39]:


df['NM'][df['Z'].idxmax()], df['AREA'][df['Z'].idxmax()]


# In[40]:


df[(df['Z'] > -0.005) & (df['Z'] < 0.005)]


# ## Modelos de cor
# 
# - Cores podem ser representadas de forma abstrata através de um modelo matemático baseado em ênuplas geralmente de 3 ou 4 coordenadas. 
#     - Em geral, uma cor é uma estrutura $c = (c_1,c_2,c_3)$, ou $c = (c_1,c_2,c_3,c_4)$. 
#     - Quando cada uma das componentes $c_i$ são associadas a aspectos da percepção visual, elas podem ter diferentes interpretações e dar origens a um _espaço de cores_. 

# ### Óptica, ondas e cores
# 
# - _Cor_: nome que damos à qualidade perceptiva da luz
# - Resposta subjetiva do cérebro ao estímulo retinal 
# - Percepção das cores baseia-se em sensibilidade a ondas eletromagnéticas
# - Espectro de energia visível – gráfico de intensidade vs. comprimento de onda (ou frequência) – é caracterizado por comprimentos de onda na faixa de 400 - 700 nm. 
# - "Luz visível": cobre matizes do violeta ao vermelho. 
#     - Abaixo do espectro visível: "luz ultravioleta" (UV) e acima, a "luz infravermelha" (IR).

# ### "Cones visuais"
# 
# - Células receptoras localizadas na retina. 
# - Há 3 "cones" (células fotoreceptoras) que respondem a estímulos em três regiões do espectro visível:
# 
# - Cone _S_ (_short_), que é sensível a ondas curtas com pico em torno de 440 nm (azul).
# - Cone _M_ (_medium_), que é sensível a ondas médias com pico em torno de 540 nm (verde).
# - Cone _L_ (_long_), que é sensível a ondas longas com pico em torno de 580 nm (vermelho).

# ### Espaço de cores triestimular
# 
# - Cones _M_ e _L_ respondem a praticamente todos os comprimentos de onda do espectro visível, 
# - Cone _S_ é limitado a comprimentos de até 550 nm. 
# - Tripleta de estímulos no espaço Euclidiano 3D - $(S,M,L)$ - define o _espaço de cores triestimular_ (_tristimulus color space_)
# - O ECT determina o espaço de cores do olho humano, conceito intimamente ligado a "_espaço vetorial_"

# ### Espectro, cones e monocromatismo 
# 
# - Algumas cores _monocromáticas_ (únicas) foram historicamente definidas
# - Os comprimentos de onda de fronteira que as definem podem variar. 
# - De acordo com o _CRC Handbook of Physics (1966)_, há 6 bandas de ondas do espectro:
#     - Vermelho: 647 - 700;
#     - Laranja: 585 - 647;
#     - Amarelo: 575 - 585;
#     - Verde: 491 - 575;
#     - Azul: 424 - 491; e
#     - Violeta: 400 - 424.

# In[41]:


import aux06a


# ### Processos físicos da óptica
# 
# - A cor da luz que emana de objetos origina-se por processos físicos:
#     - _emissão_, quando o objeto é uma fonte de luz com cor determinada pelo seu espectro;
#     - _reflexão_, quando algumas frequencias são refletidas pelo objeto;
#     - _transmissão_, quando algumas frequencias são transmitidas através do objeto;
#     - _interferência_, quando algumas frequencias são amplificadas e outras atenuadas;

# ### Modelos aditivos e subtrativos
# 
# #### RGB
# 
# - Assume que uma cor é identificada por $c = (r,g,b)$
# - Quando $0 \leq r,g,b \leq 1$, cada cor é um vetor com origem em $(0,0,0)$ e extremidade imersas no "cubo unitário" formado pelos eixos $r$, $g$ e $b$
# - Geometricamente, a cor preta seria representada por $\vec{o} = (r=0,g=0,b=0)$
#     - Combinação linear: $\vec{c} = r(1,0,0) + g(0,1,0) + b(0,0,1)$
# - Nos sistemas digitais modernos, $r$, $g$ e $b$ limitam-se ao intervalo de 0 a 255

# ##### Cubo RGB
# 
# - Máx.: 256 x 256 x 256 = 16.777.216 cores (~ 16 milhões de cores). 
# 
# <img src="../figs/rgb-cube.jpg" width="600" height="600">

# #### Aditividade
# 
# - RGB é um _modelo aditivo_ (cor percebida representada por soma de valores numéricos de suas componentes)
# - Vermelho, verde e azul são _cores primárias_
# - Cor preta equivale a um "elemento neutro":
#     - preto + vermelho = vermelho
#     - preto + verde = verde
#     - preto + azul = azul.

# Entretanto,
# 
# - vermelho + verde = amarelo
# - verde + azul = ciano
# - azul + vermelho = magenta
# - vermelho + verde + azul = branco

# #### Modelo fundamental de mistura aditiva de cores RGB
# 
# <img src="../figs/cores-aditivas.png" width="600" height="600">

# #### CMYK
# 
# - Cor identificada por $c = (c,m,y,k)$
# - $c$, $m$, $y$, e $k$ são proporções de ciano, magenta, amarelo e preto
# - c, m, y são _cores subtrativas primárias_ e k uma quarta componente que gera tonalidades escuras
# - Por isso, o modelo também é conhecido como _CMY_

# #### Subtratividade 
# 
# - Cores subtrativas agem em complementaridade às aditivas primárias e servem como filtros que as absorvem. 
# - c,m,y são complementares de r,g,b, nesta ordem. 
# - CMYK preferível para impressão (espectro de cores significativamente menor e composto por pigmentos)
# - RGB preferível para telas e dispositivos eletrônicos (composto por luz)

# ##### Pigmentos x luz
# 
# - A ausência de pigmentos é o papel branco. Isto significa que o papel permanece "branco" quando iluminado pela luz branca. 
# - Adicionar pigmentos a ele é como subtrair certos comprimentos de onda. Então, algebricamente:
# 
# - branco - vermelho = ciano
# - branco - verde = magenta
# - branco - azul = amarelo.

# Entretanto, 
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

# #### Modelo fundamental de mistura subtrativa de cores CMY/K
# 
# <img src="../figs/cores-subtrativas.png" width="600" height="600">

# ### Modelos geométricos
# 
# - Outros diversos modelos de cor tridimensionais em formatos cônicos, cilíndricos ou esféricos foram desenvolvidos ao longo do tempo:
#     - HSL, HSV, HSI, HCL, HSB, NCS, XYZ, entre outros. 
# - HSL (_Hue_, _Saturation_, _Luminosity_) é considerado um dos mais acessíveis para aplicação em visualização de dados
# - Representação cilíndrica do modelo RGB

# #### RVs dos modelos HSL e HSV em formas geométricas diferentes
# 
# <img src="../figs/color-solid-comparison.png" width="600" height="600">

# ### HSL
# 
# - O modelo HSL é 3D com componentes:
# - _Hue_ (matiz): varia na direção azimutal do cilindro e define a cor "verdadeira". 
# 
# > O matiz é tecnicamente definido como _"o grau com que um estímulo pode ser descrito como semelhante ou diferente de estímulos descritos como vermelho, laranja, amarelo, verde, azul ou violeta"_ (Modelo CIECAM02 de colorimetria)
# 
# - No sistema cilíndrico: a cor vermelha primária (matiz puro) está em 0 grau, verde primária em 120 e azul em 240. 
# - Matiz é atributo qualitativo da cor porque é definido por diferença e não por escala (sem _tints_, _shades_ ou _tones_)

# - _Saturation_ (saturação), que varia na direção radial do cilindro e define a pureza do matiz. 
# - A cor plenamente saturada é _vívida_ (_vivid_). 
# - À medida que a insaturamos até o estado de tons de cinza, ou _acromaticidade_, ou _neutralidade_ (eixo central do cilindro), a cor torna-se _muda_ (_muted_). 
# - Um matiz com 0% de saturação neutro (mudo), ao passo que um matiz com 100% de saturação é puro (vívido). 
# - A saturação é um parâmetro quantitativo da cor.

# - _Luminosity_ (luminosidade), que define a direção axial do cilindro e define o contraste do matiz. 
# - Tecnicamente, não é sinônimo de brilho, mas pode ser entendida como um controlador entre tons claros e escuros.
# - A luminosidade também é um parâmetro quantitativo da cor.

# #### `seaborn.palplot()` e `seaborn.hls_palette` 
# 
# - Demonstrando variações dos valores das componentes $h$, $s$, e $l$ no modelo de HSL, no qual a cor é uma tripleta em coordenadas cilíndricas dada por $c=(h,s,l)$

# #### Variação de matizes com 100% de saturação e luminosidade média

# In[42]:


from seaborn import palplot, hls_palette
# cores puras do arco-íris
palplot(hls_palette(n_colors=5, h=0, s=1, l=0.5)) 


# In[43]:


# matiz 33%
palplot(hls_palette(n_colors=5, h=0.5, s=1, l=0.5)) 


# In[44]:


# matiz 66%
palplot(hls_palette(n_colors=5, h=0.1, s=1, l=0.5)) 


# #### Matiz 100% com variação de saturação e luminosidade média

# In[45]:


# saturação 80%
palplot(hls_palette(n_colors=5, h=1, s=.75, l=0.5)) 


# In[46]:


# saturação 50%
palplot(hls_palette(n_colors=5, h=1, s=.5, l=0.5)) 


# In[47]:


# saturação 10%
palplot(hls_palette(n_colors=5, h=1, s=.1, l=0.5)) 


# #### Matiz e saturação 100% e luminosidade variável

# In[48]:


# luminosidade 90%
palplot(hls_palette(n_colors=5, h=1, s=1, l=.9)) 


# In[49]:


# luminosidade 40%
palplot(hls_palette(n_colors=5, h=1, s=1, l=.4)) 


# In[50]:


# luminosidade 10%
palplot(hls_palette(n_colors=5, h=1, s=1, l=.1)) 


# ### Código HEX
# 
# - Representação de cores por código hexadecimal (_hex codes_) emergiu como um sistema prático para trabalhar com desenvolvimento _web_. 
# - Passou a ser utilizado para diversos fins em dataviz devido à sua simplicidade de uso e facilidade de compreensão.
# - Tripleta HEX: 6 dígitos (3 bytes) hexadecimais do tipo `AABB00` 
# - Famosa em HTML e CSS para estilizar páginas da internet e também em artes gráficas. 
# - Em geral, usa-se uma tralha (`#`) antes do código por razões sintáticas.

# #### Decifrando o HEX code
# 
# - Representação implícita do modelo RGB. 
# - Dígitos 1 e 2 (byte 1) controlam a proporção de vermelho
# - Dígitos 3 e 4 (byte 2) controlam a proporção de verde
# - Dígitos 5 e 6 (byte 3) controlam a proporção de azul
# - Sistema admite dígitos de 0 a 9 e as letras de A a F
#     - 16 possibilidades por dígito de _hex code_, ou seja, até $16^6 = 16.777.216$ cores representáveis.

# #### Conversão RGB > HEX
# 
# Para a cor RGB(1,0.5,0.3): 
# 
# - multiplicamos por 255 para ter RGB(255,127,76). _Obs.: se a tupla já for inteira, este passo é ignorado._
# - realizamos a divisão inteira por componente para obter a tupla de quocientes (15,7,4);
# - tomamos o resto da divisão inteira por componente para obter a tupla de restos (15,15,12);
# - convertemos os dígitos maiores do que 9 para letras nas tuplas para obter (F,7,4) e (F,F,C);
# - juntamos as tuplas elemento a elemento para formar os bytes chegando ao _hex code_ FF7F4C

# #### Teste RGB / HEX

# In[51]:


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


# In[59]:


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


# In[53]:


# teste 1
rgb = (1,0.5,0.3)
rgb2hex(rgb)


# In[54]:


# teste 2
rgb = (255,127,76)
rgb2hex(rgb)


# ### Exemplos de cores CSS

# In[62]:


from matplotlib.colors import CSS4_COLORS; from matplotlib.pyplot import subplots; from matplotlib.patches import Rectangle
fig, ax = subplots(37,4,figsize=(10,8),constrained_layout=True)
fig.suptitle('Cores CSS predefinidas do matplotlib e seus hex codes',fontsize=8)
# cores CSS
css = CSS4_COLORS; ck,cv = list(css.keys()),list(css.values())
# mosaico de cores: len(css)/4 = 37 x 4
for k in range(1,5):
    nms = ck[(k-1)*37:k*37]; cols = cv[(k-1)*37:k*37]
    for a in range(37):         
        ax[a,k-1].add_patch(Rectangle(xy=(0,0),width=0.1, height=1, color=cols[a]))
        s = f'\'{nms[a]}\': {cols[a]}'
        ax[a,k-1].text(0.15,0.5,s,fontdict={'color':'k','fontsize':8,'va':'center'}); ax[a,k-1].set_axis_off()


# ### Misturas de cor
# 
# - Alguns termos utilizados para fazer referência a misturas de cor decorrentes de _cores puras_ (cores que não podem ser obtidas a partir de outras) são empregados pelos teóricos da cor. 
# - Não possuem tradução imediata para o português, mas podem ser especificados com auxílio de prefixo "tons de". São eles:
#     - _Tints_ (tons de branco): são cores que, misturadas com branco, produzem variações de luminosidade;
#     - _Shades_ (tons de preto): são cores que, misturadas com preto, produzem variações de escuridão;
#     - _Tones_ (tons): são cores misturadas com cinza, preto ou branco.

# ### Relação de tonalidades de cor
# 
# <img src="../figs/tint-tone-shade.png" width="600" height="600">

# ## Outros esquemas de cor
# 
# - As escalas de cor às vezes são chamadas de _esquemas de cor_. 
# - Existem diversos esquemas com aplicações e usos específicos (p.ex. triádico, tetrádico, análogo) 
# - Alguns deles sugerem terminologias úteis:

# ### _Esquema monocromático_
# 
# - Composto por cores derivadas de um único matiz adicionadas de branco, cinza ou preto, isto é, seus _tints_, _tones_ e _shades_.

# ## Outros esquemas de cor
# 
# - As escalas de cor às vezes são chamadas de _esquemas de cor_. 
# - Existem diversos esquemas com aplicações e usos específicos (p.ex. triádico, tetrádico, análogo) 
# - Alguns deles sugerem terminologias úteis:
#     - _Esquema monocromático_: composto por cores derivadas de um único matiz adicionadas de branco, cinza ou preto, isto é, seus _tints_, _tones_ e _shades_.
#     - _Esquema complementar_: composto pelas cores que cancelam os matizes de outras, segundo o princípio subtrativo.

# - _Esquema acromático_: composto por cores insaturadas, acromáticas, ou aproximadamente neutras. Cores acromáticas puras incluem preto, branco, cinzas e beges. Cores aproximadamente neutras incluem marrons, tons canelados, pastéis e escurecidos. Cores neutras podem ser produzidas pela mistura de cores puras com preto, branco, cinza, ou com duas cores complementares.

# ### Esquemas de propriedade comercial
# 
# - No cenário internacional, muitas empresas disputam o "mercado da cor" e das artes gráficas. 
# - Algumas delas possuem sistemas de classificação de cor próprios e patenteados. 
# - Uma parte delas é bastante conhecida no Brasil, outra nem tanto. 

# - Links para marcas devotadas às cores:
#     - [Faber-Castell(c)](https://www.faber-castell.com) (veja tabela de cores [aqui](https://www.faber-castell.com/-/media/Faber-Castell-new/PDF/en/Farbtabelle-AG-ENG-0214.ashx)
#     - [Pantone(c)](https://www.pantone.com/) (veja sistemas de cores [aqui](https://www.pantone.com/color-systems/pantone-color-systems-explained))
#     - [Prisma Color(c)](https://www.prismacolor.com)
#     - [Spectrum Noir(c)](https://www.spectrumnoir.com)
#     - [Stabilo(c)](https://www.stabilo.com/)
#     - [Staedtler(c)](https://www.staedtler.com/intl/en/)
#     - [Tombow(c)](https://www.tombowusa.com)
# 
# [Tabela de conversão de cores](https://www.colourwithclaire.com/latest/pantoner-spring-2018-colour-conversion-chart).

# ## Teoria dos espaços de cor
# 
# > Um _espaço de cor_, compreendido de maneira direta, é uma estrutura de organização de cores. 
# - O que separa um modelo de cor, como o RGB, por exemplo, de um espaço de cor, como o CIELAB, é uma espécie de _função de mapeamento de cor_ que está vinculada à percepção real do olho humano das cores. 
# - Em 1931, a [_International Commission on Illumination_](http://cie.co.at) (em francês, _Commission Internationale de l'Éclairage_ - CIE), a autoridade internacional em matéria de padrões para luz e cor, estabeleceu o _observador padrão (colorimétrico)_ como a função de mapeamento.

# ### Espectro e componentes
# 
# - Energia física (radiância) é expressa em um espectro de 31 componentes representando bandas de 10 nanômetros
# - Faixa do espectro visível de aproximadamente 400 - 700 nm. 
# - A rigor, uma cor seria representada por 31 componentes. 
# - Uma vez que isso é irrazoável, a ponderação dessas componentes no espectro permite que reduzamos sua complexidade a apenas 3 componentes.

# ### CMFs 
# 
# - As 3 componentes geralmente utilizadas dependerão, por sua vez, do espectro de energia. 
# - Experimentos primários da CIE: _color matching functions_ (CMFs) para o observador padrão foram definidas como superposições de curvas gaussianas dadas pela expressão
# 
# $$
# \mathcal{G}(\lambda;\mu,\sigma_1,\sigma_2) = 
# \begin{cases}
# e^{-\frac{1}{2}\left(\frac{ \lambda - \mu}{\sigma_1}\right)^2}, \ \ \text{se} \ \ \lambda \le \mu \\
# e^{-\frac{1}{2}\left(\frac{ \lambda - \mu}{\sigma_2}\right)^2}, \ \ \text{se} \ \ \lambda \geq \mu
# \end{cases},
# $$
# 
# com $\lambda \, [nm]$ é o comprimento de onda, $\mu$ o valor médio da distribuição, $\sigma_1$ o desvio à esquerda da média e $\sigma_2$ o desvio à direita da média. 

# ### CMFs para CIEXYZ
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

# - A partir daí, definindo-se o espectro de energia por uma função $p(\lambda)$, uma cor é definida pelo vetor
# 
# $$
# \vec{c} = \left( 
#     \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) \bar{x}(\lambda) \, d\lambda,
#     \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) \bar{y}(\lambda) \, d\lambda,
#     \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) \bar{z}(\lambda) \, d\lambda
#     \right),
# $$
# para o espectro compreendido entre comprimentos de onda no intervalo $[\lambda_{min},\lambda_{max}]$.

# ### Relacionamento com a Álgebra Linear
# 
# - Parâmetros que definem a cor:
#     - espectro de distribuição da luz, $p(\lambda)$
#     - sensibilidade dos 3 cones de percepção visual. 
#     
# - Escrevendo a função de sensibilidade do i-ésimo cone como $s_i(\lambda)$ para um espaço de cor $E$, podemos expressar as componentes de uma cor $c$ em $E$ como
# 
# $$
# c_i = \int_{\lambda_{min}}^{\lambda_{max}} p(\lambda) s_i(\lambda) \, d\lambda
# $$

# - Em termos de matemática discreta, a cor, grosso modo, é representada por uma operação algébrica do tipo
# 
# $$
# \mathbf{c} = \mathbf{S}^T \mathbf{p},
# $$
# 
# com $\mathbf{c} \in \mathbb{R}^3$, $\mathbf{S} \in \mathbb{R}^{n \times 3}$ e $\mathbf{p} \in \mathbb{R}^n$.

# ### Conversão de espaços de cor
# 
# - A conversão entre espaços de cor dá-se por meio de operações matriciais,
# - Por exemplo, para converter cores do sistema RGB para XYZ, devemos resolver uma equação matricial do tipo:
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
# onde $[X \, Y \, Z]^T$ é o vetor de coordenadas da cor no sistema XYZ, $[R \, G \, B]^T$ o vetor equivalente no sistema RGB e $\mathbf{M}$ a matriz de transformação. 
# 
# - A conversão no sentido inverso depende da inversa de $\mathbf{M}$. 

# ### Exemplos de matrizes de conversão
# 
# - Pares de matrizes para conversão RGB-XYZ para dois espaços RGB comuns considerando a referência de cor branca $D_{65}$ (chamada de _reference white_):
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

# ## Referências complementares
# 
# - [Color space](https://en.wikipedia.org/wiki/Color_space)
# - [CIE Color Space, Gernot Hoffmann](http://docs-hoffmann.de/ciexyz29082000.pdf)
# - [A Guided Tour of Color Space, Charles Poynton](https://poynton.ca/PDFs/Guided_tour.pdf)
# - [Mathematics and Colour, Nick Higham](https://www.maths.manchester.ac.uk/~higham/talks/digphot_long.pdf)
# - [Colour spaces - perceptual, historical and applicational background, Tkalcic M. e Tasic, J.](https://web.archive.org/web/20090306063001/http://ldos.fe.uni-lj.si/docs/documents/20030929092037_markot.pdf)
# - [Color Spaces, Rolf Kuehni](https://web.archive.org/web/20090306062959/http://www4.ncsu.edu/~rgkuehni/PDFs/ColSp.pdf)
# - [Bruce Lindbloom.com](http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html)
