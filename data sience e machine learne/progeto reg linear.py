# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:24:15 2020

@author: adani
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


['Email', 'Address', 'Avatar', 'Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership', 'Yearly Amount Spent']

p= 'C:/Users/adani/Desktop/estudo_data/Python-Data-Science-and-Machine-Learning-Bootcamp/5. Machine Learning/Regressões Lineares\Ecommerce Customers.csv'

df= pd.read_csv(p)

df.head()
df.describe()
df.info()

#checando as correlaçoes 
sns.pairplot(df)

# checando a distribuição da minha variavel alvo 
sns.distplot(df['Yearly Amount Spent'])

# indo mais a fundo na analise das variaveis que são importante 
sns.jointplot(data=df,x='Yearly Amount Spent',y='Time on Website')
sns.jointplot(data=df,x='Yearly Amount Spent',y='Time on App')
# tempo no app parece mais relacionado com o valor gasto 

# vamos quebrar em reste e treino 
x = df[['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership',]]

y = df['Yearly Amount Spent']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=101)

#montando o modelo 

lm = LinearRegression()
lm.fit(x_train,y_train)

#fazendo as prediçoes 
predict = lm.predict(x_test)

#vendo se o modelo deu bom 
sns.scatterplot(y_test,predict)

#ficou bem alinhado, mas tem poco dado nessa base 

#calculando o erro 
erro = y_test-predict 

#calculando os indicadore 
print('erro medio abisoluto', metrics.mean_absolute_error(y_test,predict))

print('erro medio quadrado', metrics.mean_squared_error(y_test,predict))

print('rais do erro medio quadrado', np.sqrt( metrics.mean_squared_error(y_test,predict)))

#esqueci de checar o intercep e os coefs

lm.intercept_

lm.coef_

 coefs = pd.DataFrame(lm.coef_,x.columns,columns=['coefs'])
 
 #conclusao a empresa deve otimisar o tempo no app 
 
 
 
