import GraphMatrix as GM
import GraphList as GL
import Queue
import Vertex

file = open('graf.txt', 'r').read()
graph = GM.GraphMatrix(file)

print(graph.dijkstra())
