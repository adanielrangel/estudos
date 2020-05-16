# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:05:14 2020

@author: adani
"""

# dentro de um dicionario eu acesso a os valores do mesmo jeito que eu aceso uma coluna no pandas. 
#nome_do_dicionario['nome_da_chave']

dic = {'valor_1' : 1, 
       'valor_2' : 2
       }

dic['valor_1'] 

#posso passar uma lista tambem dentro desse dicionario 

dic = {'lista' :[1,2,3,4],
        'valor': 1
       }
#ai eu acesso a lista da mesma forma e o valor 
#da lista do mesmo jeito que uma lista normal 

dic['lista'][0]

#tuplas 
#diferença entre a tupla e a lista é que a lista é imutavel 
# acesso os valoere da mesma forma 

t = (1,2,3)

t[0]

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

for i in range(0,100):
    print(i)
    
def f1(parametro):
    x = parametro**2
    return x 

seq = [1,2,3,4,5]

# map roda uma função para todos os valores de um iteravel
#passa a função depois passa o iteravel

map(f1,seq)

list(map(f1,seq))

#filter é uma funço que se eu passar um lambda para ele
# ele filtra uma lista com os valores que eu preciso 

list(filter(lambda item:item%2==0,seq))


