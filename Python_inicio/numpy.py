#Maintenant on va essayer de jouer avec le paquet numpy (je vais écrire en français pour améliorer mon vocabulaire.)

import numpy as np
import seaborn as sns
echantillon = np.random.normal(3,2,500) #crée une echantillon de 500 observations avec distribuition normale, moyenne 3 et écart type 2
echantillon[1:10:2]

ec = np.array([[[1],[2],[3]], [[4],[5],[6]]])
ec2 = np.array([[1,2],[3,4],[5,6]])
ec2[(0,2),(0)]


np.arange(6).reshape(2,3)
for i in np.nditer(ec2):
    print(i)
    
np.mean(echantillon).round(2)
np.std(echantillon).round(2)

sns.distplot(echantillon)
iris = sns.load_dataset('iris')
sns.pairplot(iris)
iris
sns.boxplot(x=iris['species'],y=iris[iris.columns[0]])
sns.boxplot(x=iris['species'],y=iris[iris.columns[1]])
sns.boxplot(x=iris['species'],y=iris[iris.columns[2]])
sns.boxplot(x=iris['species'],y=iris[iris.columns[3]])
sns.lineplot(x=iris[iris.columns[1]],y=iris[iris.columns[2]])
sns.lmplot(iris.columns[0],iris.columns[2],data=iris)  #C'est intéressant... mais je prefére R...
sns.pairplot(data = iris[[iris.columns[1],iris.columns[2]]])
sns.swarmplot(x = iris[iris.columns[0]],y = iris[iris.columns[1]],hue=iris[iris.columns[4]])
