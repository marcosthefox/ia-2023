# Proyecto Knights

## Descripción

El proyecto Knights es un conjunto de acertijos lógicos que involucran a un conjunto de personajes, cada uno de los cuales puede ser un caballero (que siempre dice la verdad) o un mentiroso (que siempre miente). El objetivo es determinar, para cada personaje, si es un caballero o un mentiroso.

La consigna de este trabajo se encuentra en el archivo [Consigna](./tp2-u3-u4.pdf).

## Archivos

El proyecto contiene los siguientes archivos:

- `logic.py`: Este archivo contiene la lógica de la resolución de los acertijos.
- `puzzle.py`: Este archivo contiene los acertijos a resolver. Cada acertijo se representa como una serie de declaraciones hechas por los personajes.

### Puzzle.py

El archivo `puzzle.py` contiene una serie de acertijos. Cada acertijo se representa como una serie de declaraciones hechas por los personajes. El script utiliza la lógica de `logic.py` para resolver los acertijos.

## Resolución de los acertijos

Para resolver los acertijos, el script `puzzle.py` utiliza la lógica de `logic.py`. Cada acertijo se representa como una serie de declaraciones hechas por los personajes. El script utiliza la lógica para determinar, para cada personaje, si es un caballero o un mentiroso.

## Primer Puzzle

A dice "soy a la vez un caballero y un bribon".
- La solucion es: 
Puzzle 0
    A is a Knave

## Segundo Puzzle

A dice "Ambos somos bribones"
B dice ""
- La solucion es:
Puzzle 1
    A is a Knave
    B is a Knight

## Tercer Puzzle

A dice "somos del mismo tipo"
B dice "somos de diferentes tipos"
- La solucion es:
Puzzle 2
    A is a Knave
    B is a Knight

## Cuarto Puzzle

A dice "soy un caballero o soy un bribon pero no sabes cual"
B dice "somos de diferentes tipos"
B dice "A dijo "soy un bribon""
C dice "A es un caballero"

- La solucion es:
Puzzle 3
    A is a Knave
    B is a Knight
    C is a Knave

## Ejecución

Para ejecutar el script `puzzle.py`, usa el siguiente comando en tu terminal:

```bash
python puzzle.py