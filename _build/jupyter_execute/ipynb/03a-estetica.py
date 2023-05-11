#!/usr/bin/env python
# coding: utf-8

# (cap:estetica)=
# # Criação de Representações Visuais e Estética

# Neste capítulo, consideraremos o modelo básico para representação visual, rudimentos das representações visuais em uma, duas e três dimensões, tipos de dados e estética.

# ## Modelo referencial
# 
# A geração de representações visuais através do computador segue um modelo referencial geralmente descrito pelas seguintes componentes:
# 
# - _Entrada_: dado bruto à disposição do _storyteller_ que será manipulado para produzir um visual.
# - _Pré-Processamento_: etapa secundária de preparação e tratamento dos dados.
# - _Mapeamento_: etapa terciária onde são definidos o projeto gráfico, as estruturas visuais e o mapeamento de valores em formas quantificadas que determinarão a _estética_.
# - _Visualização_: etapa finalística que entrega o produto final, isto é, a própria representação visual.
# 
# A figura abaixo – criada através de objetos `patch` do `matplotlib` – ilustra o fluxograma do modelo referencial. Como podemos ver pelo código acompanhante, a representação visual é totalmente gerada via Python e não passou por nenhum outro software de desenho. Este exemplo é uma constatação de quão poderoso o `matplotlib` é. Porém, criar figuras de maneira elementar exige tempo e dedicação. Nem sempre será necessário seguir este caminho para criarmos bons gráficos, mas aplicar-se a conhecer a ferramenta em profundidade enaltece a capacidade técnica de engenharia visual.
# 
# Detalharemos as etapas importantes nas subseções a seguir.

# In[121]:


import matplotlib.colors as clr
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.path import Path


def draw_my_arrow(A1:tuple, B1:tuple, C1:tuple, D:tuple, C2:tuple, B2:tuple, A2:tuple):
      """
      Desenha uma seta com 7 vértices com largura e comprimento controláveis.

                C1
                o .
      A1      B1|   .
      o - - - - o     .
      |                 o D
      o - - - - o     .
      A2      B2|   .    
                o .   
                C2

      Larg. corpo: m(A1A2)
      Compr. corpo: m(A1B1)
      Larg. cabeça: m(B1C1)
      Compr. cabeça: m(B1D)
      """

      # pontos
      points = [A1, B1, C1, D, C2, B2, A2] 
      
      # caminho
      moves = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]

      return Path(points, moves)

# mapa de cores XKCD
xkcd = clr.XKCD_COLORS

# parâmetros
x0,y0 = 0,0  # origem
xa,ya = 1, 1 # 100% da área da figura
L,H = 8, 1   # tamanho da figura (polegadas)

# propriedades de my_arrow
xmid, ymid = 0.15, 0.5
body_width, body_length = 0.25, 0.02
head_width, head_length = 0.1, 0.03

# figura e eixo
fig = plt.figure(figsize=(L,H)) 
ax = fig.add_axes(rect=[x0, y0, xa, ya], frameon=False)
ax.set_axis_off()

'''CRIAÇÃO DE ELEMENTOS VISUAIS'''

# DADO BRUTO
ax.text(0.01,0.45, 
        s='Dado bruto', 
        size=12,
        style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})


# SETA 1
arrow = draw_my_arrow(A1=(xmid,ymid + body_width/2),
              B1=(xmid + body_length, ymid + body_width/2),
              C1=(xmid + body_length, ymid + body_width/2 + head_width),
              D=(xmid + body_length + head_length, ymid),
              C2=(xmid + body_length, ymid - body_width/2 - head_width),
              B2=(xmid + body_length, ymid - body_width/2),
              A2=(xmid,ymid - body_width/2)
              )

arrow = pch.PathPatch(arrow,facecolor=xkcd['xkcd:almost black'],lw=0,alpha=0.3)
ax.add_patch(arrow)


