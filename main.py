from typing import Any, Optional, Tuple
from AVLTree import AVLTree
from Node import Node
import pandas as pd
from Movie import Movie #, create_movie, create_node
Tree = AVLTree()

node = Movie()
node.createMovie("Mission: Impossible II")

print(node.__repr__())

node = Movie().createMovie("Gladiator")

print(node.__repr__())