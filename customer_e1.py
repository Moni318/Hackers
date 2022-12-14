# -*- coding: utf-8 -*-
"""Customer_E1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v8zOyb0gzDHB8pK6v3Da25Lk349ramXo
"""

import pandas as pd
df=pd.read_excel("Cust.xlsx")

df.head()

import matplotlib.pyplot as plt

df.isnull().sum()

df.dropna(how="all",inplace=True)

df.dropna(how="any",inplace=True)

df.isnull().sum()

df.describe()

df2=df.groupby("RFCClientes").sum()
df2.shape

df2.isnull().sum()

fig=plt.figure(figsize=(15,15),dpi=50)

plt.barh(df.RFCClientes,df.ISRDISCOUNT)
plt.yticks(rotation=360)
plt.xlabel("ISR")
plt.ylabel("RFC clientes")
plt.show()

import seaborn as sns
sns.boxplot(x=df2["REGIME"])

import seaborn as sns
sns.boxplot(x=df2["XMLCOUNT"])

sns.histplot(data=df2, x="ISRDISCOUNT")

df.describe()

df.columns

df3=df[['CUSTOMERID', 'ISRDISCOUNT','REGIME', 'XMLCOUNT', 'ZIPCODE']]

sns.heatmap(df3)

"""¿Hay alguna variable que no aporta información?

Si todas las variables que son ID tal como currency branch id y company id ya que todas tienen un valor y se supone que deben ser numeros diferentes.

Si tuvieras que eliminar variables, ¿cuáles quitarías y por qué?
Las de id y currency porque no nos aporta nada en temas estadisticos o financiero para el cliente.

¿Existen variables que tengan datos extraños?
La de regime y XMLCOUNT como se puede onservar en la caja de bigote tiene un valor atipico

Si comparas las variables, ¿todas están en rangos similares? ¿Crees que esto afecte?

No, no afecta porque son diferente valores que no se relaciona nada y tienen el mismo numero de registro

¿Puedes encontrar grupos qué se parezcan? ¿Qué grupos son estos?

Ninguna
"""