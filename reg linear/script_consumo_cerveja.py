# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:57:14 2019

@author: adani
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

f = "C:/Users/adani/Desktop/estudos datas/reg-linear/Dados/Consumo_cerveja.csv"

db = pd.read_table(f,sep=";")
db.describe()
db.shape
db.describe().round()
db.corr().round(3)


fig, ax = plt.subplots(figsize =(15 , 6))
ax.set_title('consumo de cerveja', fontsize = 20)
ax.set_ylabel('litros' ,fontsize = 16)
ax.set_xlabel('dias' ,fontsize = 16)
ax = db['consumo'].plot()
#grafico de linha

ax = sns.boxplot(data= db['consumo'],orient= 'v', width= 0.2)
ax.figure.set_size_inches(12,6)
ax.set_ylabel('litros' ,fontsize = 16)
#box plot variavel consumo 

ax = sns.boxplot(y ='consumo', x ='fds', data= db,orient= 'v', width= 0.5)
ax.figure.set_size_inches(12,6)
ax.set_ylabel('litros' ,fontsize = 16)
ax.set_xlabel('final de semana',fontsize = 16)
sns.set_palette('Accent')
sns.set_style('darkgrid')
#box plot vareavel consumo considerando a variavel FDS

ax = sns.distplot(db['consumo'])
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuiçao de frequancia', fontsize = 20)
ax.set_ylabel('consumo de cerveja (litros)' ,fontsize = 16)
#olhar a distribuição da variavel consumo de cereveja 

ax = sns.pairplot(db)
#ele gera varios graficos scater plot mostrand as relaçoes entre os dadsos 

ax = sns.pairplot(db, y_vars='consumo', x_vars=['data','temp_media','temp_min','temp_max','chuva','fds'])
ax.fig.suptitle('disperção entre variaveis')
#vamos olhar somente para os graficos em relação a consumo 

ax = sns.jointplot(x='temp_max',y='consumo',data= db)
ax.fig.suptitle('disperção entre variaveis')
#cria um grafico de disperção que mostra a distribuição fa variavel em cima 
ax = sns.jointplot(x='temp_max',y='consumo',data= db, kind="reg")
#se eu passar a variavel kind = reg ele mostra o grafico com a linha de tendencia 

ax = sns.jointplot(x='temp_max',y='consumo',data= db, kind="kde")
#se eu passar kede ele mostra um heet map da distribuição dos pontos 
ax = sns.jointplot(x='temp_max',y='consumo',data= db, kind="hex")
# hex fas o het map com exagonos, fica muito bom 

ax = sns.lmplot(x='temp_max',y='consumo', data= db)
ax.set_xlabels('temperatura macimas(ºC)')
ax.set_ylabels("consumo de cerveja")
#consigo criar um scater plot para mostrar a corelação 

ax = sns.lmplot(x='temp_max',y='consumo', data= db,hue ='fds', markers= ['o', '*'],legend=False)
ax.set_xlabels('temperatura macimas(ºC)')
ax.set_ylabels("consumo de cerveja")
ax.add_legend(title='Fim de semana')
#com o parametro hue eu posso pasr uma outra variavel do meu db, ai eu consigo enternder esse escater a partir de uma outra variavel 

ax = sns.lmplot(x='temp_max',y='consumo', data= db,col= 'fds',legend=False,)
ax.set_xlabels('temperatura macimas(ºC)')
ax.set_ylabels("consumo de cerveja")
ax.add_legend(title='Fim de semana')
# se eu passar a variavel col en ves de hue ele quebra em graficos diferentes, talves seja muito util para mostrar as corelaçoes quando eu tenho uma terceira variavel com varios valores

#ok agora a coisa fica ceria 
#vamos comesara usar a train_test_split que é uma finção que é usada para criar dados para treino de mashine learning
y =db['consumo']
#primeiro criamos uma variavel lista que contem nosa variavel  dependente 'consumo' 
X = db[['temp_max','chuva','fds']]
# e um df com as nossas variaveis explicativas

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2811)
# ele vai retornar 4 variaveis 
# eu desempacoto e crio 4 variaveis X_train, X_test, y_train, y_test
#agora vamos entender os criterios da função 
# X e y são o dataset que eu quero dividir 
#test_size=0.3 qual é o percentual da base que eu vou usar para teste 
#random_state=42 tem a mesma função da seed 

