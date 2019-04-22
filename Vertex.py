class Vertex:
    def __init__(self, index, visited, previous, distance):
        self.index = index
        self.visited = visited
        self.previous = previous
        self.distance = distance

    def __str__(self):
        return f'wierzchołek:\t\t\t\t{self.index}\nodwiedzony:\t\t\t\t\t{self.visited}\npoprzedni:\t\t\t\t\t{self.previous}\nodległość od startowego:\t{self.distance}\n'

    def __lt__(self, other):
        if self.distance < other.distance:
            return True
        else:
            return False

    def __le__(self, other):
        if self.distance <= other.distance:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.distance == other.distance:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.distance != other.distance:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.distance > other.distance:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.distance >= other.distance:
            return True
        else:
            return False
