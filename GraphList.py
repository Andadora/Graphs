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

    def info(self):
        print(f'edges: {self.edges}\nvertices: {self.vertices}\nstarting vertex: {self.start}')

    def set_start(self, new_start):
        self.start = new_start