# PRÉ-PROCESSAMENTO
ax.text(0.22,0.45, 
        s='Pré-processamento', 
        style='italic',
        size=12,
        bbox={'facecolor': xkcd['xkcd:algae green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5, 
              'boxstyle': 'round',
              'pad': 0.5})


# SETA 2
xmid += 0.29
arrow = draw_my_arrow(A1=(xmid,ymid + body_width/2),
              B1=(xmid + body_length, ymid + body_width/2),
              C1=(xmid + body_length, ymid + body_width/2 + head_width),
              D=(xmid + body_length + head_length, ymid),
              C2=(xmid + body_length, ymid - body_width/2 - head_width),
              B2=(xmid + body_length, ymid - body_width/2),
              A2=(xmid,ymid - body_width/2)
              )

arrow = pch.PathPatch(arrow,facecolor=xkcd['xkcd:almost black'],lw=0,alpha=0.3)
ax.add_patch(arrow)

# MAPEAMENTO
ax.text(0.51,0.45, 
        s='Mapeamento', 
        style='italic',
        size=12,
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5, 
              'boxstyle': 'round',
              'pad': 0.5})

# SETA 3
xmid += 0.23
arrow = draw_my_arrow(A1=(xmid,ymid + body_width/2),
              B1=(xmid + body_length, ymid + body_width/2),
              C1=(xmid + body_length, ymid + body_width/2 + head_width),
              D=(xmid + body_length + head_length, ymid),
              C2=(xmid + body_length, ymid - body_width/2 - head_width),
              B2=(xmid + body_length, ymid - body_width/2),
              A2=(xmid,ymid - body_width/2)
              )

arrow = pch.PathPatch(arrow,facecolor=xkcd['xkcd:almost black'],lw=0,alpha=0.3)
ax.add_patch(arrow)