modelo = LinearRegression()
# primero eu crio uma variavel chamada modelo e passo a função LinearRegression()
#isso vai me permitir aplicar um metodo a esse modelo 
modelo.fit(X_train,y_train)
#passo o metodo .fit com as variavesi de treino, e isso me gera o modelo 

print('R²={}'.format(modelo.score(X_train,y_train).round(2)))
#agora vamos caucular o R². ou seja o quanto o modelo se adequa aos dados 
# ele retorna um valor de 0 a 1, quanto mais perto de 1 melhor 
 
y_previsto = modelo.predict(X_test)
#agora eu passo os meus dados de teste 
# se eu quero montar uma previsão eu tenho que passar só os as variaveis preditivas 
# isso me gera uma series de previsões 

print('R² = %s' % metrics.r2_score(y_test,y_previsto).round(2))
#ta mas como eu sei se elas são boas ? 
# eu tenho que comparar as previsoes com o modelo
# por isso eu passo o metrics e crio um R² com os 2 

entrada = X_test[0:1]
#vamos tentar prever alguma coisa 
#eu crio uma variavel chamada entrada e puxo a primeira linha do meu db de teste. 
# ou seja para fazer o imput para a previsão eu tenho que usar o mesmo padrão de veriavel da X_teste
modelo.predict(entrada)
#essa função me gera uma predição, no caso um aray com 1 obj [26094.90177526]

temp_max = 30.5
chuva = 12.2
fds = 0
entrada = [[temp_max, chuva, fds]]
#posso fazer essa brincadeira para o imput dos dados, seto 3 variaveis cada uma com uma das minhas variaveis esplicativas 
#crio uma variavel usando ela as 3 outras que eu criei
print("{0:.2f} litros".format(modelo.predict(entrada)))
 #aplico o modelo com o .predict e printo ele 

#Yi = b1+b2*X2i+b3*X3i+b4*X4i+Ui
#vamos entender essa formula 
#Yi e a variavel dependente, no caso consumo de cerveja 
#b1 intercepto, ou seja o consumo mdio sem considerar as outras variavei 
#b. os outros b sã os coeficientes de regreção, o quanto uma alteração de 1 em uma varivel 
#altera no resultado da variavel dependente
#X.i as variaveis explicativas
# Ui é o termo de erro, o que o modelo não consegue explica 
# é assim que o modelo funciona 
 
#vamos olhar para o intercepto
modelo.intercept_
#5951.976339312445
#consguindo os b
modelo.coef_
#array([ 684.73675898,  -60.7824355 , 5401.08333866])
 
#vamo printar essa porra de um jeito bunitinho  
index = ['intercepto', ' temperatura maxima', 'chuva', ' final de semana']
#crio um index com o nome das variaveis mais o intercepto (na ordem que elas aparecem no modelo )
#na duvida usa o X.columns
pd.DataFrame(data= np.append(modelo.intercept_, modelo.coef_),index= index, columns=['parametros'])
#crio um dataframe na parte de data eu passo as funçoes para consequir os coeficentes e o intercepto 
#passo o index com as colunas 
#e para dar um nome buinitinho passo o colons com parametros, não esquece que o coluns tm que ser um arey 

y_previsto_train = modelo.predict(X_train)
#vamos voltar nos dados de treino, fazendo previsoes neles, para ver se as previsoes do modelo batem com os dados. 

ax = sns.scatterplot(x= y_previsto_train, y= y_train)
ax.figure.set_size_inches(12,6)
ax.set_title('previsão x real')
ax.set_xlabel('consumo de cerveja em litros - previsão')
ax.set_ylabel('consumo de cerveja em litros - real')
# eu faço um grafico para ver se as previsoes batem com o real 
# nesse caso não ta ideal, pois ela deveria bater com a linha de tendencia, mas eles estão meio disperços

