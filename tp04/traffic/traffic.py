import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
# NUM_CATEGORIES = 3 # small
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files.
    images, labels = load_data(sys.argv[1])

    labels = tf.keras.utils.to_categorical(labels)
    
    """
    la funcion de scikit learn train_test_split() nos permite separar los datos de entrenamiento de los de prueba. Esta funcion recibe como parametros los datos de entrada y las etiquetas de salida y nos devuelve los datos de entrada de entrenamiento, los datos de entrada de prueba, las etiquetas de salida de entrenamiento y las etiquetas de salida de prueba. El parametro test_size nos permite indicar el porcentaje de datos que queremos que se utilicen para el conjunto de prueba. En este caso hemos indicado que el 40% de los datos se utilicen para el conjunto de prueba, por lo que el 60% de los datos se utilizaran para el conjunto de entrenamiento. 

    """
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # (datos de entrada de training, labels de salida de training, cuantas epocs)
    """
    una vez que tenemos el modelo compilado, tenemos que entrenarlo y esto se consigue llamando al metodo fit() de nuestro modelo. Este metodo recibe como parametros los datos de entrada de entrenamiento, las etiquetas de salida de entrenamiento y el numero de epocas que queremos entrenar nuestro modelo. Una epoca es una pasada completa por todos los datos de entrenamiento. Por ejemplo, si tenemos 1000 imagenes y un batch size de 10, entonces una epoca consistira en 100 iteraciones, ya que 1000 / 10 = 100. En cada iteracion se procesaran 10 imagenes y se calculara el error cometido por el modelo. Una vez que se han procesado todas las imagenes de entrenamiento, se habra completado una epoca. Normalmente se suele entrenar un modelo durante varias epocas, ya que en cada epoca el modelo va mejorando su precision.
    """
    model.fit(x_train, y_train, epochs=EPOCHS) #entrena el modelo

    #evaluamos el modelo 
    # con la funcion evaluate() podemos evaluar el modelo con los datos de prueba. Esta funcion recibe como parametros los datos de entrada de prueba y las etiquetas de salida de prueba. Esta funcion nos devuelve el valor de perdida y la precision del modelo.
    """
    El valor de perdida nos indica el error cometido por el modelo. Cuanto menor sea este valor, mejor sera nuestro modelo. La precision nos indica la precision del modelo. Cuanto mayor sea este valor, mejor sera nuestro modelo.
    Por ejemplo, si el valor de perdida es 0.1 y la precision es 0.9, esto significa que el modelo ha cometido un error del 10% y que ha acertado el 90% de las veces.
    """
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Esta funcion recibe como parametro el directorio donde se encuentran las imagenes y devuelve dos listas, una con las imagenes y otra con las etiquetas de salida. 
    Las etiquetas de salida son los nombres de las carpetas que contienen las imagenes. Por ejemplo, si tenemos una imagen de un semaforo, la etiqueta de salida sera 0, ya que la imagen se encuentra en la carpeta 0. Si tenemos una imagen de un limite de velocidad de 30 km/h, la etiqueta de salida sera 1, ya que la imagen se encuentra en la carpeta 1. Y asi sucesivamente.
    """
    images = []
    labels = []

    for category_dir in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category_dir)
        
        if os.path.isdir(category_path):
            label = int(category_dir)
            
            for image_file in os.listdir(category_path):
                image_path = os.path.join(category_path, image_file)
                
                image = cv2.imread(image_path)
                image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
                
                images.append(image)
                labels.append(label)
    
    return images, labels



def get_model():
    """
    keras.Secuential: es una forma de decirle a keras que queremos crear un modelo conformado por una secuencia de capas. A partir de este momento ya podemos empezar a añadir capas a nuestra red neuronal.
    En este caso las capas fully connected donde cada neurona tiene una conexion con todas las neuronas de la capa anterior son denominadas capas Densas a las cuales se les pasa como parametro la cantidad de neuronas que tendra la capa y la funcion de activacion que se utilizara en cada neurona. 

    Conv2D(capa convolucional de dos dimensiones q prende 32 filtros, kernel de 3x3, activacion relu, dato de entrada)
    a la salida de esta capa
    MaxPooling2D(aplica convolucion, tamaño de pooling 2x2, divide la imagen por 2 el alto y el ancho creo)
    funcion flattern, convierte la matriz en un arreglo
    la paso a una capa oculta tipo densa

    capa de salida, capa densa, softmax da prediccion porcentual
    """
    # ALTERNATIVA 1
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    #     tf.keras.layers.MaxPooling2D((2, 2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation='relu'),
    #     tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')  # Cambia el número de unidades en la capa de salida a 3
    # ])

    # # ALTERNATIVA 2
    # model = tf.keras.models.Sequential([
    #     # Capas de convolución y pooling
    #     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    #     tf.keras.layers.MaxPooling2D((2, 2)),
    #     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    #     tf.keras.layers.MaxPooling2D((2, 2)),
    #     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    #         # Capas totalmente conectadas
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(64, activation='relu'),
    #     tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    # ])

    # ALTERNATIVA 3
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (5, 5), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.3), # va descartando la mitad de las entidades previene el overfiting
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='sigmoid') 
    ])

    # ALTERNATIVA 4
    # model = tf.keras.models.Sequential([
    # tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    # tf.keras.layers.MaxPooling2D((2, 2)),
    # tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(128, activation='relu'),
    # tf.keras.layers.Dense(64, activation='relu'),  # Nueva capa densa oculta
    # tf.keras.layers.Dense(32, activation='relu'),  # Nueva capa densa oculta
    # tf.keras.layers.Dropout(0.3),
    # tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax') 
    # ])
    # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    # ALTERNATIVA 5
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    #     tf.keras.layers.MaxPooling2D((2, 2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation='relu'),
    #     tf.keras.layers.Dense(64, activation='linear'),  # Nueva capa densa ocultav
    #     tf.keras.layers.Dense(64, activation='linear'),  # Nueva capa densa oculta
    #     tf.keras.layers.Dense(64, activation='linear'),  # Nueva capa densa oculta
    #     tf.keras.layers.Dense(64, activation='linear'),  # Nueva capa densa oculta
    #     tf.keras.layers.Dense(64, activation='linear'),  # Nueva capa densa oculta
    #     tf.keras.layers.Dense(64, activation='linear'),  # Nueva capa densa oculta
    #     tf.keras.layers.Dense(32, activation='tanh'),  # Nueva capa densa oculta
    #     tf.keras.layers.Dropout(0.3),
    #     tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax') 
    # ])
    # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])



    """
    lo primero que tenemos que hacer es compilar nuestro modelo, para asi comunicar al backend de tensorflow que queremos entrenar nuestro modelo con el algoritmo de optimizacion Adam, que es un algoritmo de optimizacion que se utiliza para entrenar redes neuronales profundas.

    con el metodo compile se entrena el modelo (a la red neuronal).
    loss es funcion de perdida. binary_crossentropy es la mejor para caracterizar perdida en clasificacion binaria.
    y la metrica es la presicion.
    """
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

    return model


if __name__ == "__main__":
    main()