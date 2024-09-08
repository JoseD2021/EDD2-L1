from typing import Any, Optional, Tuple
from AVLTree import AVLTree
from Node import Node
import pandas as pd
from movie import create_movie, create_node
Tree = AVLTree()

node = create_node("Mission: Impossible II")

print(node.data)