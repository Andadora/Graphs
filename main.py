import GraphMatrix as GM
import GraphList as GL
import MinHeap
import Vertex

file = open('graf.txt', 'r').read()
graph = GL.GraphList(file)
v1 = Vertex.Vertex(1, True, 'A', 5)
v2 = Vertex.Vertex(2, True, 'A', 8)
v3 = Vertex.Vertex(3, True, 'A', 12)
v4 = Vertex.Vertex(4, True, 'A', 3)
v5 = Vertex.Vertex(5, True, 'A', 10)
v6 = Vertex.Vertex(6, True, 'A', 1)

heapH = MinHeap.MinHeap()
heapH.insert(v1)
heapH.insert(v2)
heapH.insert(v3)
print(heapH.remove())
print(heapH.remove())
heapH.insert(v4)
print(heapH.remove())
heapH.insert(v5)
heapH.insert(v6)
print(heapH.remove())
print(heapH.remove())
print(heapH.remove())

print(graph)