# VISUALIZAÇÃO
ax.text(0.74,0.45, 
        s='Visualização', 
        style='italic',
        size=12,
        bbox={'facecolor': xkcd['xkcd:dark green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5, 
              'boxstyle': 'round',
              'pad': 0.5})

# SETA 4
xmid += 0.22
arrow = draw_my_arrow(A1=(xmid,ymid + body_width/2),
              B1=(xmid + body_length, ymid + body_width/2),
              C1=(xmid + body_length, ymid + body_width/2 + head_width),
              D=(xmid + body_length + head_length, ymid),
              C2=(xmid + body_length, ymid - body_width/2 - head_width),
              B2=(xmid + body_length, ymid - body_width/2),
              A2=(xmid,ymid - body_width/2)
              )

arrow = pch.PathPatch(arrow,facecolor=xkcd['xkcd:almost black'],lw=0,alpha=0.3)
ax.add_patch(arrow)


# FIM
ax.text(0.96,0.45, 
        s='Fim', 
        size=12,
        style='normal',
        bbox={'facecolor': xkcd['xkcd:army green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5});


# ### Dado bruto
# 
# Empregamos o termo "dado bruto" (ou "dado cru") para fazer referência a toda sorte de dado disponível no mundo que não passou por nenhum processo de tratamento ou limpeza. Dados brutos raramente possuem uma estrutura lógica que facilita a compreensão de como estão organizados. Quando minimamente organizados, a melhor forma de manipulá-los é através de tabelas, serializações, ou outro formato apropriado capaz de gerar _datasets_.
# 
# #### Exemplo 1: registros cirúrgicos e obstétricos de um hospital
# 
# O arquivo `raw-data-hospital.txt` a seguir mostra um exemplo de dado bruto. Nele foram registrados os números de cirurgias \(C\) e partos \(P\) realizados nos blocos 1 (BLC1), 2 (BLC2) e 3 (BLC3) de um hospital público de grande porte no primeiro semestre de 2021 que levaram até 2 horas (I) ou mais do que 2 horas (II) de intervenção.

# ```
# -- raw-data-hospital.txt
# :BLC1 01/Fev/2021 I 30C 2P
# :BLC2 20/Fev/2021 II 0C 3P
# :BLC1 02/Mar/2021 I 0C 1P
# :BLC3 03/Mar/2021 II 0C 0P
# :BLC1 22/Abr/2021 I 7C 2P
# :BLC1 21-Abr/2021 II 1C 0p
# :BLC2 12-Mai/2021 I 22C 10P
# :BLC3 22-Mai/2021 II 1C 5P
# :BLC3 11/06/2021 I 36C 1P
# :blc2 01/06/2021 II 11C 22P
# .blc1 12.Jun.2021 I 33c 20P
# .blc2 30.Jun.2021 II 0C 17P
# .blc1 15.Jun.2021 I 42c 32P
# ```

# Como podemos ver pelo conteúdo, é difícil ter uma visualização clara das informações nele contidas. Além disso, ele possui uma diversidade de inconsistências de caracteres, produzindo uma formatação não padronizada. Antes de o utilizarmos para propósitos de visualização, devemos realizar operações de tratamento.

# #### Exemplo 2: monitoramento climático em tempo real
# 
# Há ocasiões em que arquivos bem estruturados estão disponíveis, mas, mesmo assim, é preciso algum tipo de manipulação para extrair deles a visualização desejada. Abaixo temos um extrato do arquivo `NEONDSTowerTemperatureData.hdf5`, que possui registros de temperatura coletados por sensores localizados em torres de captação ({numref}`fig-neonTower`) de dois domínios ecoclimáticos terrestres dos EUA (03: Flórida e 10: Colorado). 
# 
# O arquivo pleno pode ser baixado do site da [National Ecolological Observatory Network](https://www.neonscience.org/resources/learning-hub/tutorials/explore-data-hdfview). Trata-se de um dado formatado hierarquicamente, com extensão `hdf` (_Hierarchical Data Format_). Arquivos HDF podem ser entendidos como um grande diretório compactado que pode conter uma árvore de subdiretórios em muitos níveis. Eles possuem _datasets_ contendo objetos e atributos que podem ser agrupados e linkados internamente de forma variada. Neste curso, não faremos uma análise profunda sobre este formato, mas daremos exemplos de uso.
# 
# ```{figure} ../figs/NEONtower.png
# ---
# name: fig-neonTower
# alt: Torre de monitoramento.
# align: center
# width: 300px
# ---
# Torre de monitoramento climático com sensores (_boom_) distribuídos em 4 diferentes alturas e o quinto sensor posicionado no topo da torre, para captação de temperatura dos domínios ecoclimáticos terrestres americanos. Fonte: National Ecological Observatory Network/EUA.
# ```

# In[109]:


# importa módulo para ler HDF
import h5py as h5

# lê arquivo
file_hdf = h5.File('../data/NEONDSTowerTemperatureData.hdf5','r')

# imprime valores na hierarquia do domínio '03: Flórida'
for i in range(5):
    print(file_hdf['Domain_03']['OSBS']['min_1']['boom_1']['temperature'][i])


# A tupla armazena, nesta ordem: data e hora da medição, número de pontos de cálculo das estatísticas (60 segundos), temperaturas média, mínima e máxima (por minuto), variância, erro e incerteza. Mesmo assim, para produzirmos alguma visualização útil, temos que perscrutar o arquivo e entender cada um de seus atributos.

# ##### Introspectando arquivos _HDF_
# 
# A visualização da "árvore" de um arquivo HDF é possível via interface ou linha de comando. No primeiro caso, basta fazer o download da ferramenta [HDF View](https://www.hdfgroup.org/downloads/hdfview/) e seguir o guia do usuário. No segundo caso, há pelo menos dois modos práticos: 
# 
# - **Modo 1**: usando uma função definida pelo usuário para impressão dos objetos e atributos:
# 
# ```python
# # leitura do arquivo
# file_hdf = h5.File('../data/NEONDSTowerTemperatureData.hdf5','r')
# 
# # função para imprimir conteúdo do arquivo 'file_hdf'
# def print_h5_tree(name, obj):
#     print(name, dict(obj.attrs))
# 
# # chamada
# file_hdf.visititems(print_h5_tree)    
# ```
# 
# - **Modo 2**: usando o pacote `nexusformat` – instalável via `pip install nexusformat` —, que lida com o formato [NeXus](https://www.nexusformat.org):
# 
# ```python
# # importação da função `nxload`
# from nexusformat.nexus import nxload
# 
# # leitura do arquivo
# hdf5 = nxload('../data/NEONDSTowerTemperatureData.hdf5')
# 
# # impressão
# print(hdf5.tree)
# ```

# ### Pré-Processamento
# 
# Como já é sabido de cursos prévios sobre análise de dados, podemos realizar o _workflow_ tradicional com `pandas` e outros módulos necessários para extração, limpeza, tratamento e carregamento dos dados, a fim de torná-los adequados para manuseio. Podemos aplicar operações de filtragem, _casting_, _splitting_ de strings, renomeação de atributos, salvamento em formatos tabelares etc. 
# 
# Exercitando técnicas que já constam em nosso portifólio de conhecimento, podemos trabalhar sobre os arquivos dos exemplos anteriores para obter versões mais claras.

# #### Exemplo 1: reorganizando o arquivo de registros cirúrgicos e obstétricos

# In[665]:


import pandas as pd

# leitura de arquivo
df_h = pd.read_csv('../data/raw-data-hospital.txt',sep=' ',names=['Bloco','Data','Porte','Cirurgias','Partos'])

# remoção de inconsistências nas séries
df_h['Bloco'] = df_h['Bloco'].str.upper().str.strip(':BLC').str.strip('.BLC')
df_h['Data'] = df_h['Data'].str.replace('-','/').str.replace('.','/').\
                str.replace('/','-').str.replace('06','Jun').\
                str.replace(r'([A-Z][a-z][a-z])',lambda x: x.group().lower(),regex=True)
df_h['Cirurgias'] = df_h['Cirurgias'].str.strip('C').str.strip('c')
df_h['Partos'] = df_h['Partos'].str.strip('P').str.strip('p')

# reindexação
df_h.set_index('Data',inplace=True)


# A tabela que resulta do processamento realizado pelo código acima é a seguinte:

# In[666]:


df_h


# #### Exemplo 2: acessando dados de temperatura
# 
# Como o arquivo HDF possui uma hierarquia bem definida, podemos usar `keys` para acessar os _datasets_ e usar métodos do `numpy` e do `pandas` para recuperar a estrutura e criar os _dataframes_ diretamente.

# In[771]:


from pandas import DataFrame
from numpy import array

# conversão para array e posterior criação do dataframe
df_t = DataFrame(array(file_hdf['Domain_10']['STER']['min_1']['boom_2']['temperature']))
df_t.set_index('date')


# ### Mapeamento
# 
# O mapeamento visual é definido pelo processo de transferir os dados para a área de visualização e exibi-los através de estruturas visuais adequadas. Há muitos dados _abstratos_, cuja natureza não se vincula a uma estrutura topológica (forma) ou a uma localização geográfica. Nesses casos, a estrutura visual mais adequada pode não ser imediata. 
# 
# Por exemplo, as temperaturas coletadas do monitoramento ambiental são diretamente associadas com uma localização geográfica dentro do território americano. Os dados de registro hospitalar, embora também possam ser associados a um local físico (hospital), o local é desconhecido. Casos como este não possuem correspondência imediaata com dimensões. Outro exemplo de dado abstrato é, por exemplo, o consumo quilômetro/litro de automóveis que rodam a gasolina.
# 
# Há três estruturas fundamentais que consolidam o mapeamento visual:
# 
# - _substrato espacial_: define as dimensões do espaço físico onde a representação visual é criada (eixos Cartesianos, por exemplo);
# - _elementos gráficos_: caracterizam os elementos visuais que aparecem no espaço;
# - _propriedades gráficas_: definem-se pelas propriedades dos elementos gráficos às quais o olho humano (retina) são sensíveis. São também conhecidos como _atributos visuais_.

# #### Categorias e tipos de dados
# 
# Na {numref}`Seção %s <sec:termos-dados>`, elencamos algumas definições para tipos de dados. Neste ponto, vale acomodar o espectro das definições para considerar duas categorias principais e algumas subcategorias da seguinte forma:
# 
# - **Dado quantitativo**
#     - _Numérico contínuo_: valores numéricos (inteiros, racionais, reais);
#     - _Numérico discreto_: comumemente inteiros, mas podem ser fracionários quando não há valores intervalares a considerar;
# - **Dado qualitativo**
#     - _Categórico não ordenado_: discretos e sem ordem natural. Também chamado de _fatores_.
#     - _Categório ordenado_ (ordinal): discretos e ordenados. Também chamado de _fatores ordenados_.
# 
# _Data_, _hora_ e _texto_ são casos especiais que não categorizaremos por, às vezes, se comportarem como quantitativos, qualitativos ou nenhuma das duas categorias.
# 
# Alguns exemplos são vistos na {numref}`Tabela %s <tbl-tipos-dados>`.

# ```{table} Tipos e categorias de dados.
# :name: tbl-tipos-dados
# 
# | Categoria    | Tipo                       | Exemplo                                                     | Descrição                                                                                                                   |
# |:-------------|:---------------------------|:------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
# | Quantitativo | Numérico contínuo          | 2.7,1.22,10,1e-5                                            | Valores numéricos arbitrários.                                                                                              |
# | Quantitativo | Numérico discreto          | 1,2,3; 0.5,1.5, 2.5                                         | Números em unidades discretas. Fracionários em escalas especiais.                                                           |
# | Qualitativo  | Categórico não ordenado    | mamífero, crustáceo, aracnídeo                              | Categoria únicas, discretas e sem ordem aparente.                                                                           |
# | Qualitativo  | Categórico ordenado        | Péssimo, razoável, excelente                                | Categoria únicas, discretas e com ordenamento por significado. “Razoável" é algo entre “péssimo" e “excelente".             |
# | -            | Numérico contínuo/Discreto | 23/03/1996, 13:22                                           | Podem ser “contínuos" se considerados em intervalos contíguos (datas sucessivas), ou discretos, se tomados particularmente. |
# | -            | -                          | Tempos vividos não retornam; sim/talvez/não; jamais/sempre. | Texto em formato livre não possui categoria definida. Em outras situações, pode ser considerado categórico, discreto.       |
# ```

# #### Atributos e elementos visuais
# 
# [Jacques Bertin](https://en.wikipedia.org/wiki/Jacques_Bertin) estabeleceu os fundamentos teóricos para a visualização da informação elencando 7 atributos visuais, ou _canais_, ({numref}`Tabela %s <tbl-visual-bertin>`):
# 
# - posição;
# - tamanho;
# - orientação;
# - valor;
# - textura (ou granularidade);
# - cor; e
# - forma.
# 
# A figura abaixo, produzida unicamente com `matplotlib`, ilustra esses conceitos.

# In[661]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots(4,2,figsize=(10,6))

# 1
ax[0,0].set_axis_off()
ax[0,0].set_ylim([0.4,0.5])
ax[0,0].plot(.5,.46,'o',color='k')
ax[0,0].axhline(y=.45,xmin=0.3,xmax=0.7,c='k',lw=1.0)
ax[0,0].axvline(x=0.49,ymin=0.45,ymax=0.5,c='k',lw=1.0)
ax[0,0].axvline(x=0.50,ymin=0.45,ymax=0.5,c='k',lw=1.0)
ax[0,0].axvline(x=0.51,ymin=0.45,ymax=0.5,c='k',lw=1.0)

ax[0,0].text(0.4965,0.41, s='Posição', size=9, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})


# 2
ax[0,1].set_axis_off()
ax[0,1].set_ylim([0.4,0.5])
ax[0,1].axhline(y=.46,xmin=0.3,xmax=0.7,c='k',lw=1.0)
ax[0,1].axhline(y=.45,xmin=0.3,xmax=0.8,c='k',lw=1.0)
ax[0,1].axhline(y=.44,xmin=0.3,xmax=0.9,c='k',lw=1.0)

ax[0,1].text(0.496,0.41, s='Tamanho', size=9, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})

# 3
ax[1,0].set_axis_off()
ax[1,0].set_ylim([0.4,0.5])
ax[1,0].plot([0.49,0.495],[0.46,0.46],c='k')
ax[1,0].plot([0.5,0.5],[0.44,0.48],c='k')
ax[1,0].plot([0.505,0.51],[0.48,0.44],c='k')

ax[1,0].text(0.498,0.41, s='Orientação', size=9, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5});


# 4
ax[1,1].set_axis_off()
ax[1,1].set_ylim([0,0.3])
ax[1,1].add_patch(ptc.Rectangle(xy=(0.26,0.15),width=.1, height=.1, color='k',alpha=0.3))
ax[1,1].add_patch(ptc.Rectangle(xy=(0.51,0.15),width=.1, height=.1, color='k',alpha=0.6))
ax[1,1].add_patch(ptc.Rectangle(xy=(0.76,0.15),width=.1, height=.1, color='k'))

ax[1,1].text(0.51,0.03, s='Valor', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})

