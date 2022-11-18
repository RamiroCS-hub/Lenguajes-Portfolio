import pandas as pd
from matplotlib import pyplot as plt

dataF = pd.read_csv("Python\Data Analytics\dataset_viajes_sube.csv")

# print(data["CANTIDAD"].describe())

"""Me fijo la cantidad de nulos que hay"""
# print(data.isnull().sum())

"""Elimino todas las filas que tengan nulo en la columna CANTIDAD"""
dataF = dataF.dropna(subset="CANTIDAD")

# table = pd.concat([dataF[x],dataF[y]], axis=1)
# print(table.head())
# print(data.isnull().sum())
""""Hago un nevo dataset con cada transporte"""
colectivos = dataF.loc[dataF["TIPO_TRANSPORTE"] == "Colectivo"]
sutes = dataF.loc[dataF["TIPO_TRANSPORTE"] == "Subte"]
trenes = dataF.loc[dataF["TIPO_TRANSPORTE"] == "Tren"]

"""Sumo la cantidad de cada transporte"""
cantC = colectivos["CANTIDAD"].sum()
cantS = sutes["CANTIDAD"].sum()
cantT = trenes["CANTIDAD"].sum()

"""
cantC,cantS,cantT = 0,0,0
for i in dataF.values:
    if i[0] == "Colectivo":
        cantC += i[-1]
    elif i[0] == "Subte":
        cantS += i[-1]
    else:
        cantT += i[-1]
"""

data = pd.DataFrame([cantC,cantS,cantT],index=("CANT.COLECTIVOS","CANT.SUBTES","CANT.TRENES"))
total = data.sum(axis=1)
plt.bar(total.index,total)
plt.show()





