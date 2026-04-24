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