# 5
ax[2,0].set_axis_off()
ax[2,0].set_xlim([0,5])
ax[2,0].set_ylim([0,0.3])

dh = 0.05
for i in range(8):
      xo = 0.1 + i*2*dh
      ax[2,0].add_patch(ptc.Rectangle(xy=(xo,0.1),width=.1-dh/2, height=.18, color='k'))


dh = 0.08
for i in range(8):
      xo = 1.2 + i*2*dh
      ax[2,0].add_patch(ptc.Rectangle(xy=(xo,0.1),width=.1-dh/2, height=.18, color='k'))

dh = 0.15
for i in range(8):
      xo = 2.8 + i*2*dh
      ax[2,0].add_patch(ptc.Rectangle(xy=(xo,0.1),width=.1-dh/2, height=.18, color='k'))

ax[2,0].text(2.1,0.02, s='Textura', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})


# 6
ax[2,1].set_axis_off()
ax[2,1].set_ylim([0,0.3])
ax[2,1].add_patch(ptc.Rectangle(xy=(0.26,0.15),width=.1, height=.1, color='r'))
ax[2,1].add_patch(ptc.Rectangle(xy=(0.51,0.15),width=.1, height=.1, color='g'))
ax[2,1].add_patch(ptc.Rectangle(xy=(0.76,0.15),width=.1, height=.1, color='b'))

