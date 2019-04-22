import GraphMatrix as GM
import GraphList as GL
import MinHeap

file = open('graf.txt', 'r').read()
graph = GL.GraphList(file)

heapH = MinHeap.MinHeap()
heapH.insert(5)
heapH.insert(6)
heapH.insert(7)
heapH.insert(2)
heapH.insert(9)
print(heapH.remove())
print(heapH.remove())
heapH.insert(12)
print(heapH.remove())
heapH.insert(2)
print(heapH.remove())
print(heapH.remove())
print(heapH.remove())
print(heapH.remove())
