class Vertex:
    def __init__(self, previous, distance):
        self.previous = previous
        self.distance = distance

    def __str__(self):
        return f'poprzedni:\t\t\t\t\t{self.previous}\nodległość od startowego:\t{self.distance}\n'

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
