class GraphMatrix:

    #   wczytuje graf zapisany w pliku tekstowym w formacie:
    #   liczba_krawedzi, liczba_wierzchołków, wierzchołek_startowy
    #   wierzchołek_poczatkowy, wierzchołek_koncowy, waga
    def __init__(self, file):
        lines = file.split('\n')

        parameters = lines[0].split(', ')
        self.edges = int(parameters[0])                                                 #liczba krawedzi
        self.vertices = int(parameters[1])                                              #liczba wierzcholkow
        self.start = int(parameters[2])                                                 #indeks wierzcholka startowego
        self.adjacency_matrix = [[0] * self.vertices for i in range(self.vertices)]     #utworzenie macierzy sasiedztwa i wypelnienie jej 0 oznaczajacymi brak sasiedztwa

        #wczytanie macierzy sasiedztwa
        for line in lines[1:]:
                edge = line.split(', ')
                self.adjacency_matrix[int(edge[0])][int(edge[1])] = int(edge[2])

    def __str__(self):
        return f'edges:\t\t\t\t{self.edges}\nvertices:\t\t\t{self.vertices}\nstarting vertex:\t{self.start}'

    def set_start(self, new_start):
        self.start = new_start
