import random


# generuje plik z grafem w postaci:
# liczba_krawedzi, liczba_wierzchołków, wierzchołek_startowy
# wierzchołek_poczatkowy, wierzchołek_koncowy, waga
def graph_generate_file(vertices, density, start, file_name):
    file = open(file_name, 'w')

    edges = int(density*vertices*(vertices-1))      # wylicz liczbę krawędzi z gęstości
    file.write(f'{edges}, {vertices}, {start}')

    population = []                                 # stwórz tablicę wszystkich możliwych krawędzi bez pętli
    for i in range(vertices):
        for j in range(vertices):
            if i != j:
                population.append([i, j])
    random_pairs = random.sample(population, edges)  # wybierz losowo krawędzie bez zwracania

    for i in range(edges):
        distance = random.randint(1, 100)
        file.write(f'\n{random_pairs[i][0]}, {random_pairs[i][1]}, {distance}')

    file.close()
