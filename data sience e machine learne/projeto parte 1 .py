# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:06:14 2020

@author: adani
"""

# importaçoes 
import pandas as pd 

import seaborn as sns



#path 
p = 'C:/Users/adani/Desktop/estudo_data/Python-Data-Science-and-Machine-Learning-Bootcamp/4. Projetos de dados/911.csv'

#caregando o df  
df = pd.read_csv(p)


df.info()
df.describe()
df.head()

#pergunta 1 top 5 csps com ligaçoies 
df['zip'].value_counts().head(5)
#fazendo o grafico bunitinho 
df['zip'].value_counts().head(5).plot.bar()

#pergunta 2 : 5 principais cidades com chamadas 
df['twp'].value_counts().head(5).plot.bar()

#pergunta 3 quantos codigos de titulos unicos existem 
df['title'].nunique()


def get_fpart(lista):
    out = []
    for i in lista :
        values = i.split(': ')
        out.append(values[0])
    return out

df['razao'] = get_fpart(df['title'])
df['razao'].value_counts().plot.bar()

#4 converter em time frame 
    
df['timeStamp']=pd.to_datetime(df['timeStamp'])

#criar colunas hora month e dia da semana 

df['hora']=df['timeStamp'].dt.hour
df['mes']=df['timeStamp'].dt.month
df['dia_semana']=df['timeStamp'].dt.dayofweek
df['data']=df['timeStamp'].dt.date

df[['timeStamp','hora','mes','dia_semana']].head()

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['dia_semana_tra'] = df['dia_semana'].map(dmap)
# plotando essas colunas 
sns.countplot(x='dia_semana_tra',hue='razao',data=df)

sns.countplot(x='mes',hue='razao',data=df)

# faltam os meses 9,10,11
# agrupando meses por mes 
mes_grup = df.groupby(['mes']).count()

# plotando os dados 
mes_grup['lat'].plot.line()

mes_grup = mes_grup.reset_index()

# criando um plot de regreção 
sns.lmplot(x='mes',y='lat',data = mes_grup)


data_grup = df.groupby(['data']).count()
data_grup = data_grup.reset_index()
data_grup.plot.line(x='data',y='lat')



df_ems = df.query('razao=="EMS"')
df_ems = df_ems.groupby(['data']).agg({'data':['count']})
df_ems = df_ems.reset_index()
df_ems.columns = ['data', 'count']
df_ems.plot.line(x='data',y='count')



df_Fire = df.query('razao=="Fire"')
df_Fire = df_Fire.groupby(['data']).agg({'data':['count']})
df_Fire = df_Fire.reset_index()
df_Fire.columns = ['data', 'count']
df_Fire.plot.line(x='data',y='count')


df_Traffic = df.query('razao=="Traffic"')
df_Traffic = df_Traffic.groupby(['data']).agg({'data':['count']})
df_Traffic = df_Traffic.reset_index()
df_Traffic.columns = ['data', 'count']
df_Traffic.plot.line(x='data',y='count')


pivot =pd.pivot_table(df,values= 'lat',index = ['dia_semana_tra'], columns=['hora'], aggfunc= 'count')
sns.heatmap(pivot)
sns.clustermap(pivot)


pivot =pd.pivot_table(df,values= 'lat',index = ['dia_semana_tra'], columns=['mes'], aggfunc= 'count')
sns.heatmap(pivot)
sns.clustermap(pivot)











