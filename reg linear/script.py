# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:28:04 2019

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
#importando as bibliotecas

f = 'C:/Users/adani/Desktop/estudos datas/reg_linar_2/data-science/reg-linear-II/Dados/dataset.csv'
db = pd.read_table(f,sep=';')

db.describe().round(2)
db.corr().round(2)

#olhando as primeiras estatisticas
sns.set_palette('Accent')
sns.set_style('darkgrid')
#setando as caracteristicas dos graficos 


ax = sns.boxplot(data=db['Valor'],orient='h',width=0.3)
ax.figure.set_size_inches(20,5)
ax.set_title('preço dos imoveis')
ax.set_xlabel('reais')
#boxplot com a variavel valor 

ax = sns.distplot(a=db['Valor'],bins=100)
ax.figure.set_size_inches(20,5)
ax.set_title('distribuição de preços de imoveis')
ax.set_xlabel('preço em R$')
#analise de distribuição
#tem uma asimetria a direita

ax = sns.pairplot(db, x_vars='Valor',y_vars=['Area','Dist_Praia','Dist_Farmacia'],height=5)
ax.fig.suptitle('distribuição entre variaveis')
#graficos de disperção entre as variaveis descritiva e a principal 
#e é tudo bisarro, não parecem exitir relaçoes entre os dados 

db['log_Valor']= np.log(db['Valor'])
db['log_Area']= np.log(db['Area'])
db['log_Dist_Praia']= np.log(db['Dist_Praia'] +1)
db['log_Dist_Farmacia']= np.log(db['Dist_Farmacia']+1)
#fazer o log dos dados ajuda voce a trazer os dados para a distribuição normal 

ax = sns.distplot(a=db['log_Valor'],bins=100)
ax.figure.set_size_inches(20,5)
ax.set_title('distribuição de preços de imoveis')
ax.set_xlabel('preço em R$')
# a pos a transformação da para ver que melhorou bastante o efeito de assimetria 

ax = sns.pairplot(db, x_vars=['log_Area','log_Dist_Praia','log_Dist_Farmacia'],y_vars='log_Valor',height=5)
ax.fig.suptitle('distribuição entre variaveis')
# ploto de novo os graficos de dispreção. 
# com essa transformação da para ver bem melhor a corelação entre as variaveis 

#vamos começar o modelo
y = db.log_Valor

X = db[['log_Area','log_Dist_Praia','log_Dist_Farmacia']]
#separa as variaveis explicativas, da variavel dependente)
X_train, X_test, y_train,y_test =train_test_split(X,y,test_size =0.2, random_state=2811)
#divide em variaveis de trino e de teste 

# nova bibloteca stats model 

X_train_com_constante = sm.add_constant(X_train)
# para eu conseguir montar o modelo nessa biblioteca, eu preciso criar uma coluna 
#constante 

modelo_statsmodels = sm.OLS(y_train,X_train_com_constante, hasconst=True).fit()
#agora eu estimo o modelo e tenho que avisar que tem constante 
modelo_statsmodels.summary()
#isso me da um sumerio das estatistica do modelo 
# o que eu preciso prestar atenção 
# R² = tem que estar mais proximo do 1 
#R² ajustado = tem que estar mais proximo do 1, mas tem que olhar a diferença entre ele 
#e o R² quando eu comparar modelos 
# prob(F-statistic) se estiver acima de 0.05 o modelo não é estatisticamente representativo
# estatisticas de cada variavel 
# P>|t| é a mesma coisa de prob(F-statistic) ou seja maior que 0.05 não faz sentido no modelo 
# no caso da para ver que a variavel log_Dist_Farmacia não serve para o modelo 
#pq tem o P>|t|> 0,05
X= db[['log_Area','log_Dist_Praia']]
X_train, X_test, y_train,y_test =train_test_split(X,y,test_size =0.2, random_state=2811)
X_train_com_constante = sm.add_constant(X_train)
modelo_statsmodels = sm.OLS(y_train,X_train_com_constante, hasconst=True).fit()
modelo_statsmodels.summary()
#como o a variavel não tinha siginificancia a gente tira ela do modelo 
#ai fazemos o mesmo processo. 
# no caso podemos ver que não teve alteração do r² 
#então o modelo continua ok 

#daqui para frente é o mesmo processo da criação do modelo 
modelo = LinearRegression()
modelo.fit(X_train,y_train)
print('r² = {}'.format(modelo.score(X_train,y_train).round(2)))
y_previsto =modelo.predict(X_test)
print('R² = %s' % metrics.r2_score(y_test,y_previsto).round(2))

#montar o sistema para o imput dos dados 
entrada = X_test[0:1]
modelo.predict(entrada)[0]
# ok temos um problema. 
#minhas variaveis estão transformadas, ou seja minha previsão tambem vai estar
#temos que resolver isso 
np.exp(modelo.predict(entrada)[0])
# ou seja, tenho que faser a exponencial da previsão

area = 250 
dist_praia = 1

entrada = [[np.log(area),np.log(dist_praia+1)]]
print('R$ {}'.format(np.exp(modelo.predict(entrada).round(2)[0])))
# agora vamos entender as variveis mais a fundo 

#intercepto
np.exp(modelo.intercept_)

#coeficientes das variaveis 
pd.DataFrame(data = np.append(modelo.intercept_,modelo.coef_),index = index, columns= ['parametros '])
# lembrando, os coeficeientes representam o quanto uma variação de 1% no parametro considerando que as outras variaveis são estaticas.
#qual é o impacto disso na variavel que eu quero prever 

y_previsto_train = modelo.predict(x_train)
#faço o modelo prever usando o x de traino

ax = sns.scatterplot(x=y_previsto_train,y=y_train)
ax.figure.set_size_inches(12,6)
ax.set_title('real X previsto')
ax.set_xlabel('log do preço - previsão')
ax.set_ylabel('log do preço - real')

#faço a verificação da disperção dos dados 

resido = y_train - y_previsto_train
ax = sns.distplot(resido)
#olho poara o resido, ele tem que ter um comportamento normal