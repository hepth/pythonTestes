#Ce programme tentera de créer une simulation du processus de contact proposé par Harris (1974).

import numpy as np
import seaborn as sb
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import time
grade = np.zeros([11,11,25])
grade[[1,2,5],[3,6,7],0] = 1
#grade[5,5,0] = 1

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
infecta = 2
cura = 1
def evolucao(dados):
    retorno = dados.copy()
    d1,d2,d3 = dados.shape
    doencaNorte = np.zeros([d1,d2,50])
    doencaLeste = doencaNorte.copy()
    doencaOeste = doencaNorte.copy()
    doencaSul = doencaNorte.copy()
    curas = doencaNorte.copy()
    canhao = np.array(0)
    for i in range(d1):
        for j in range(d2):  
            dn,dl,do,ds = np.random.poisson(infecta*25,4)           
            heal = np.random.poisson(1)  
            if(dn>=50):dn=50
            if(dl>=50):dl=50
            if(do>=50):do=50
            if(ds>=50):ds=50
            if(heal>=50):heal=50
            doencaNorte[i,j,:] = np.append(np.random.exponential(1/(infecta),dn),np.zeros([50-dn]))
            doencaLeste[i,j,:] = np.append(np.random.exponential(1/(infecta),dl),np.zeros([50-dl]))
            doencaOeste[i,j,:] = np.append(np.random.exponential(1/(infecta),do),np.zeros([50-do]))
            doencaSul[i,j,:] = np.append(np.random.exponential(1/(infecta),ds),np.zeros([50-ds]))
            curas[i,j,:] = np.append(np.random.exponential(1/(cura),heal),np.zeros([50-heal]))
            canhao = np.append(canhao,doencaNorte[i,j,:])
            canhao = np.append(canhao,doencaLeste[i,j,:])
            canhao = np.append(canhao,doencaOeste[i,j,:])
            canhao = np.append(canhao,doencaSul[i,j,:])
            canhao = np.append(canhao,curas[i,j,:])
    canhao = canhao[1:canhao.shape[0]]
    canhao.sort()
    k = 0
    for t in range(len(canhao)): 
        for i in range(d1):
            for j in range(d2):
                for m in range(len(curas[i,j,:])):
                    if(curas[i,j,m]==canhao[t]): retorno[i,j,k]=0
                for m in range(len(doencaNorte[i,j,:])):
                    if(doencaNorte[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(j<=9): 
                            retorno[i,(j+1),k]=1
                for m in range(len(doencaLeste[i,j,:])):
                    if(doencaLeste[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(i<=9):
                            retorno[(i+1),j,k]=1
                for m in range(len(doencaSul[i,j,:])):
                    if(doencaSul[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(j>=1):
                            retorno[i,(j-1),k]=1
                for m in range(len(doencaOeste[i,j,:])):
                    if(doencaOeste[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(i>=1): 
                            retorno[(i-1),j,k]=1
        if(canhao[t]>=k):
            if(k<23):
                k+=1
            else:
                break
    return(retorno)    
        
    
        
        
    
#np.random.exponential(1/5,5)

testando = evolucao(grade)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
aux = ax.matshow(testando[:,:,0])

def animacao(t):
   ax.clear()
   ax.matshow(testando[:,:,t])
   ax.set_title('instante: %d' % t)
   if(t>=(testando.shape[2]-1)):
        ax.set_title('fim')   

ani = animation.FuncAnimation(fig,animacao,interval=250)
plt.show()
