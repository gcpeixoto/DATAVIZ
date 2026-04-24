import matplotlib.colors as clr
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

fig, ax = plt.subplots(2,2,figsize=(10,3))

xkcd = clr.XKCD_COLORS

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