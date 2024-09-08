from typing import Any, Optional, Tuple
from Node import Node
import movie as mv


class AVLTree:
    
    def __init__(self, root: Optional["Node"] = None) -> None:
        self.root = mv.create_node(root)

    def levels_nr(self) -> None:
        q = []
        p = self.root
        q.append(p)
        while len(q) > 0:
            p = q.pop(0)
            print(p.data, end = ' ')
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        print()

    def height(self) -> int:
        return self.__height_r(self.root)

    def __height_r(self, node: Optional["Node"]) -> int:
        if node is None:
            return 0
        return 1 + max(self.__height_r(node.left), self.__height_r(node.right))

    @staticmethod
    def generate_sample_tree() -> "AVLTree":
        T = AVLTree(Node('A'))
        T.root.left = Node('B')
        T.root.right = Node('C')
        T.root.left.left = Node('D')
        T.root.left.right = Node('E')
        T.root.right.right = Node('F')
        T.root.right.left = Node('G')
        T.root.left.left.left = Node('H')
        T.root.left.left.right = Node('I')
        T.root.right.left.left = Node('J')
        T.root.right.left.right = Node('K')

        return T

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

    def insert(self, data: Any) -> bool:
        to_insert = mv.create_node(data)
        if self.root is None:
            print(f"Inserción: {data.title} (Año: {data.year}) - como raíz")
            self.root = to_insert
            return True
        else:
            p, pad = self.search(data.title)
            if p is not None:
                print(f"La película {data.title} ya existe.")
                return False
            else:
                print(f"Inserción: {data.title} (Año: {data.year})")
                if data < pad.data.title:
                    pad.left = to_insert
                else:
                    pad.right = to_insert
                self.actualizarEquilibrio(pad)
                return True

    def delete(self, data: Any, mode: bool = True) -> bool:
        p, pad = self.search(data)
        if p is not None:
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
        while (node != None):
            node.fEquilibrio = self.calcEquilibrio(node)
            if node.fEquilibrio < -1 or node.fEquilibrio > 1:
                self.rebalance(node)
                
            node = self.search(node.data)[1]

    def rebalance(self, node: "Node") -> None:
        ad = node.data
        
        if node.fEquilibrio == 2 and node.right.fEquilibrio == -1:
            node = self.doubleRightLeft(node)
        elif node.fEquilibrio == -2 and node.left.fEquilibrio == 1:
            node = self.doubleLeftRight(node)
        elif node.fEquilibrio == 2 and node.right.fEquilibrio >= 0:
            node = self.simpleLeftRotation(node)
        elif node.fEquilibrio == -2 and node.left.fEquilibrio <= -1:
            node = self.simpleRightRotation(node)

        if ad == self.root.data:
            self.root = node
        else:
            pad = self.search(ad)[1]
            if pad.left.data == ad:
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

            if nodo.data.year == year:
                resultados.append(nodo.data)
                print(f"Encontrada: {nodo.data.title} del año {nodo.data.year}")  # Impresión de debugging

            buscar_por_año(nodo.left)
            buscar_por_año(nodo.right)

        buscar_por_año(self.root)
        print("a")
        return resultados
