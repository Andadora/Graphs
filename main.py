import GraphMatrix as GM
import GraphList as GL
import Queue
import Vertex

file = open('graf.txt', 'r').read()
graph = GL.GraphList(file)

v0 = Vertex.Vertex(1, 30)
v1 = Vertex.Vertex(2, 8)
v2 = Vertex.Vertex(1, 6)
que = Queue.Queue()
que.insert(v0)
que.insert(v1)
que.insert(v2)
print(que)
que.set_distance(0, 2)
print(que.remove())
print(que.remove())
print(que.remove())
print(que)

