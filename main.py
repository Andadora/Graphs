import GraphMatrix
import GraphList
import GraphData
import time


representation_list = ['List', 'Matrix']
vertices_list = [10, 50, 100, 500, 1000]
density_list = [0.25, 0.50, 0.75, 1.00]

results = open('test.txt', 'a')

for representation in representation_list:
    for vertices in vertices_list:
        for density in density_list:
            duration_100 = 0
            for i in range(1):
                GraphData.graph_generate_file(vertices, density, 0, 'graph.txt')
                file = open('graph.txt', 'r').read()
                if representation == 'List':
                    graph = GraphList.GraphList(file)
                    start = time.perf_counter_ns()
                    graph.dijkstra()
                    end = time.perf_counter_ns()
                    duration = end - start
                    duration_100 += duration
                if representation == 'Matrix':
                    graph = GraphMatrix.GraphMatrix(file)
                    start = time.perf_counter_ns()
                    graph.dijkstra()
                    end = time.perf_counter_ns()
                    duration = end - start
                    duration_100 += duration
            average_duration = duration_100/1
            results.write('r: {:6s}, v: {:5d}, d: {:.2f}, t: {:11.0f} ns\n'.format(representation, vertices, density, average_duration))
results.close()
