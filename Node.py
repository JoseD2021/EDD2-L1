from typing import Any, Optional, Tuple

class Node:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.fEquilibrio: int = 0