resido = y_train - y_previsto_train
# chegamos na ultima parte da formula, 
#o resido é a diferença entre os dados reais e sua previsão 

ax = sns.scatterplot(x= y_previsto_train, y=resido, s=150)
ax.figure.set_size_inches(20,8)
ax.set_title('resido X previsão')
ax.set_xlabel('consumo de cerveja (litros)- previsão')
ax.set_ylabel('resido')
#iso me cria um grafico de dispeção entre a previsão e o resido 
# o ideal ´que o resido fique sempre dentro de um intervalo 
#ou seja, que ele forme tipo um tubo e não um cone 

ax = sns.scatterplot(x= y_previsto_train, y=resido**2, s=150)
ax.figure.set_size_inches(20,8)
ax.set_title('resido X previsão')
ax.set_xlabel('consumo de cerveja (litros)- previsão')
ax.set_ylabel('resido')
# se eu elavar os residos ao ² eu passo tosos os dados para o positivo, assim fica mais facil de ver 

# hetericedacidade seguinifica os dados estrem entre intervalos constantes 
# se ele não tiver isso representa um problema no nosso modelo 

ax = sns.distplot(resido) 

# outra forma de olhar para os residos é entender a ditribuição deles. 
# o ideal seria a distribuição normal 
ax = sns.distplot(resido, bins= 50)
# se eu passar o criterio bins eu tenho um maior numero de barras. 
 
X2 = db[['temp_media','chuva','fds']]
X2_train, X2_test, y2_train,y2_test = train_test_split( X2 , y, test_size=0.3,random_state=2811)
#ok agora vamos comparar os testes. 
#crio um novo X e refaço o trainamento considerando a variavel temp_media, para ver se o resultado é melhor
modelo_2 = LinearRegression()
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
#criando o modelo 2 
print('modelo com temp. max')
print('R² = {}'.format(modelo.score(X_train,y_train).round(2)))

print('modelo com temp. med')
print('R² = {}'.format(modelo_2.score(X2_train,y2_train).round(2)))
#fiz o medoelo 2 e agora eu vou comparar o R² 2 variaveis. 

y_previsto = modelo.predict(X_test)
y2_previsto = modelo_2.predict(X2_test)

print('modelo com temp. max')
print('R² = {}'.format(metrics.r2_score(y_test,y_previsto)))

print('modelo com temp. med')
print('R² = {}'.format(metrics.r2_score(y2_test,y2_previsto)))
# outra forma de comparar o r². 

#outra forma de se comparar modelos é com o erro qudretico medio. 
#ou seja a media do resido ao quadrado
# ou a reis da media do resido ao quadredo 

eqm_2 = metrics.mean_squared_error(y2_test,y2_previsto).round(2)
reqm_2 = np.sqrt(metrics.mean_squared_error(y2_test,y2_previsto)).round(2)
r2_2 = metrics.r2_score(y2_test,y2_previsto).round(2)

modelo_2 = pd.DataFrame([eqm_2,reqm_2,r2_2],['eqm','reqm','r²'],columns=['metricas'])


eqm_1 = metrics.mean_squared_error(y_test,y_previsto).round(2)
reqm_1 = np.sqrt(metrics.mean_squared_error(y_test,y_previsto)).round(2)
r2_1 = metrics.r2_score(y_test,y_previsto).round(2)

modelo_1 = pd.DataFrame([eqm_1,reqm_1,r2_1],['eqm','reqm','r²'],columns=['metricas'])

#faz os cauculos do erro quadrtico medio e da sua raiz (eqm , reqm) e do R² 
#coloca num DF so para ficar visual 
# lembrendo que o EQM e REQM tem que ser mais proximo de 0, quanto menor melhor. 
# e o R² quanto maior melhor 


output = open('modelo_consumo_cerveja','wb')

pickle.dump(modelo, output)

output.close()

#definimos qual é o melhor modelo, agora temos que salvar essa binboca. 
#tenho que chamar a biblioteca pickle
# abro um arquivo e uso o dump para gravar ele 
#ai fecha o arquivo 


