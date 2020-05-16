# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:11:49 2020

@author: adani
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#folhas de estil do sns 
#posso alterar o estilo do grafico do pandas uzando as folhas de estilo do sns 
plt.style.use('ggplot')
plt.style.use('dark_background')



%matplotlib inline

p1 = 'C:/Users/adani/Desktop/estudo_data/3.Python_para_Visualizacao_de_dados/Visualizacao_de_dados_incorporada_do_Pandas/df1.csv'

p2 = 'C:/Users/adani/Desktop/estudo_data/3.Python_para_Visualizacao_de_dados/Visualizacao_de_dados_incorporada_do_Pandas/df2.csv'

p3 = 'C:/Users/adani/Desktop/estudo_data/3.Python_para_Visualizacao_de_dados/Visualizacao_de_dados_incorporada_do_Pandas/df3.csv'

df1= pd.read_csv(p1,index_col = 0 )
df2= pd.read_csv(p2,index_col = 0 )

#criando histogramas 
df1['A'].hist()

#area
df2.plot.area()

#barras
df2.plot.bar()

#barras empilhadas 
df2.plot.bar(stacked=True)


#histogramas a partir do plot 
df1['A'].plot.hist(bins=50)

#grafico de linhas, tenho que passar o x e o y 
df1.plot.line(x='A',y='B')

#scater plot 
df1.plot.scatter(x='A',y='B')


#no scater posso usar o argumento c para colorir os pontos conforme uma outra variavel 
df1.plot.scatter(x='A',y='B',c='C')
#troca a paleta pelo cmap
df1.plot.scatter(x='A',y='B',c='C',cmap='inferno')

#parametro s muda o tamanho dos ponto 
df1.plot.scatter(x='A',y='B',s=df1['C'])

#boxplot
df2.plot.box()


 df = pd.DataFrame(np.random.rand(1000,2),columns=['a','b'])
 
#plot exagonal 
df.plot.hexbin(x='a',y='b')

#posso alterar o tamenho e a plate
df.plot.hexbin(x='a',y='b',gridsize=20,cmap='inferno')


#kde
df2['b'].plot.kde()











