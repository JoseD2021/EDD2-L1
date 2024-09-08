from typing import Any, Optional, Tuple
from AVLTree import AVLTree
from Node import Node
import pandas as pd
from Movie import Movie, createMovie


#tree = AVLTree()
#
#for i in [80,50,20,10,34,98,67,12,4,76,3,78,90,45]:
#    tree.insert(i)
#
#tree.levels_nr()
#
#tree.delete(50)
#
#tree.levels_nr()
#node = Movie()
#node.createMovie("Mission: Impossible II")
# 
#print(node.__repr__())
# 
node = createMovie("Mission: Impossible II")
# 
print(node.__str__())