ax[2,1].text(0.53,0.03, s='Cor', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})


# 7
ax[3,0].set_axis_off()
ax[3,0].set_ylim([0,0.3])
ax[3,0].add_patch(ptc.Circle(xy=(0.24,0.15),radius=0.05, color='k'))
ax[3,0].add_patch(ptc.Rectangle(xy=(0.44,0.1),width=.1, height=.1, color='k'))
x0,y0 = 0.65,0.15
h = 0.1
ax[3,0].add_patch(ptc.Polygon(xy=[[x0,y0],[x0+h/2,y0+h/2],[x0+h,y0],[x0+h/2,y0-h/2]],color='k'))

ax[3,0].text(0.43,0.01, s='Forma', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})

# 8
ax[3,1].set_axis_off()


# ```{table} Designações para os atributos visuais de Bertin.
# :name: tbl-visual-bertin
# 
# | Atributo    | Designações | 
# |:-------------|:-----------|
# | Posição | esquerda, centro, direita etc. |
# | Tamanho | pequeno, médio, grande etc.|
# | Orientação | horizontal, vertical, oblíqua |            
# | Valor | claro, médio, escuro (tons de cinza) |
# | Textura | fina, média, grossa |            
# | Cor | vermelho, verde, azul etc. |            
# | Forma | círculo, retângulo, polígono de n lados etc. |            
# ```
# 
# Os elementos visuais possíveis são 4:
# 
# - ponto;
# - linha;
# - superfície; e
# - volume.
# 
# Exemplos desses elementos visuais também puramente criados com `matplotlib` são desenhados a seguir.

