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
