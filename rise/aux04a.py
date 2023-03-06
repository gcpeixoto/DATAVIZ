import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc_file_defaults()

# dados
x = np.array([1,3.16,10,31.6,100])

# figuras
fig, ax = plt.subplots(1,4,figsize=(10,1),constrained_layout=True)

# plotagens
ax[0].plot(x,0*x,'o',ms=8,c='#117029')
ax[0].get_yaxis().set_visible(False)
ax[0].axis('equal')
ax[0].spines['bottom'].set_color('gray')
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].set_xlabel('$x$')
ax[0].set_title('dados originais; escala linear',fontsize=8)

ax[1].semilogx(x,0*x,'o',ms=8,c='#117029')
ax[1].get_yaxis().set_visible(False)
ax[1].axis('equal')
ax[1].spines['bottom'].set_color('gray')
ax[1].spines['top'].set_visible(False)
ax[1].spines['left'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].set_xlabel('$x$')
ax[1].set_title('dados originais; escala logarítmica',fontsize=8)

ax[2].plot([1,2,3,4,5],0*x,'o',ms=8,c='#117029')
ax[2].get_yaxis().set_visible(False)
ax[2].axis('equal')
ax[2].set_xticks([1,2,3,4,5])
ax[2].set_xticklabels([0,0.5,1.0,1.5,2.0])
ax[2].spines['bottom'].set_color('gray')
ax[2].spines['top'].set_visible(False)
ax[2].spines['left'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].set_xlabel('$\log_{10}(x)$')
ax[2].set_title('dados transformados; escala linear',fontsize=8)

ax[3].plot([1,2,3,4,5],0*x,'o',ms=8,c='#117029')
ax[3].get_yaxis().set_visible(False)
ax[3].axis('equal')
ax[3].set_xticks([1,2,3,4,5])
ax[3].set_xticklabels([1,3.16,10,31.6,100])
ax[3].spines['bottom'].set_color('gray')
ax[3].spines['top'].set_visible(False)
ax[3].spines['left'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].set_xlabel('$x$')
ax[3].set_title('dados originais; escala logarítmica',fontsize=8);
