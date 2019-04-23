import Queue
import Vertex
from math import inf


class GraphMatrix:
    #   wczytuje graf zapisany w pliku tekstowym w formacie:
    #   liczba_krawedzi, liczba_wierzchołków, wierzchołek_startowy
    #   wierzchołek_poczatkowy, wierzchołek_koncowy, waga
    def __init__(self, file):
        lines = file.split('\n')

        parameters = lines[0].split(', ')
        self.edges = int(parameters[0])                                                 # liczba krawedzi
        self.vertices = int(parameters[1])                                              # liczba wierzcholkow
        self.start = int(parameters[2])                                                 # indeks wierzcholka startowego
        self.adjacency_matrix = [[inf] * self.vertices for i in range(self.vertices)]   # utworzenie macierzy sasiedztwa i wypelnienie jej inf oznaczajacymi brak sasiedztwa

        # wczytanie macierzy sasiedztwa
        for line in lines[1:]:
                edge = line.split(', ')
                self.adjacency_matrix[int(edge[0])][int(edge[1])] = int(edge[2])

    def __str__(self):
        return f'edges:\t\t\t\t{self.edges}\nvertices:\t\t\t{self.vertices}\nstarting vertex:\t{self.start}'

    def set_start(self, new_start):
        self.start = new_start

    def dijkstra(self):
        que = Queue.Queue()                         # kolejka wierzchołków do sprawdzenia
        shortest_paths = []                         # tablica przechowująca wierzchołki z indeksem, dystansem i poprzednikiem
        for i in range(self.vertices):
            que.insert(Vertex.Vertex(i, -1, inf))
        que.set_distance(self.start, 0)

        while not que.is_empty():
            current = que.remove()
            shortest_paths.append(current)
            for i in range(self.vertices):
                if que.contains(i):             # sprawdź, czy sprawdzany wierzchołek nie ma już wyliczonej najkrótszej ścieżki
                    if current.distance + self.adjacency_matrix[current.index][i] < que[i].distance:      # jeśli droga przez current jest krótsza:
                        que.set_distance(i, current.distance + self.adjacency_matrix[current.index][i])   # ustaw ją jako nowy dystans
                        que.set_previous(i, current.index)                                                # aktualizuj poprzednika
        return shortest_paths
