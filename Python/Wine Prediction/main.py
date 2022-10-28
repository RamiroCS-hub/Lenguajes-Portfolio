import pandas as pd
from matplotlib import pyplot as plt
#Importaciones para el entrenamiento del modelo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('wine.csv')

#Separo las caracteristicas de los vinos y el tipo de vino
features = ['Alcohol','Malic_acid','Ash','Alcalinity','Magnesium','Phenols','Flavanoids','Nonflavanoids','Proanthocyanins','Color_intensity','Hue','OD280_315_of_diluted_wines','Proline']
label = "WineVariety"
# X = Valores de propiedades de todos los vinos, Y = Valores de tipos de vino(0,1,2)
X, Y = data[features].values ,data[label].values
# for n in range(0,4):
#     print("Vino:",str(n+1),"Caracteristicas:",list(X[n]),"\nTipo de vino:",Y[n])
# for col in features:
#     data.boxplot(column=col, by=label, figsize=(7,7))
#     plt.title(col)
#     plt.show()

#Separo el 30% de la info para el testing,y 70% para entrenamiento
xTrain,xTest,yTrain,yTest = train_test_split(X,Y, test_size=0.3, random_state=0)

featureColumns = [0,1,2,3,4,5,6]
featureTransformer = Pipeline(steps=[
    ('scaler', StandardScaler())
    ])

preprocessor = ColumnTransformer(
    transformers=[
        ('preprocess', featureTransformer, featureColumns)])

# Crea el pipeline para entrenar
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', LogisticRegression(solver='lbfgs', multi_class='auto'))])

# Entrena el pipeline para que entrene al modelo con una regresión lineal
model = pipeline.fit(xTrain, yTrain)

from sklearn. metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

# Predicciones con los valores de test
predictions = model.predict(xTest)

# Get metrics
print("Exactitud:",accuracy_score(yTest, predictions))
print("Precision:",precision_score(yTest, predictions, average='macro'))
print("Recall:",recall_score(yTest, predictions, average='macro'))

# Grafica en una matriz de confusion
cm = confusion_matrix(yTest, predictions)
classes = ['Variety A','Variety B','Variety C']
#Interpolation sirve para estimar los puntos desconociddos entre 2 conocidos
plt.imshow(cm, interpolation="nearest", cmap=plt.cm.Reds)
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)
plt.title("Matriz de confusion")
plt.xlabel("Variacion predecida")
plt.ylabel("Variacion real")
plt.show()