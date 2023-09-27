import csv
import sys
import time


from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    start_time = time.time()
    path = shortest_path(source, target)
    end_time = time.time()

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    """
    ver las peliculas del chango
    sacar los actores que estan en esa pelicula
    recorrer cada actor
    si el actor == target => return path
    sino ver las peliculas del chango 2.0
    repetir
    """
    """Finds a solution to maze, if one exists."""

    #Inicio
    #Indico nodo inicial
    #  state -> ACTOR
    #  parent -> ACTOR PADRE 
    #  action -> PELICULA CON LA QUE SE RELACIONA CON EL ACTOR PADRE 
    start = Node(state=source, parent=None, action=None)

    #Creo la frontera
    #frontier = QueueFrontier()
    frontier = StackFrontier()
    #Agrego el nodo inicial a la frontera
    frontier.add(start)

    #Inicializo path
    path = set()

    #Lista con los nodos que ya exploró, aquellos a los cuales ya se han realizado las comprobaciones
    explored = set()

    #Inicio loop infinito recursivo para recorrer nodos hasta encontrar la solucion
    while True:

        # Si la frontera está vacía quiere decir que terminamos de recorrer todos los posibles nodos y por lo tanto no encontramos nada de lo que queríamos
        if frontier.empty():
            raise Exception("no solution")

        # Sacamos un nodo de la frontera para trabajar con el
        # En el caso inicial se trata del start
        node = frontier.remove()

        # Comprobamos si el noda que acabamos de sacar de la frontera es la solucion
        if node.state == target:
            #En caso de serlo armamos el path
            actions = []
            actors = []
            #Si es el nodo start no hace falta esto porque no hay path, es directamente la solucion
            while node.parent is not None:
                #En este caso CREOOOO que agrega LA PELI a una lista de peliculas (No sé si son LAS PELIS)
                actions.append(node.action)
                #En este caso lo que hace es agregar el actor a una lista de actores para el path
                actors.append(node.state)
                #Cambiamos el nodo actual a nodo padre
                node = node.parent
            #Da vuelta los arreglos para poner el path, donde el ultimo será el que debe mostrar mas a la detecha
            actions.reverse()
            actors.reverse()
            
            solution = list(zip(actions, actors))
            return solution
            

        # Crea una blacklist de los nodos ya explorados para no entrar en bucles infinitos
        # No aceptará mas en la frontera nodos que ya haya explorado antes
        explored.add(node.state)

        
        #La funcion neighbors_for_person devuelve una lista de tuplas (peli,actor) que serian todas las peliculas de el actor que recibe la func, 
        # con los actores que trabajo
        for action, state in neighbors_for_person(node.state):
            #Para cada par, comprobamos que el mismo no esté ya explorado, ni que se encuentra ya en la frontera
            if not frontier.contains_state(state) and state not in explored:
                #Creamos los hijos o nodos que surgen del nodo actual (futuro padre) y los agregamos en la frontera
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)

    # TODO
    raise NotImplementedError

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()