# TP01 - TicTacToe

## Descripción

La consigna de este trabajo se encuentra en el archivo [Consigna](./tp1-u1-u2.pdf), los requerimientos para ejecutar el proyecto en el archivo [requeriments](./requeriments.txt),
y la presentacion en el archivo [Presentacion](./TicTacToe.pdf).

## Juegos de suma cero
Entornos deterministas, totalmente observables en los cuales hay dos agentes cuyas acciones deben alternar y en los que los valores utilidad, al final de juego, son siempre iguales y opuestos.
Es decir que si uno gana es porque el otro pierde.
Ejemplo torta, si le doy mas a uno es necesariamente a costa de darle menos a otro.

## Desiciones optimas en juegos
- Jugadores MAX y MIN.
- Mueven por turno hasta que el juego termina.
- Al final del juego tenemos un ganador y un perdedor.

## Definiendo un juego
- El estado inicial, que incluye la posición del tablero e identifica al jugador que mueve.
- Una función sucesor, que devuelve una lista de pares (movimiento, estado), indicando un movimiento legal y el estado que resulta.
- Un test terminal, que determina cuándo se termina el juego. A los estados donde el juego se ha terminado se les llaman estados terminales.
- Una función utilidad, que da un valor numérico a los estados terminales. En este caso, el resultado es un triunfo, pérdida, o empate, con valores 1, -1, 0. 

## Arbol de juegos
El estado inicial y los movimientos legales para cada lado definen el árbol de juegos.
Desde el estado inicial, MAX tiene nueve movimientos posibles. El juego alterna entre la colocación de una X para MAX y la colocación de un O para MIN, hasta que alcancemos nodos hoja correspondientes a estados terminales, de modo que un jugador tenga tres en raya o todos los cuadrados estén llenos.
El número sobre cada nodo hoja indica el valor de utilidad del estado terminal desde el punto de vista de MAX; se supone que los va-
lores altos son buenos para MAX y malos para MIN (por eso los nombres de los jugadores).

Este trabajo de MAX al usar el árbol de búsqueda (en particular la utilidad de estados ter-
minales) determina el mejor movimiento.

Incluso para este simple juego es demasiado complejo para dibujar el arbol de juegos entero.

## Estrategia optima
El valor minimax de un nodo es la utilidad (para MAX) de estar en el estado correspondiente, asumiendo que ambos jugadores juegan óptimamente desde allí al final del juego. Obviamente, el valor minimax de un estado terminal es solamente su utilidad. Además, considerando una opción, MAX preferirá moverse a un estado de valor máximo, mientras que MIN prefiere un estado de valor mínimo.

Puede haber otras estrategias contra oponentes subóptimos que lo hagan mejor que la estrategia minimax;

## Algoritmo MINIMAX
Es un metodo de decision para minimizar la perdida maxima de puntuacion.
Realiza un calculo de manera recursiva y asi va eligiendo el mejor movimiento posible para el adversario.

Cuando el turno es el propio, se toma el max de los hijos.
Si el turno es el del contrario, se toma el min, porq el contrario toma el mejor camino para el 

En los nodos de los jugadores maximizadores, se selecciona la opción que maximice el valor de los nodos hijos, asumiendo que el oponente tomará las decisiones que minimicen este valor. En los nodos de los jugadores minimizadores, se selecciona la opción que minimice el valor de los nodos hijos, asumiendo que el oponente maximizará este valor.

Valor Minimax: Una vez que el algoritmo ha explorado el árbol hasta una cierta profundidad, se puede determinar la mejor jugada posible para el jugador maximizador. Esto se logra propagando hacia arriba los valores minimax desde las hojas hasta la raíz del árbol.

En este pseudocódigo, nodo representa el estado actual del juego, profundidad es la profundidad máxima que se analizará en el árbol, esMaximizador indica si el nodo actual pertenece al jugador maximizador.

El algoritmo minimax es una función recursiva que se llama para explorar el árbol de juego. En cada llamada, se evalúan los nodos hijos y se selecciona el valor máximo o mínimo, dependiendo de si el nodo actual pertenece al jugador maximizador o minimizador, respectivamente.

# Poda Alfa-Beta
El problema de la búsqueda minimax es que el número de estados que tiene que examinar es exponencial en el número de movimientos.
La jugada es que es posible calcular la decisión minimax correcta sin mirar todos los nodos en el árbol de juegos.

El algoritmo de búsqueda alfa-beta calcula el mismo movimiento óptimo que el
minimax, pero consigue una eficiencia mucho mayor, eliminando subárboles que
son probablemente irrelevantes.

La poda alfa-beta consigue su nombre de los dos parámetros que describen los límites
sobre los valores hacia atrás que aparecen a lo largo del camino:
- ALFA: el valor de la mejor opción (es decir, valor más alto) que hemos encontrado has-
ta ahora en cualquier punto elegido a lo largo del camino para MAX.
- BETA:  el valor de la mejor opción (es decir, valor más bajo) que hemos encontrado has-
ta ahora en cualquier punto elegido a lo largo del camino para MIN.
La búsqueda alfa-beta actualiza el valor de  y  según se va recorriendo el árbol y poda
las ramas restantes en un nodo (es decir, termina la llamada recurrente) tan pronto como
el valor del nodo actual es peor que el actual valor  o  para MAX o MIN, respectivamente.



