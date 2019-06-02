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
dados.plot?

