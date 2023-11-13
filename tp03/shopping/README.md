# Proyecto Shopping

## Descripción

El proyecto Shopping es un script de Python que utiliza el algoritmo de K-Nearest Neighbors (KNN) para predecir si un usuario realizará una compra en un sitio web en función de varias características.

La consigna de este trabajo se encuentra en el archivo [Consigna](../tp3-u5.pdf), los requerimientos para ejecutar el proyecto en el archivo [requeriments](./requirements.txt).

## Archivos

El proyecto contiene los siguientes archivos:

- `shopping.py`: Este es el archivo principal que contiene el código para cargar los datos, entrenar el modelo y hacer predicciones.

## Librerías

El proyecto utiliza las siguientes librerías:

- `csv`: Esta librería se utiliza para leer y escribir archivos CSV.
- `sys`: Esta librería proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python.
- `sklearn.model_selection`: Este módulo de sklearn se utiliza para dividir los datos en conjuntos de entrenamiento y prueba.
- `sklearn.neighbors`: Este módulo de sklearn se utiliza para implementar el algoritmo K-Nearest Neighbors.

### K-Nearest Neighbors (KNN)

K-Nearest Neighbors es un algoritmo de aprendizaje supervisado que se utiliza para clasificación y regresión. En ambos casos, la entrada consta de los k ejemplos de entrenamiento más cercanos en el espacio de características.

## Ejecución

Para ejecutar el script `shopping.py`, usa el siguiente comando en tu terminal:

```bash
python shopping.py data.csv