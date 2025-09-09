import pandas as pd
import numpy as np

# Impotar el dataset
data=pd.read_csv('correos_dataset.csv')

# Seleccion de features y etiquetas
x=data.iloc[:,6].values #contenido
y=data.iloc[:,9].values #etiqueta

# Separacion de train y test mediante sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=0)

# Vectorizacion del texto mediante sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Escalado de los datos
from sklearn.preprocessing import StandardScaler
standar_x = StandardScaler(with_mean=False)
X_train=standar_x.fit_transform(X_train)
X_test=standar_x.fit_transform(X_test)

# Entrenamiento del modelo
from sklearn.linear_model import LogisticRegression
reg=LogisticRegression(random_state=0)
reg.fit(X_train,y_train)

# Prediccion
pred=reg.predict(X_test)

print("Predicciones del modelo:")
print(pred)
print("\n")
print("Etiquetas reales:")
print(y_test)

# Evaluacion del modelo
# Matriz de confusion
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,pred)
print("Matriz de confusion:")
print(cm)
print("Porcentaje de acierto:")
print((140+137)/len(y_test))