# In[512]:


import matplotlib.pyplot as plt
import matplotlib.patches as ptc

fig, ax = plt.subplots(2,2,figsize=(10,3))

# 1
ax[0,0].set_axis_off()
ax[0,0].set_ylim([0,0.3])
ax[0,0].add_patch(ptc.Circle(xy=(0.4,0.2),radius=0.05,color='k'))
ax[0,0].add_patch(ptc.Rectangle(xy=(0.5,0.15),width=.1, height=.1, color='k'))

ax[0,0].text(0.4,0.05, s='Pontos', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})

# 2
ax[0,1].set_axis_off()
ax[0,1].set_ylim([0.0,0.3])
ax[0,1].axhline(y=.2,xmin=0.2,xmax=0.8,c='k',lw=3.0)

ax[0,1].text(0.4,0.05, s='Linhas', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})


# 3
ax[1,0].set_axis_off()
ax[1,0].set_ylim([0.24,0.27])
ax[1,0].add_patch(ptc.Polygon(xy=[[0.22,0.26],[0.39,0.265],[0.45,0.26],[0.26,0.255]],color='k',alpha=0.8))
ax[1,0].add_patch(ptc.Polygon(xy=[[0.65,0.252],[0.63,0.265],[0.85,0.267],[0.84,0.254]],color='k',alpha=0.8))


