class Node:
    def __init__(self, coords=None):
        if coords is None:
            coords = []
        self._coords = coords

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value

    def __eq__(self, other):
        return isinstance(other, Node) and self.coords == other.coords

    def __repr__(self):
        return f"{self._coords}" + "\n"
