# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:26:05 2019

@author: adani
"""
import pickle


modelo = open('C:/Users/adani/Desktop/estudos datas/reg-linear/modelo_consumo_cerveja','rb')
lm_new = pickle.load(modelo)
temp_max = -50
chuva = 0
fds = 0
entrada = [[temp_max,chuva,fds]]


print('{0:.2f} litros '.format(lm_new.predict(entrada)[0]))

