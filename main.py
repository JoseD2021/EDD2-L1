from typing import Any, Optional, Tuple
from AVLTree import AVLTree
from Node import Node
import pandas as pd
from movie import Movie #, create_movie, create_node
Tree = AVLTree()

node = Movie()
node.createMovie("Mission: Impossible II")
print(node.__repr__())
node1 = Movie()

node1.createMovie("Gladiator")

print(node1.__repr__())
print(f"Año de 'Mission: Impossible II': {node.year}")
print(f"Año de 'Gladiator': {node1.year}")
Tree.insert(node)
Tree.insert(node1)


year = int(input("Inserta el año de la película que deseas buscar: "))
found = Tree.search_year(year)

if found:
    print(f"Películas del año {year}:")
    for index, pelicula in enumerate(found, start=1): 
        print(f"{index}. {pelicula}")
else:
    print(f"No se encontraron películas del año {year}.")
