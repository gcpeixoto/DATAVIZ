import matplotlib.pyplot as plt
import numpy as np

# gera sequencia aleatória
np.random.seed(10)
text = np.random.randint(0,9,80)

# casting
ss = ''
for si in text:
    ss += str(si)
text = ss; del ss

# figura
fig, ax = plt.subplots(2,1,figsize=(8,0.5),constrained_layout=True)
ax[0].set_xlim(0,1)
ax[0].axis('off'); 
ax[1].axis('off')

# anotação
x = 0.01; dx = 0.02
for si in text:
    ax[0].text(x=x,y=0.5,s=si,fontsize=10,va='center',color='gray')
    if si == '5':
        ax[1].text(x=x,y=0.5,s=si,fontsize=10,va='center',color='r')
    else:
        ax[1].text(x=x,y=0.5,s=si,fontsize=10,va='center',color='gray')
    x += dx
