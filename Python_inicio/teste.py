#Vamos começar a trabalhar com python.

#Usando objetos comuns do R (com panda):
import pandas as pd
#Vetores quaisquer
teste1 = pd.Series(data = [1,2,3,4,5,6,7,8,9,10])
#Data frames
teste2 = {'individuo' : ['laura','carlos','pedro','joao'],'renda':[2000.00,1350.00,11000.00,3400.00],'carro':[True,False,True,False]}
dados = pd.DataFrame(teste2)
dados.to_csv('dadosBestas.csv')
dados.describe()
dados[0:1]
dados[dados['individuo']=='laura']
dados = dados.set_index('individuo')
dados[dados['carro']][['renda']]
dados.loc['laura']
dados['renda2'] = dados['renda']/1000
dados.plot(x='individuo',y=['renda2','anosServico'],kind='bar')
dados.plot(x='individuo',y='anosServico',kind='bar')

#Trabalhando com numpy?
import numpy as np
a = np.array([1,2,3,4])
b = np.array([(1,2,3),(4,5,6),(7,8,9)])
np.random.normal(5,2,10)# =  rnorm(5,2,10)
b.T #Transpose

#Começando a trabalhar com "análises" de dados
import statsmodels.api as sm
import statsmodels.formula.api as smf
teste2['anosServico'] = [15,10,20,15]
dados = pd.DataFrame(teste2)
modelo = smf.ols('renda~anosServico+C(carro)',data=dados).fit()
sm.stats.anova_lm(modelo)
print(modelo.summary())
smf.glm('np.log(renda)~anosServico+C(carro)',data=dados,family=sm.families.Gamma()).fit()
y = np.asarray(dados.loc[:,['renda']])
aux = [int(i) for i in np.array(dados.loc[:,['carro']])]
dados['aux'] = aux
x = np.asarray(dados.loc[:,['anosServico','aux']])
x =sm.add_constant(x)
#design = sm.tools.categorical(np.array(dados.loc[:,['carro']]))
modelo2 = sm.GLM(y,x,data=dados,family=sm.families.Poisson()).fit()
modelo2.summary()
