import GraphMatrix as GM
import GraphList as GL
import GraphData as GD

GD.graph_generate_file(4, 0.5, 0, 'graph.txt')
file = open('graph.txt', 'r').read()
graph = GL.GraphList(file)
print(graph.dijkstra())
