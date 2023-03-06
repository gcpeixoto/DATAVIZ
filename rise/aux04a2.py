import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# limites do domínio: região do plano [a,b] x [c,d]
a, b = -2, 2
c, d = -1, 3

# no. de pontos em cada direção
nx, ny = 40, 40 

# distribuição dos pontos
x = np.linspace(a,b,nx)
y = np.linspace(c,d,ny)

# grade 2D
[X,Y] = np.meshgrid(x,y)

# superfíe
Z = 4*np.exp(-( ( X - (a+b)/2 )**2 + ( Y - (c+d)/2 )**2 ))

# plotagem
fig = plt.figure(figsize=(10,4),constrained_layout=True)
fig.suptitle('$f(x,y) = 4e^{ - \
     \\left[ \\left( x -  \\frac{a+b}{2} \\right)^2  + \
             \\left( y -  \\frac{c+d}{2} \\right)^2 \\right] }$')

gs = fig.add_gridspec(1,3) 
ax1 = fig.add_subplot(gs[0],projection='3d')
ax2 = fig.add_subplot(gs[1],projection='3d')
ax3 = fig.add_subplot(gs[2])

# superfície
ax1.set_zlim(0,5)
s = ax1.plot_surface(X,Y,Z,cmap=cm.jet)
fig.colorbar(s, shrink=0.5,ax=ax1)
ax1.set_title('Superfície',fontsize=8)

# aramado
ax2.set_zlim(0,5)
s = ax2.plot_wireframe(X,Y,Z,cmap=cm.jet,lw=0.4)
ax2.axis('off')
ax2.set_title('Superfície aramada',fontsize=8)

# curvas de nível com preenchimento
ax3.contourf(X,Y,Z,cmap=cm.jet)
ax3.axis([a,b,c,d])
ax3.set_title('Curvas de nível',fontsize=8);
