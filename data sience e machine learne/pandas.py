# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:03:58 2020

@author: adani
"""

import pandas as pd 
import numpy as np 

labels = ['a','b','c']
lista = [10,20,30]
arr = np.array([10,20,30])
d ={'a':10,'b':20,'c':30}

#criando uma siris, tenho que passar os dados e um index 
series = pd.Series(data = lista , index= labels) 

# a mesma coisa pod ser faito com array
pd.Series(data = arr , index= labels)

# calculo com seris

ser1 = pd.Series([1,2,3,4],  index= ['eua','alemanha','urss','japao'])
ser2 = pd.Series([1,2,3,4],  index= ['alemanha','eua','italia','japao'])

#diferente do np.arrey ele opera os valores pelo index 
# ou seja, não importa a posição do valor mais sim o 
#index asociado a ele para o calculo 

#ps: de ele não achar o valor nas duas tabelas ele vai retornar nan 
ser1 +ser2

#_____________________________________________________________________
## dataframes 

#setando uma sead para padronisar com o curço 

np.random.seed(101)

#definindo um df aleatorio 

df =pd.DataFrame(np.random.randn(5,4),index = 'a b c d e'.split(), columns = 'w x y z'.split() )

#pegando uma ou mais coluna do df 
df[['w','z','w']]

#criando uma coluna nova no df 

df['new'] = df['w'] + df['x']

# dropando uma coluna 
#axis = 0  é o index 
# axis = 1 é as colunas 

df = df.drop('new',axis=1, inplace = True)

#localizando por indice (ou seja puxar um valor ou uma linha)

# se eu passar o index + a coluna ele me retorna um valor unico 
df.loc['a','w']

# se eu passar só o index ele me retorna a linha inteira
df.loc['a']

# funciona se eu passar listas tambem 
df.loc[['a','b']]

#posso uzar a linguagem de arreys 
#nesse caso puxando do indice 1 ao 3 e a partir da coluna 2 até o fim 
df.iloc[1:4 , 2:]

#_____________________________________________________________________
##seleção condicional 

# se eu passar algum teste logico ele me retorna um buliano 
bol = df >0 

# se eu passar ele bulian dentro do colchetes ele vai me 
#retornar todos os valoere que forem verdadeiros 
df[bol]

# uzando essa notação ele permite que eu de fato filter um dataframe 

df[df['w']>0]

#posso puxar somente colunas especificas 
df[df['w']>0]['y']

# para fazer um filtro de and
# o & subistitui o and 
#o and só compara valore unicos o & compara serys 

df[(df['w']>0)& (df['y']>0)]

#para fazer um filtro de or 
#eu tenho que usar o | 

df[(df['w']>0)|(df['y']>0)]


# resetando o index 

#vai me dar um index iguar a um do np 
df = df.reset_index()

# redefinindo index 
#crio uma lista com os valores que eu quero 
col = 'rs rj sp am sc'.split()

#defino uma coluna com os valores que eu queria 
df['estado'] = col

df= df.set_index('estado')

#__________________________________________________________________
#index multinivel 

# crio duas listas 
out = ['g1','g1','g1','g2','g2','g2']
inside = [1,2,3,1,2,3]

#monto uma lista com tuplas que juntam as duas listas de cima 
hier_index = list(zip(out,inside))

#crio um index de multinivel 
hier_index = pd.MultiIndex.from_tuples(hier_index)

# crio um df aleatorio e passo com index os index multi nivel 
df = pd.DataFrame(np.random.randn(6,2), index= hier_index, columns = ['a','b'])

# para acessar o primeiro nivel desses index 
df.loc['g1']

# posso uzar o .loc de novo para acessar o segundo 
#dai ele me retorna uma siris 
df.loc['g1'].loc[1]

#posso trocar o nome do index 
df.index.names = ['grupo','numero']

#se eu quiser ir direto no 2 nivel do index 
#posso usar o xs com a vareavel level

df.xs(1,level='numero')


#________________________________________________________________
#tratando nan 

#df.dropna() 
#dropa os valores nulos, mas ele dropa a linha inteira
#posso passar o parametro thresh = x para deteminar um valor minimo de nan 
#que tem que existir numa linha para ele dropar

#df.fillna()
# fillna vai prencher os valores nulos com algum valor que eu decidir 
#df.fillna(values=0) vai subistituir todos os na por 0 ]

#posso subistituir com a lguma formula / calculo 
#df.fillna(values = df['a'].meam()) vai subistituir pela media da coluna  

# posso usar algum metodo tambem
# exemplo method = 'ffil' que puxa o ultimo valor 
#ler documentação para os metodos 
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html


#________________________________________________________________
#group by 

import pandas as pd
# Cria um DataFrame
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Venda':[200,120,340,124,243,350]}

# crio um obj que é um grupo 
grupo = df.groupby('Empresa')

# ai eu posso passar o metodo que eu quero que ele use 
# no caso soma 
grupo.sum()

# posso usar o discribe para mostrar estatisticas sobre aquele modelo 
grupo.describe()

# o output disso é um dataframe ou seja posso usar metodos de df nele
grupo.sum().loc['FB']


















