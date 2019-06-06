#Ce programme tentera de créer une simulation du processus de contact proposé par Harris (1974).

import numpy as np
import seaborn as sb
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import time
grade = np.zeros([51,51,25])
grade[25,25,0] = 1

#def conversor(dados):
#    d1 = dados.shape[0]
#    d2 = dados.shape[1]
#    d3 = dados.shape[2]
#    count=0
#    retorno = np.zeros([d1*d2*d3,4])
#    for k in range(d3):
#        for i in range(d1):
#            for j in range(d2):
#                retorno[count,:] = np.array([k,i,j,dados[i,j,k]])
#                count +=count
#    return retorno

#lala = conversor(grade)
infecta = 5
cura = 1
def evolucao(dados):
    d1,d2,d3 = dados.shape
    doencaNorte = np.zeros([d1,d2,500])
    doencaLeste = doencaNorte.copy()
    doencaOeste = doencaNorte.copy()
    doencaSul = doencaNorte.copy()
    curas = doencaNorte.copy()
    for i in range(d1):
        for j in range(d2):  
            doencaNorte[i,j,:] = np.random.exponential(infecta*25,500)
            doencaLeste[i,j,:] = np.random.exponential(infecta*25,500)
            doencaOeste[i,j,:] = np.random.exponential(infecta*25,500)
            doencaSul[i,j,:] = np.random.exponential(infecta*25,500)
            curas[i,j,:] = np.random.exponential(cura*25,500)
    for k in np.arange(1,d3,1):
        for i in range(d1):
            for j in range(d2):
                if(dados[i,j,k]==1):
                    
                    
        
        
    
#np.random.exponential(1/5,5)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
aux = ax.matshow(grade[:,:,0])

def animacao(t):
   ax.clear()
   ax.matshow(grade[:,:,t])
   ax.set_title('instante: %d' % t)
   if(t>=(grade.shape[2]-1)):
        ax.set_title('fim')   

ani = animation.FuncAnimation(fig,animacao,interval=250)
plt.show()
