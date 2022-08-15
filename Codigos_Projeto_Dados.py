#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## EXTRAÇÃO, TRATAMENTO E LIMPEZA DOS DADOS (ETL)

import pandas as pd
dfmontadora = pd.read_csv('Montadora.csv',sep=';')
dfmontadora2 = pd.read_csv('Montadora2.csv',sep=';')


# In[2]:


## DF montadora

dfmontadora


# In[3]:


## DF montadora2

dfmontadora2


# In[4]:


## Renomeando as colunas MONTADORA 

dfmontadora.columns = ["Data","Modelo","Montadora","Valor","Vendedor","ID","Cor"]


# In[5]:


## Resultado

dfmontadora.head()


# In[6]:


## Renomeando as colunas MONTADORA 2

dfmontadora2.columns = ["Data","ID","Modelo","Montadora","Cor","Valor","Vendedor"]


# In[7]:


## Resultado

dfmontadora2.head()


# In[8]:


## Alterando a ordem das colunas MONTADORA

dfmontadora = dfmontadora[['ID','Data', 'Modelo' , 'Montadora' , 'Cor' , 'Valor' , 'Vendedor']]


# In[9]:


## Resultado

dfmontadora.head()


# In[10]:


## Alterando a ordem das colunas MONTADORA2

dfmontadora2 = dfmontadora2[['ID','Data', 'Modelo' , 'Montadora' , 'Cor' , 'Valor' , 'Vendedor']]


# In[11]:


## Resultado

dfmontadora2.head()


# In[12]:


## Verificando Dados Nulos - dfmontadora

dfmontadora.isnull().sum()


# In[13]:


## Verificando Dados Nulos - dfmontadora2

dfmontadora2.isnull().sum()


# In[14]:


# Poderia substituir os dados nulos por erro Sistemico ou qualquer outra informação dependendo da regra do Negocio. 

## dfmontadora2['Data'].fillna("Erro_sistemico", inplace=True) ##


# In[15]:


# dados duplicados - dfmontadora

dfmontadora[dfmontadora.duplicated()] 


# In[16]:


# dados duplicados - dfmontadora2

dfmontadora2[dfmontadora2.duplicated()] 


# In[17]:


#dados duplicados, buscamos pela ID - dfmontadora2

dfmontadora2[dfmontadora2.duplicated(['ID'],keep=False)]


# In[18]:


## Substituindo "." por "/" na data, (dfmontadora)

#dfmontadora['Data'] = dfmontadora['Data'].apply(lambda x: str(x).replace(".","/"))


# In[19]:


## Resultado

dfmontadora


# In[20]:


## Substituindo "." por "/" na data, (dfmontadora)

#dfmontadora2['Data'] = dfmontadora['Data'].apply(lambda x: str(x).replace(".","/"))


# In[21]:


## Resultado

dfmontadora2


# In[22]:


dfmontadora.info()


# In[23]:


dfmontadora2.info()


# In[24]:


## Filtro por ID dados Duplicados 

dfmontadora2[dfmontadora2.duplicated(['ID'],keep=False)]


# In[25]:


# excluimos o segundo registro pelo criterio Data e mantem o Primeiro registro.

dfmontadora2.drop_duplicates(subset="ID", keep='first',inplace=True)


# In[26]:


## Consulta dados nulos

dfmontadora.isnull().sum()


# In[27]:


# Consulta dados nulos

dfmontadora2.isnull().sum()


# In[28]:


# Poderia substituir os dados nulos por erro Sistemico ou qualquer outra informação dependendo da regra do Negocio. 

## dfmontadora2['Data'].fillna("Erro_sistemico", inplace=True) ##


# In[29]:


## Excluindo Dados nulos Montadora2 - optei por excluir devido ser linhas em Branco

dfmontadora2 = dfmontadora2.dropna()


# In[30]:


dfmontadora2.isnull().sum()


# In[31]:


dfmontadora2.info()


# In[32]:


dfmontadora2


# In[33]:


dfmontadora


# In[36]:


## Unindo dfmontadora e dfmontadora2 através do concat

dfmontadoras = pd.concat([dfmontadora, dfmontadora2], ignore_index=True)


# In[37]:


dfmontadoras


# In[40]:


dfmontadoras['Data'] = dfmontadoras['Data'].apply(lambda x: str(x).replace(".","/"))


# In[41]:


dfmontadoras


# In[42]:


dfmontadoras.info()


# In[43]:


## Alterando o tipo dos dados

dfmontadoras['ID'] = dfmontadoras['ID'].astype('int64')
dfmontadoras['Valor'] = dfmontadoras['Valor'].astype('int64')


# In[44]:


dfmontadoras.info()


# In[45]:


## Resultado

dfmontadoras


# In[47]:


## Exportando para CSV/Excel

dfmontadoras.to_csv('Montadoras.csv')
dfmontadoras.to_excel('Montadoras.xlsx')


# In[ ]:




