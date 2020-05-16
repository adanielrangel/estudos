# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:01:28 2020

@author: adani
"""

import pandas as pd 
import numpy as np 
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

p = 'C:/Users/adani/Desktop/estudo_data/Python-Data-Science-and-Machine-Learning-Bootcamp/5. Machine Learning/Regressões Lineares/USA_Housing.csv'

usahousing = pd.read_csv(p)

usahousing.describe()

#pair plote para ver a distribuição das veriaveis 
sns.pairplot(usahousing)

#heatmap para ver a corelação 
sns.heatmap(usahousing.corr())

#divido em x e y 
#tem que esquecer a vareavel adress pq ela não é numerica 
X = usahousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
Y = usahousing['Price']
#quebra em treino e em test 
X_train, X_test, Y_train,Y_test = train_test_split(X,Y, test_size= 0.4, random_state = 101)

#instancio o obj
lm = LinearRegression()
#faço o fit 
lm.fit(X_train,Y_train)

#alguns parametros para interpretarmos 
print(lm.intercept_)
print(lm.coef_)

#colocando os coeficientes num df para ficar bunitinho 
coefs = pd.DataFrame(lm.coef_,X.columns,columns=['coefs'])
#como ler os coeficientes 
# o valor que pe mostrado é representa o quanto um almento de 1 unidade 
#na quela variavel vai impactar na variavel alvo do modelo 

# para eu fazer meu test é só rodar o metodo predict do lm 
#ele retorna um df no mesmo formato do seu imput 

predict = lm.predict(X_test)

#ok vamos ver se esse modelo ta bom 

# se o modelo tivesse bom ele deveria 
#me dar uma linha reta em um grafico de disperção 
plt.scatter(Y_test,predict)
#ele se aproxima bem de uma linha reta

# outra maneira é calcular os erros 
#y_test-predic = erro 
# e ele deveria me retornar uma normal ao redor do 0 
sns.distplot((Y_test-predict))

# existem 3 metricas padros para ver o fi do seu modelo 

# erro abisoluto medio 
# calcula a media dos erros 
#mae
print('MAE', metrics.mean_absolute_error(Y_test,predict))

#media do quadrado dos erros 
#calcual a media dos erros^2 
#mse
print('MSE', metrics.mean_squared_error(Y_test,predict))

#rais da media dos quadrados dos erros 
#calcual a media dos rais(erros^2)
#RMSE
print('RMSE', np.sqrt(metrics.mean_squared_error(Y_test,predict)))




















