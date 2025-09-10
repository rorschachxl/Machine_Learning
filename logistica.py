# 📧 Clasificación de Correos con Regresión Logística

Este proyecto implementa un modelo de **Machine Learning** para clasificar correos electrónicos en **spam/no spam (o categorías similares)** utilizando **Regresión Logística**.  

El flujo del proyecto incluye:  
1. Carga del dataset.  
2. Selección de variables (contenido del correo y su etiqueta).  
3. División en entrenamiento y prueba.  
4. Vectorización de texto con **TF-IDF**.  
5. Escalado de datos.  
6. Entrenamiento del modelo de **Regresión Logística**.  
7. Predicciones sobre los datos de prueba.  
8. Evaluación mediante **matriz de confusión** y porcentaje de acierto.  

---

##  1. Carga del dataset
Se importa el dataset `correos_dataset.csv` usando **Pandas**.  
De este dataset se seleccionan:  
- **Columna 6** → Contenido del correo (texto).  
- **Columna 9** → Etiqueta (clase a predecir, por ejemplo *spam* o *no spam*).  

---

##  2. División de los datos
Se utiliza `train_test_split` de **Scikit-learn** para dividir los datos en:  
- **70% entrenamiento**  
- **30% prueba**  

Esto permite entrenar el modelo en un subconjunto y luego evaluarlo en datos que nunca ha visto.

---

##  3. Vectorización de texto
El contenido de los correos (texto) se transforma en vectores numéricos usando **TF-IDF (Term Frequency – Inverse Document Frequency)**.  
Esto asigna un peso a cada palabra según su importancia en el documento y en el corpus.

---

##  4. Escalado de datos
Se aplica un **StandardScaler** (con `with_mean=False` ya que los datos son dispersos).  
El escalado ayuda a normalizar los valores numéricos para que el modelo entrene de manera más estable.

---

##  5. Entrenamiento del modelo
Se entrena un modelo de **Regresión Logística**, que es un algoritmo supervisado muy utilizado en clasificación binaria.  
Este modelo aprende a distinguir entre las etiquetas (ejemplo: *spam* vs *no spam*) en función de las palabras presentes en el correo.

---

##  6. Predicción
El modelo predice las etiquetas de los datos de prueba (X_test).  
Se muestran:  
- **Predicciones del modelo** (clases asignadas).  
- **Etiquetas reales** (valor verdadero del dataset).

---

##  7. Evaluación del modelo
La calidad del modelo se mide con:  
- **Matriz de confusión**: muestra cuántos correos fueron clasificados correctamente y cuántos se confundieron.  
- **Porcentaje de acierto (accuracy)**: mide el rendimiento global del modelo.  

En el ejemplo, el cálculo de accuracy fue hecho sumando los verdaderos positivos y verdaderos negativos y dividiéndolos entre el total de muestras.

---

## Conclusiones
- Se logró entrenar un modelo de clasificación de correos basado en texto usando **Regresión Logística**.  
- El uso de **TF-IDF** permitió convertir el texto en características numéricas relevantes.  
- La evaluación con matriz de confusión y accuracy mostró el rendimiento del modelo.  

---

## 🚀 Requisitos
- Python  
- Pandas  
- Numpy  
- Scikit-learn  

---

## Ejecución
1. Clonar el repositorio o descargar el script.  
2. Asegurarse de tener el archivo `correos_dataset.csv` en el mismo directorio.  
3. Instalar dependencias:  
   ```bash
   pip install pandas numpy scikit-learn
