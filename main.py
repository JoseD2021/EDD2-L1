from typing import Any, Optional, Tuple
from AVLTree import AVLTree
from Node import Node
import pandas as pd
from movie import Movie

Tree = AVLTree("Mission: Impossible II")

#Tree.insert()
Tree.insert("Gladiator")
Tree.insert("Nancy Drew")
Tree.insert("Helter Skelter")
Tree.insert("The Hobbit: The Desolation of Smaug")
Tree.insert("The Real Exorcist")
Tree.insert("Cast Away")
# Tree.insert("")
# Tree.insert("")

Tree.levels_nr()

#print("root",Tree.root.data.title)

year = int(input("Inserta el año de la película que deseas buscar: "))
found = Tree.search_year(year)

if found:
    print(f"Películas del año {year}:")
    for index, pelicula in enumerate(found, start=1): 
        print(f"{index}. {pelicula}")
else:
    print(f"No se encontraron películas del año {year} que cumplan con todas las características.")
