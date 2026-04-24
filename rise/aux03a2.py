import matplotlib.colors as clr
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

fig, ax = plt.subplots(4,2,figsize=(10,6))

xkcd = clr.XKCD_COLORS

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