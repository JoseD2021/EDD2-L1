from typing import Any, Optional, Tuple
from AVLTree import AVLTree
from Node import Node
import pandas as pd
from movie import Movie

Tree = AVLTree("Mission: Impossible II")
Tree.insert("Gladiator")
Tree.insert("Nancy Drew")
Tree.insert("Helter Skelter")
Tree.insert("The Hobbit: The Desolation of Smaug")
Tree.insert("The Real Exorcist")
Tree.insert("Cast Away")

def operaciones_adicionales(pelicula):
    while True:
        print("\nOperaciones adicionales:")
        print("a. Obtener el nivel del nodo.")
        print("b. Obtener el factor de balanceo (equilibrio) del nodo.")
        print("c. Encontrar el padre del nodo.")
        print("d. Encontrar el abuelo del nodo.")
        print("e. Encontrar el tío del nodo.")
        print("f. Volver al menú principal.")

        opcion = input("Selecciona una opción: ")
        
        if opcion == 'a':
            nivel = Tree.nivel(pelicula.title)
            print(f"El nivel del nodo '{pelicula.title}' es: {nivel}")
        
        elif opcion == 'b':
            balance = Tree.calcEquilibrio_titulo(pelicula.title)
            print(f"El factor de balance del nodo '{pelicula.title}' es: {balance}")
        
        elif opcion == 'c':
            _,padre = Tree.search(pelicula.title)
            if padre:
                print(f"El padre de '{pelicula.title}' es: {padre.data.title}")
            else:
                print(f"'{pelicula.title}' no tiene padre.")
        
        elif opcion == 'd':
            abuelo = Tree.find_Grandparent(pelicula.title)
            if abuelo:
                print(f"El abuelo de '{pelicula.title}' es: {abuelo.data.title}")
            else:
                print(f"'{pelicula.title}' no tiene abuelo.")
        
        elif opcion == 'e':
            tio = Tree.find_Uncle(pelicula.title)
            if tio:
                print(f"El tío de '{pelicula.title}' es: {tio.data.title}")
            else:
                print(f"'{pelicula.title}' no tiene tío.")
        
        elif opcion == 'f':
            break
        
        else:
            print("Opción no válida. Por favor selecciona una opción válida.")

def menu():
    while True:
        print("\nMenú de operaciones con el árbol AVL de películas:")
        print("1. Insertar una película.")
        print("2. Eliminar una película.")
        print("3. Buscar una película.")
        print("4. Buscar películas con criterios específicos.")
        print("5. Mostrar recorrido por niveles.")
        print("6. Salir.")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            titulo = input("Ingresa el título de la película: ")
            if Tree.insert(titulo):
                print(f"Película '{titulo}' insertada correctamente.")
            else:
                print(f"La película '{titulo}' ya existe en el árbol.")
                
        elif opcion == '2':
            titulo = input("Ingresa el título de la película que deseas eliminar: ")
            if Tree.delete(titulo):
                print(f"Película '{titulo}' eliminada correctamente.")
            else:
                print(f"La película '{titulo}' no se encontró en el árbol.")
                
        elif opcion == '3':
            metrica = int(input("Selecciona la métrica para buscar: 0. Título, 1. Ingresos Mundiales, 2. Ingresos Nacionales, etc: "))
            valor = input("Ingresa el valor de búsqueda: ")
            nodo = Tree.searchBy(valor, metrica)
            if nodo:
                print(f"Película encontrada: {nodo.data.title}")
                operaciones_adicionales(nodo.data)  # Realizar operaciones adicionales con el nodo encontrado
            else:
                print("Película no encontrada.")
        
        elif opcion == '4':
            year = int(input("Ingresa el año de la película que deseas buscar: "))
            found = Tree.search_year(year)
            if found:
                print(f"Películas del año {year}:")
                for index, pelicula in enumerate(found, start=1):
                    print(f"{index}. {pelicula.title}. Nivel {Tree.nivel(pelicula.title)}")
                
                pelicula_seleccionada = int(input("Selecciona el número de la película para realizar operaciones adicionales: ")) - 1
                if 0 <= pelicula_seleccionada < len(found):
                    operaciones_adicionales(found[pelicula_seleccionada])
                else:
                    print("Selección no válida.")
            else:
                print(f"No se encontraron películas del año {year} que cumplan con los criterios.")
        
        elif opcion == '5':
            print("Recorrido por niveles del árbol (solo los títulos):")
            Tree.levels()
        
        elif opcion == '6':
            print("Saliendo del menú.")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

# Llamar al menú
menu()
