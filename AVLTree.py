from typing import Any, Optional, Tuple
from Node import Node
from movie import Movie
from graphviz import Digraph
import pandas as pd

class AVLTree:
    
    def __init__(self, root: Optional["Node"] = None) -> None:
        if root:
            mv = Movie().createMovie(root)
            if mv != None:
                self.root = Node(mv)
            else:
                print(f"No se ha encontrado la pelicula {root}")
                self.root = None
        else:
            self.root = None

    
    def find_Grandparent(self, title: str) -> Optional["Node"]:
        nodo, parent = self.search(title)  # Busca el nodo y el padre usando el título
        if parent is None:
            return None  # No hay padre, por lo tanto no hay abuelo
        _, grandparent = self.search(parent.data.title) 
        return grandparent

   
    def find_Uncle(self, title: str) -> Optional["Node"]:
        nodo, parent = self.search(title)  # Busca el nodo y el padre usando el título
        if parent is None:
            return None  # No hay padre, por lo tanto no hay tío
        _, grandparent = self.search(parent.data.title)  # Busca el abuelo para identificar al tío
        if grandparent is None:
            return None  
        if grandparent.left == parent:
            return grandparent.right  # El tío es el hijo derecho
        else:
            return grandparent.left  # El tío es el hijo izquierdo

       

    def levels(self):
        self.levelsR([self.root])

    def levelsR(self,list):
        if len(list) > 0:
            p = list.pop(0)
            print(p.data.title, end = ', ')
            if p.left is not None:
                list.append(p.left)
            if p.right is not None:
                list.append(p.right)
            self.levelsR(list)
        

    def height(self) -> int:
        return self.__height_r(self.root)

    def __height_r(self, node: Optional["Node"]) -> int:
        if node is None:
            return 0
        return 1 + max(self.__height_r(node.left), self.__height_r(node.right))

    def search(self, data: Any) -> Tuple[Optional["Node"], Optional["Node"]]:
        p, pad = self.root, None
        while p is not None:
            if data == p.data.title:
                return p, pad
            else:
                pad = p
                if data < p.data.title:
                    p = p.left
                else:
                    p = p.right
            
        return p, pad
    
    def searchBy(self, value: Any, m = 0) -> "Node" :
        p = self.root
        while p is not None:
            if (m == 0):
                if value == p.data.title:
                    return p
                else:
                    if value < p.data.title:
                        p = p.left
                    else:
                        p = p.right
            elif (m == 1):
                if value == p.data.worldwide_earnings:
                    return p
                else:
                    if value < p.data.worldwide_earnings:
                        p = p.left
                    else:
                        p = p.right
            elif (m == 2):
                if value == p.data.domestic_earnings:
                    return p
                else:
                    if value < p.data.domestic_earnings:
                        p = p.left
                    else:
                        p = p.right
            elif (m == 3):
                if value == p.data.domestic_percent:
                    return p
                else:
                    if value < p.data.domestic_percent:
                        p = p.left
                    else:
                        p = p.right
            elif (m == 4):
                if value == p.data.foreign_earnings:
                    return p
                else:
                    if value < p.data.foreign_earnings:
                        p = p.left
                    else:
                        p = p.right
            elif (m == 5):
                if value == p.data.foreign_percent:
                    return p
                else:
                    if value < p.data.foreign_percent:
                        p = p.left
                    else:
                        p = p.right
            elif (m == 6):
                if value == p.data.year:
                    return p
                else:
                    if value < p.data.year:
                        p = p.left
                    else:
                        p = p.right
        return p
    
    def insert(self, data: Any) -> int: # -1 no se encontro la pelicula. 0 ya fue encontrada. 1 exito
        mv = Movie().createMovie(data)
        if mv != None:
            to_insert = Node(mv)
        else:
            return -1

        if self.root is None:
            self.root = to_insert
            return 1
        else:
            p, pad = self.search(data)
            if p is not None:
                return 0 
            else:
                if data < pad.data.title:
                    pad.left = to_insert
                else:
                    pad.right = to_insert
                self.actualizarEquilibrio(pad)
                return 1
            
    def deleteBy(self, data: Any, m = 0):
        self.delete(self.searchBy (data, m).data.title)

    def delete(self, data: Any, mode: bool = True) -> bool:
        p, pad = self.search(data)
        if p is not None:
            if pad is None and p == self.root and p.left is None and p.right is None:
                self.root = None
                return True

            if p.left is None and p.right is None:
                if p == pad.left:
                    pad.left = None
                else:
                    pad.right = None
                del p
            elif p.left is None and p.right is not None:
                if p == pad.left:
                    pad.left = p.right
                else:
                    pad.right = p.right
                del p
            elif p.left is not None and p.right is None:
                if p == pad.left:
                    pad.left = p.left
                else:
                    pad.right = p.left
                del p
            else:
                if mode:
                    pred, pad_pred, son_pred = self.__pred(p)
                    p.data = pred.data
                    if p == pad_pred:
                        pad_pred.left = son_pred
                    else:
                        pad_pred.right = son_pred
                    del pred
                else:
                    sus, pad_sus, son_sus = self.__sus(p)
                    p.data = sus.data
                    if p == pad_sus:
                        pad_sus.right = son_sus
                    else:
                        pad_sus.left = son_sus
                    del sus
            self.actualizarEquilibrio(pad)
            return True
        return False

    def __pred(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad, p.left

    def __sus(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p, pad, p.right

    def calcEquilibrio(self, node: "Node") -> int:
        return self.__height_r(node.right) - self.__height_r(node.left)


    def actualizarEquilibrio(self, node: "Node") -> None:
        if node is not None:
            # llega a cada nodo hoja
            if node.left is not None:
                self.actualizarEquilibrio(node.left)
            if node.right is not None:
                self.actualizarEquilibrio(node.right)
            # si es nodo hoja comprueba su factor de equilibrio
            if node.left is None and node.right is None:
                self.actualizarEquilibrio2(node)
    
    def actualizarEquilibrio2(self, node: "Node"): 
        #comprueba todos los factores de equilibrio desde el nodo hasta la raiz
        while node is not None:
            node.fEquilibrio = self.calcEquilibrio(node)
            if node.fEquilibrio < -1 or node.fEquilibrio > 1:
                self.rebalance(node)
                
            node = self.search(node.data.title)[1]

    def rebalance(self, node: "Node") -> None:
        ad = node.data.title
         
        if node.fEquilibrio == 2 and node.right.fEquilibrio >= 0:
            node = self.simpleLeftRotation(node)
        elif node.fEquilibrio == -2 and node.left.fEquilibrio <= 0:
            node = self.simpleRightRotation(node)
        elif node.fEquilibrio == 2 and node.right.fEquilibrio == -1:
            node = self.doubleRightLeft(node)
        elif node.fEquilibrio == -2 and node.left.fEquilibrio == 1:
            node = self.doubleLeftRight(node)

        if ad == self.root.data.title:
            self.root = node
        else:
            pad = self.search(ad)[1]
            if pad.left.data.title == ad:
                pad.left = node
            else: 
                pad.right = node

        
    
    def simpleLeftRotation(self, node: "Node") -> "Node":
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux

    def simpleRightRotation(self, node: "Node") -> "Node":
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux

    def doubleRightLeft(self, node: "Node") -> "Node":
        node.right = self.simpleRightRotation(node.right)
        return self.simpleLeftRotation(node)

    def doubleLeftRight(self, node: "Node") -> "Node":
        node.left = self.simpleLeftRotation(node.left)
        return self.simpleRightRotation(node)
    
    def search_year(self, year: int):
        resultados = []

        def buscar_por_año(nodo):
            if nodo is None:
                return

            if nodo.data.year == year and nodo.data.domestic_percent < nodo.data.foreign_percent and nodo.data.foreign_earnings >= 10000000:
                resultados.append(nodo.data)

            buscar_por_año(nodo.left)
            buscar_por_año(nodo.right)

        buscar_por_año(self.root)
        return resultados
    
    def nivel(self, data: Any) -> int:
        p = self.root
        nivel = 0

        while p is not None:
            if data == p.data.title:
                return nivel
            elif data < p.data.title:
                p = p.left
            else:
                p = p.right
            nivel += 1

        return -1


    def visualize(self, filename='avl_tree'):
        #Genera una visualización del árbol AVL y la guarda en un archivo.
        def add_edges(dot, node):
            if node is not None:
                if node.left is not None:
                    dot.node((node.left.data.title).replace(":","")) # elimina los ":" para evitar conflictos con la sintaxis de graphviz
                    dot.edge((node.data.title).replace(":",""), (node.left.data.title).replace(":",""))
                    add_edges(dot, node.left)
                if node.right is not None:
                    dot.node((node.right.data.title).replace(":",""))
                    dot.edge((node.data.title).replace(":",""), (node.right.data.title).replace(":",""))
                    add_edges(dot, node.right)

        dot = Digraph()
        if self.root is not None:
            dot.node((self.root.data.title).replace(":",""))
            add_edges(dot, self.root)
        dot.render(filename, format='png', cleanup=True)  # Guarda el archivo en formato PNG
        
    def calcEquilibrio_titulo(self, title: str) -> int:
        nodo, _ = self.search(title)  # Busca el nodo utilizando el título
        if nodo is None:
            print(f"No se ha encontrado la película con el título {title}.")
            return 0
        return self.calcEquilibrio(nodo) # Calcula el equilibrio enviando el nodo

#Tree = AVLTree()
#
#ds = pd.read_csv("dataset_movies.csv")
#
#for i in range(0,43):
#    Tree.insert(ds.iloc[i]["Title"])
#
##for i in range(0,4951):
##    Tree.delete(ds.iloc[i]["Title"])
#
#Tree.visualize('AVLTree')