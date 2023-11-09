# TP04 - Señales de trafico

## Descripción

La consigna de este trabajo se encuentra en el archivo [Consigna](./tp4-u6-u7.pdf), los requerimientos para ejecutar el proyecto en el archivo [requeriments](./traffic/requeriments.txt),
y la presentacion en el archivo [Presentacion](./presentacion-trafico.pdf).

## Problema vs Solucion
Problema - Mientras la investigación avanza en el desarrollo de coches autónomos, uno de los retos clave es la visión por computadora, que permite a estos coches que desarrollen una comprensión de su entorno a partir de imágenes digitales.
Solucion - Utilizaremos TensorFlow para construir una red neuronal que sea capaz de clasificar señales de tráfico basadas en imágenes de dichas señales.

## Dataset
German Traffic Sign Recognition Benchmark.
Este dataset alemán contiene 
+ 40 clases de señales de tráfico.
+ 50.000 imágenes en total.

## Dependencias

- cv2
- numpy
- os
- sys
- tensorflow
- sklearn

## Funcion LoadData
Esta función recibe como parámetro el directorio donde se encuentran las imágenes y devuelve dos listas, una con las imágenes y otra con las etiquetas de salida.
Las etiquetas de salida son los nombres de las carpetas que contienen las imágenes. 
Por ejemplo, si tenemos una imagen de un semáforo, la etiqueta de salida será 0, ya que la imagen se encuentra en la carpeta 0. Si tenemos una imagen de un límite de velocidad de 30 km/h, la etiqueta de salida será 1, ya que la imagen se encuentra en la carpeta 1. Y así sucesivamente.

## Separar los datos de entrenamiento de los de prueba

La funcion de scikit learn train_test_split() nos permite separar los datos de entrenamiento de los de prueba. Esta función recibe como parámetros los datos de entrada y las etiquetas de salida y nos devuelve los datos de entrada de entrenamiento, los datos de entrada de prueba, las etiquetas de salida de entrenamiento y las etiquetas de salida de prueba. 
El parámetro test_size nos permite indicar el porcentaje de datos que queremos que se utilicen para el conjunto de prueba. En este caso hemos indicado que el 40% de los datos se utilicen para el conjunto de prueba, por lo que el 60% de los datos se utilizaran para el conjunto de entrenamiento.

## Funcion GetModel

- keras.Secuential, es una forma de decirle a keras que queremos crear un modelo conformado por una secuencia de capas. 
- Conv2D, capa convolucional de dos dimensiones que prende 32 filtros.
- MaxPooling2D, aplica convolucion, tamaño de pooling 2x2.
- Funcion flattern, convierte la matriz en un arreglo.
- Capa de salida, capa densa, softmax da prediccion porcentual.

Lo primero que tenemos que hacer es compilar nuestro modelo, para así comunicar al backend de TensorFlow que queremos entrenar nuestro modelo con el algoritmo de optimización Adam.

Con el método compile se entrena el modelo.
Loss es función de pérdida.
- binary_crossentropy
    Esta función de pérdida es adecuada para problemas de clasificación binaria, donde cada muestra puede pertenecer a una de las dos clases

- categorical_crossentropy
    Esta es una función de pérdida común para problemas de clasificación multiclase. Es adecuada cuando cada muestra pertenece a exactamente una de las clases y las clases son mutuamente excluyentes

Y la métrica es la precisión (accuracy).

Una vez que tenemos el modelo compilado, tenemos que entrenarlo y esto se consigue llamando al método fit() de nuestro modelo. 
Este método recibe como parametros los datos de entrada de entrenamiento, las etiquetas de salida de entrenamiento y el número de épocas que queremos entrenar nuestro modelo. 
Una época es una pasada completa por todos los datos de entrenamiento.
Por ejemplo, si tenemos 1000 imagenes y un batch size de 10, entonces una epoca consistira en 100 iteraciones, ya que 1000 / 10 = 100. En cada iteracion se procesaran 10 imagenes y se calculara el error cometido por el modelo. Una vez que se han procesado todas las imagenes de entrenamiento, se habra completado una epoca. Normalmente se suele entrenar un modelo durante varias epocas, ya que en cada epoca el modelo va mejorando su precision.

Por ultimo se evalua el modelo, con la funcion evaluate.
El valor de perdida nos indica el error cometido por el modelo. Cuanto menor sea este valor, mejor sera nuestro modelo. 
La precision nos indica la precision del modelo. Cuanto mayor sea este valor, mejor sera nuestro modelo.
Por ejemplo, si el valor de perdida es 0.1 y la precision es 0.9, esto significa que el modelo ha cometido un error del 10% y que ha acertado el 90% de las veces.

