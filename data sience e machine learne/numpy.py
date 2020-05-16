# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 10:11:29 2020

@author: adani
"""

import numpy as np

minhas_lista = [1,2,3]

#converte a lista em array 
np.array(minhas_lista)

#poddo criar arrays multi dimenncionais, é só passar uma lista de listas 
minha_matris = [[1,2,3],[4,5,6],[7,8,9]]

np.array(minha_matris)

# cria um array e prenche ele com uma sequencia a partit do valor inicia até o valor final-1
np.arange(0,10)

# cria um arrey com valores 0  e passo o numero de valores dessa arrey 
np.zeros(3)

# se eu passar uma tupla, com 2 dimençoes ele cria uma matris com essas dimençoes 

np.zeros((5,5))

#posso usar o metodo ines para criar uma matris com 1 
np.ones((3,3))

#posso criar uma matris com 1 em suas diagonais usando o metdo eye
np.eye(4)

# com o metodo linspace eu posso pegar umeros em uma sequencia que estejam igualmente espaçados 

np.linspace(0,10,2)

#np.reandom 'sub lib ' que tras metodos aleatorios 
#o metodo rand puxa um numero que voce passar de valores aleatorios 
#que tem a mesma probabilidade de serem escolhidos 
np.random.rand(5)

# posso multiplicar o resultado por 10 e vou ter um 
#numero aleatorio de 0 a 10 
np.random.rand(5) * 10

#se eu passar 2 valor ele cria uma matris bidimencional 
np.random.rand(5,2) * 10

#vale lembrar a ordem dos numeros é a ordem das matrises.
#ou seja, nesse caso estou criando 2 listas que contem 2 listas que contem 5 valores aleatorios 
np.random.rand(2,2,5) * 10

#o metodo randn puxa valores aleatorios com uma distribuição nomal 
 # media 0 de desvipad 1 

np.random.randn(2)


# o randint me permite criar uma distribuição aleatoria onde cada numero 
#tem a mesma chance de aparecer
#passo valor inical, valor final , numero de valores 
 
np.random.randint(0,100,10)

# posso crair o mesmo efeito usando o rand mas ai eu tenho que aredondar o valor 

np.round(np.random.rand(5)*10,0) 


#atrubutos e metodos do np 

#rashape 

#array de 25 valores 
arr = np.random.rand(25)

#posso transformar ele em uma matris de 5,5 

arr =arr.reshape((5,5)) 

#puxando o maior valor
arr.max() 

#puxando menor valor
arr.min()

#puxando a posição do maior valor 
arr.argmax()


#indexacao 


arr = np.arange(0,30,3)

#posso puxar o valor de um array do mesmo 
#jeito que eu puxo de um alista

arr[3]

#posso puxar uma parte dos elementos
#passando a posiçaõ iniciarl dos elementos que eu quero e a posição final +1 (pq ele não puxa o oultimo valor )

arr[2:5]

# puxa tudo até o indice 5 não inclusivo
arr[:5]

# puxa tudo a partir do indice 3 inclusivo
arr[3:]

#posso operar os valor do mesmo jeito 

arr[2:] = 100


#procurando coisas em array bidimencional 

arr = np.arange(50).reshape(5,10)

#posso usar 2 colchetes
arr[:3][:]

#posso usar um colchete só separando os dados por prigula
arr[1:4,5:]

#se eu croar uma variavel que é uma referencia a outro arrey 
#e eu alterar esse array , ele altera o orifinal
arr2 = arr[:3]

#se eu passar o .copy() ele gera uma copia e não altera o arrey base

arr2 = arr[:3].copy()


# oprando com array 

# se eu passar alguma regra (operador logico) 
#para um arry ele me retorna um array com valores 
#boliando modtrando onde a regra é aplicavel 
bol = arr >20 

# passo esse arrey poara como filtro 
arr[bol]



# operação com np 

arr = np.arange(0,16)


# quando eu vou operar um arry ele compara cada 
#elemento com o elemento de mesmo index no segundo arrey
arr + arr

#quando eu mando np realizar alguma operação que não fas 
#sentido ele não me da um erro, ele me da um aviso e coloca nan como resultado 
#ou retona infinito quando fizer sentido 
arr/arr

# o mesmo é valido quando eu vou fazer a soma de um valor unico 
arr +100













