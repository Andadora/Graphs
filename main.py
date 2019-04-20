import GraphMatrix as GM
import GraphList as GL

file = open('graf.txt', 'r').read()
graph = GL.GraphList(file)

graph.info()
graph.set_start(2)
graph.info()
print(graph.adjacency_list)