ax[1,0].text(0.35,0.24, s='Superfícies', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5})


# 4 
ax[1,1].set_axis_off()
h, dh = 0.3, 0.005
x,y = 0.25,0.5
Q1 = [ [x,y], [x,y+h], [x+h, y+h], [x+h,y] ]
Q2 = [ [x+h+dh ,y], [x+4/3*h+dh,y+h/3], [x+4/3*h+dh,y+4/3*h], [x+h+dh,y+h] ]
Q3 = [ [x,y+h+3*dh], [x+h/3,y+4/3*h+3*dh], [x+4/3*h, y+4/3*h+3*dh], [x+h,y+h+3*dh] ]

ax[1,1].add_patch(ptc.Polygon(xy=Q1,color='k',alpha=1.0))
ax[1,1].add_patch(ptc.Polygon(xy=Q2,color='k',alpha=1.0))
ax[1,1].add_patch(ptc.Polygon(xy=Q3,color='k',alpha=1.0))


ax[1,1].text(0.38,0.0, s='Volumes', size=10, style='normal',
        bbox={'facecolor': xkcd['xkcd:nasty green'], 
              'edgecolor':xkcd['xkcd:almost black'], 
              'alpha': 0.5,
              'boxstyle': 'round',
              'pad': 0.5});


# ### Visualização
# 
# A representação visual é o produto final obtido quando se segue o modelo referencial apresentado anteriormente. Para atingirmos uma visualização eficaz, além de levar em conta todos os aspectos já discutidos na etapa do mapeamento, devemos nos atentar para o bom _design_ e para o propósito da visualização que desenvolveremos ({cite:p}`mazza2009introduction`).
# 
# Duas características cruciais a observar em um projeto de visualização são: 
# - reproduzir a informação com fidelidade; 
# - facilitar a compreensão do espectador; 
# - analisar o tipo e a natureza dos dados que serão representados; e
# - entender a audiência a quem os dados serão direcionados.
# 
# Elaborando-se um plano preliminar para a representação visual almejada, a probabilidade de sucesso do projeto é maior. Este plano deve considerar as seguintes variáveis e questões ({numref}`Tabela %s <tbl-projeto-visualizacao>`,adaptada deste [site](https://adenilsongiovanini.com.br/blog/semiologia-grafica-aplicada-e-cartografia-tematica/)):
# 
# 1. _Definição do problema_: que representação é necessária? O que desejo comunicar?
# 2. _Exame da natureza dos dados_: os dados são quantitativos ou qualitativos? Como mapeá-los?
# 3. _Dimensões_: qual é o número de dimensões dos dados (atributos)? Quais são independentes e quais são dependentes? Os dados são _univariados_ (uma dimensão varia com respeito a outra)? _Bivariados_ (uma dimensão varia com respeito a outras duas)? _Trivariados_ (uma dimensão varia com respeito a outras três)? _Multivariados_ (uma dimensão varia com respeito a quatro ou mais dimensões independentes)?
# 4. _Estrutura de dados_: os dados são _lineares_ (codificados em vetores, tabelas, matrizes, coleções etc.)? São _temporais_ (mudam com o tempo)? São _geográficos_ ou _espaciais_ (possuem correspondência com algo físico, como mapas, plantas, projeções de terreno etc.)? São _hierárquicos_ (sugerem organizações, diretórios, genealogias etc.)? Ou são em forma de _redes_ (descrevem relacionamento entre entidades)?
# 5. _Tipo de interação_: a visualização é _estática_ (imagem impressa fisicamente ou em tela de computadores)? _Transformável_ (usuário altera parâmetros que modificam e transformam os dados)? Ou é _manipulável_ (usuário tem possibilidade de girar elementos 3D, aplicar _zoom_)?
# 
# ```{table} Etapas do projeto preliminar de visualização de dados.
# :name: tbl-projeto-visualizacao
# 
# | Problema | Tipo de dado | Dimensões | Estrutura de dados |  Tipo de interação |
# |:-------------|:-----------|:-----------|:-----------|:-----------|
# |comunicar<br>explorar<br>confirmar|quantitativo<br>qualitativo|univariado<br>bivariado<br>trivariado<br>multivariado|linear<br>temporal<br>espacial<br>hierárquico<br>rede|estático<br>transformável<br>manipulável| 
# ```

