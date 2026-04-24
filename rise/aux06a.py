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

