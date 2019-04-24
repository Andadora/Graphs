import GraphMatrix as GM
import GraphList as GL
import GraphData as GD

GD.graph_generate_file(10, 0.5, 0, 'graph.txt')
file = open('graph.txt', 'r').read()
graph = GL.GraphList(file)
results = open('results.txt', 'w')

results.write(str(graph.dijkstra()))

representation_list = ['List', 'Matrix']
vertices_list = [10, 50, 100, 500, 1000]
density_list = [0.25, 0.50, 0.75, 1]

# for vertices in vertices_list:
#    for density in density_list:
#        for representation in representation_list:
#            for i in range(100):

# GD.graph_generate_file(vertices, density, 0, 'graph.txt')