# #### Exemplo 1: visualizando o número de cirurgias e partos por bloco

# In[740]:


import seaborn as sns

# reindexação
df_h2 = df_h.reset_index()

# conversão do tipo de dados
df_h2['Cirurgias'] = df_h2['Cirurgias'].astype(int)
df_h2['Partos'] = df_h2['Partos'].astype(int)

# plotagem principal
fig, ax = plt.subplots(1,2,figsize=(10,2),sharey=True)
ax[0].grid(alpha=0.5)
ax[1].grid(alpha=0.5)
p1 = sns.barplot(x='Bloco',y='Cirurgias',hue='Porte',data=df_h2,errorbar=None,palette='Blues',ax=ax[0])
p2 = sns.barplot(x='Bloco',y='Partos',hue='Porte',data=df_h2,errorbar=None,palette='Blues',ax=ax[1])

# eixos
p1.spines['top'].set_visible(False)
p1.spines['right'].set_visible(False)
p1.spines['bottom'].set_position(('axes', -0.1))

p2.spines['top'].set_visible(False)
p2.spines['right'].set_visible(False)
p2.spines['bottom'].set_position(('axes', -0.1))

# legenda
p1.get_legend().remove()
p2.legend(title='Porte',bbox_to_anchor=(1.2,1.0));


# #### Exemplo 2: plotando série temporal de temperatura

# In[928]:


import numpy as np

df_hours = df_t['date'][0::60].index
df_ti = df_t.iloc[df_hours][:48]

fig, ax = plt.subplots(figsize=(10,2))
ax.plot(df_ti['mean'],c='#be5631',lw=1.5)

da = np.array(list((df_ti['mean'].index)))
db = np.array(2*[str(i) + 'h' for i in range(0,24)])
ax.set_xticks(da,db,fontsize=5)

half = int(len(da)/2)

ax.axvline(0,ls='--',lw=1,c='#d1886e',alpha=0.4)
ax.axvline(da[half],ls='--',lw=1,c='#d1886e',alpha=0.4)
ax.grid(axis='y',ls=':',c='k',alpha=0.4)

ax.set_xlabel('Tempo',fontsize=9)
ax.set_ylabel('Temperatura',fontsize=9)

ax.text(10,-4,s='01/04/2014',fontsize=7,c='#d1886e')
ax.text(1450,-4,s='02/04/2014',fontsize=7,c='#d1886e');


# ## Referências
# 
# ```{bibliography}
# :filter: docname in docnames
# ```
