# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:02:05 2020

@author: adani
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn import metrics

f = 'C:/Users/adani/Desktop/estudo_data/reg_linar_2/data-science/reg-linear-II/dados/dataset.csv'
db = pd.read_table(f,sep=';')

dsc = db.describe().round(2)
correl = db.corr().round(2)

sns.set_palette('Accent')
sns.set_style('darkgrid')

ax = sns.boxplot(data=db['Valor'],orient='h',width=0.3)
ax.figure.set_size_inches(20,5)
ax.set_title('preço dos imoveis')
ax.set_xlabel('reais')

ax = sns.distplot(a=db['Valor'],bins=100)
ax.figure.set_size_inches(20,5)
ax.set_title('distribuição de preços de imoveis')
ax.set_xlabel('preço em R$')

ax = sns.pairplot(db, x_vars='Valor',y_vars=['Area','Dist_Praia','Dist_Farmacia'],height=5)
ax.fig.suptitle('distribuição entre variaveis')

db['log_Valor']= np.log(db['Valor'])
db['log_Area']= np.log(db['Area'])
db['log_Dist_Praia']= np.log(db['Dist_Praia'] +1)
db['log_Dist_Farmacia']= np.log(db['Dist_Farmacia']+1)



ax = sns.distplot(a=db['log_Valor'],bins=100)
ax.figure.set_size_inches(20,5)
ax.set_title('distribuição de preços de imoveis')
ax.set_xlabel('preço em R$')


ax = sns.pairplot(db, x_vars=['log_Area','log_Dist_Praia','log_Dist_Farmacia'],y_vars='log_Valor',height=5)
ax.fig.suptitle('distribuição entre variaveis')

y = db.log_Valor

X = db[['log_Area','log_Dist_Praia','log_Dist_Farmacia']]

X_train, X_test, y_train,y_test =train_test_split(X,y,test_size =0.2, random_state=2811)


X_train_com_constante = sm.add_constant(X_train)
modelo_statsmodels = sm.OLS(y_train,X_train_com_constante, hasconst=True).fit()
modelo_statsmodels.summary()


X= db[['log_Area','log_Dist_Praia']]
X_train, X_test, y_train,y_test =train_test_split(X,y,test_size =0.2, random_state=2811)
X_train_com_constante = sm.add_constant(X_train)
modelo_statsmodels = sm.OLS(y_train,X_train_com_constante, hasconst=True).fit()
modelo_statsmodels.summary()



modelo = LinearRegression()
modelo.fit(X_train,y_train)
print('r² = {}'.format(modelo.score(X_train,y_train).round(2)))
y_previsto =modelo.predict(X_test)
print('R² = %s' % metrics.r2_score(y_test,y_previsto).round(2))





