import Queue
import Vertex
from math import inf


class GraphList:

    #   wczytuje graf zapisany w pliku tekstowym w formacie:
    #   liczba_krawedzi, liczba_wierzchołków, wierzchołek_startowy
    #   wierzchołek_poczatkowy, wierzchołek_koncowy, waga
    def __init__(self, file):
        lines = file.split('\n')

        parameters = lines[0].split(', ')
        self.edges = int(parameters[0])         # liczba krawedzi
        self.vertices = int(parameters[1])      # liczba wierzcholkow
        self.start = int(parameters[2])         # indeks wierzcholka startowego
        self.adjacency_list = []                # utworzenie pustej listy sąsiedztwa
        for i in range(self.vertices):          # zagnieżdżenie w liście sąsiedztwa pustych list w liczbie wierzchołków grafu
            self.adjacency_list.append([])

        # wczytanie listy sasiedztwa
        for line in lines[1:]:
            edge = line.split(', ')
            edge_object = [int(edge[1]), int(edge[2])]
            self.adjacency_list[int(edge[0])].append(edge_object)

    def __str__(self):
        return f'edges:\t\t\t\t{self.edges}\nvertices:\t\t\t{self.vertices}\nstarting vertex:\t{self.start}'

    def set_start(self, new_start):
        self.start = new_start

    def dijkstra(self):
        que = Queue.Queue()                         # kolejka wierzchołków do sprawdzenia
        shortest_paths = []                         # tablica przechowująca wierzchołki z indeksem, dystansem i poprzednikiem
        for i in range(self.vertices):
            que.insert(Vertex.Vertex(i, -1, inf, ''))
        que.set_distance(self.start, 0)

        while not que.is_empty():
            current = que.remove()
            shortest_paths.append(current)
            for edge in self.adjacency_list[current.index]:
                if que.contains(edge[0]):                 # sprawdź, czy sprawdzany wierzchołek nie ma już wyliczonej najkrótszej ścieżki
                    if current.distance + edge[1] < que[edge[0]].distance:
                        que.set_distance(edge[0], current.distance + edge[1])
                        que.set_previous(edge[0], current.index)                              # aktualizuj poprzednika
                        que.set_path(edge[0], f'{current.path}{current.index} -> ')                 # aktualizuj sciezke
        return shortest_paths
