
import numpy as np
import seaborn as sb
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import time
grade = np.zeros([11,11,25])
#grade[[1,2,5],[3,6,7],0] = 1
grade[5,5,0] = 1

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
infecta = 0.5
cura = 1
def evolucao(dados):
    retorno = dados.copy()
    d1,d2,d3 = dados.shape
    doencaNorte = np.zeros([d1,d2,150])
    doencaLeste = doencaNorte.copy()
    doencaOeste = doencaNorte.copy()
    doencaSul = doencaNorte.copy()
    curas = doencaNorte.copy()
    canhao = np.array(0)
    for i in range(d1):
        for j in range(d2):  
            dn,dl,do,ds = np.random.poisson(infecta*30,4)           
            heal = np.random.poisson(30)  
            if(dn>=150):dn=150
            if(dl>=150):dl=150
            if(do>=150):do=150
            if(ds>=150):ds=150
            if(heal>=150):heal=150
            doencaNorte[i,j,:] = np.append(np.random.exponential(1/(infecta),dn),np.ones([150-dn])*5000)
            doencaLeste[i,j,:] = np.append(np.random.exponential(1/(infecta),dl),np.ones([150-dl])*5000)
            doencaOeste[i,j,:] = np.append(np.random.exponential(1/(infecta),do),np.ones([150-do])*5000)
            doencaSul[i,j,:] = np.append(np.random.exponential(1/(infecta),ds),np.ones([150-ds])*5000)
            curas[i,j,:] = np.append(np.random.exponential(1/(cura),heal),np.ones([150-heal])*5000)
#            doencaNorte[i,j,:].sort()
  #          doencaLeste[i,j,:].sort()
 #           doencaSul[i,j,:].sort()
 #           doencaOeste[i,j,:].sort()
 #           curas[i,j,:].sort()
            doencaNorte[i,j,:] = np.cumsum(doencaNorte[i,j,:])
            doencaLeste[i,j,:] = np.cumsum(doencaLeste[i,j,:])
            doencaSul[i,j,:] = np.cumsum(doencaSul[i,j,:])
            doencaOeste[i,j,:] = np.cumsum(doencaOeste[i,j,:])
            curas[i,j,:] = np.cumsum(curas[i,j,:])
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
                for m in range(150):
                    if(curas[i,j,m]==canhao[t]):
                        print('i = %d, j = %d, k= %d, t=%d,canhao = %.2f, Cura!'%(i,j,k,t,canhao[t]))
                        retorno[i,j,k]=0
                        break
#                for m in range(len(doencaNorte[i,j,:])):
                    if(doencaNorte[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(j<=9): 
                            retorno[i,(j+1),k]=1
                            print('i = %d, j = %d, k= %d, t=%d,canhao = %.2f, Norte!'%(i,j,k,t,canhao[t]))
                            break
 #               for m in range(len(doencaLeste[i,j,:])):
                    if(doencaLeste[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(i<=9):
                            print('i = %d, j = %d, k= %d, t=%d,canhao = %.2f, Leste!'%(i,j,k,t,canhao[t]))
                            retorno[(i+1),j,k]=1
                            break
  #              for m in range(len(doencaSul[i,j,:])):
                    if(doencaSul[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(j>=1):
                            retorno[i,(j-1),k]=1
                            print('i = %d, j = %d, k= %d, t=%d,canhao = %.2f, Sul!'%(i,j,k,t,canhao[t]))
                            break
   #             for m in range(len(doencaOeste[i,j,:])):
                    if(doencaOeste[i,j,m]==canhao[t] and retorno[i,j,k]==1):
                        if(i>=1): 
                            print('i = %d, j = %d, k= %d, t=%d,canhao = %.2f, Oeste!'%(i,j,k,t,canhao[t]))
                            retorno[(i-1),j,k]=1
                            break
        if(canhao[t]>=(k+1)):
            if(k<=23):
                k+=1
                for i in range(d1):
                    for j in range(d2):
                        retorno[i,j,k] = retorno[i,j,(k-1)]
            else:
                break
    return(retorno)    
        
    
        
        
    
#np.random.exponential(1/5,5)

testando = evolucao(grade)

#_________________________
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
#_________________________
grade2 = np.zeros([grade.shape[0],grade.shape[1],grade.shape[2]+1])
grade2[:,:,0] = grade[:,:,0]
grade2[:,:,1:] = testando
#testando = np.append(grade[:,:,0],testando)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
aux = ax.matshow(grade2[:,:,0])
def animacao(t):
   ax.clear()
   ax.matshow(grade2[:,:,t])
   ax.set_title('instante: %d' % t)
   if(t>=(grade2.shape[2]-1)):
        ax.set_title('fim')   

ani = animation.FuncAnimation(fig,animacao,interval=1000)
plt.show()
