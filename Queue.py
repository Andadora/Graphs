import Vertex


class Queue:
    def __init__(self):
        self.elements = []
        self.heap_positions = []            # hpos[elind] = indeks w kopcu
        self.elements_indexes = []          # elind[hpos] = indeks elementu

    def __getitem__(self, index):           # zwraca element-wierzchołek o danym indeksie
        return self.elements[self.heap_positions[index]]

    def __str__(self):
        return f'hpos:   {self.heap_positions}\nelind:  {self.elements_indexes}'

    def is_empty(self):
        return not self.elements

    def contains(self, index):
        if self.heap_positions[index] != -1:
            return True
        else:
            return False

    def swap(self, first, second):
        temp = self.elements[first]
        self.elements[first] = self.elements[second]
        self.elements[second] = temp
        temp_index = self.elements_indexes[first]
        self.elements_indexes[first] = self.elements_indexes[second]
        self.elements_indexes[second] = temp_index
        self.heap_positions[temp_index] = second
        self.heap_positions[self.elements_indexes[first]] = first

    def up_heap(self, min, max):
        child = max                          # indeks dziecka - nowego elementu w kopcu
        parent = int((child - 1)/2)          # indeks  rodzica nowododanego elementu (ostatniego) w kopcu
        value = self.elements[child]         # zapamiętanie przesuwanego w górę elementu
        index = self.elements_indexes[child] # zapamiętanie indeksu elementu przesuwanego
        while(child > min) and (self.elements[parent] > value):     # dopóki nad dzieckiem jest mniejsza wartość popycha dziecko w górę
            self.elements[child] = self.elements[parent]
            self.elements_indexes[child] = self.elements_indexes[parent]
            self.heap_positions[self.elements_indexes[parent]] = child
            child = parent
            parent = int((child - 1)/2)
        self.elements[child] = value
        self.elements_indexes[child] = index
        self.heap_positions[index] = child

    def down_heap(self, min, max):
        parent = min
        while True:
            left_child = parent * 2 + 1
            right_child = parent * 2 + 2
            if (left_child <= max) and (self.elements[left_child] < self.elements[parent]):     # jeśli lewe dziecko mniejsze o rodzica:
                index = left_child                                                              # zapamiętaj jego indeks
            else:
                index = parent                                                                  # jeśli nie - zapamiętaj indeks rodzica
            if (right_child <= max) and (self.elements[right_child] < self.elements[index]):    # jeśli prawe dziecko mniejsze od zapamiętanego
                index = right_child                                                             # zapamiętaj jego indeks
            if index == parent:                                                                 # jeśli indeks równy rodzicowi mamy kopiec minimany
                break
            else:
                self.swap(index, parent)                                                        # jeśli nierówny powtórz dla nowego rodzica
                parent = index

    def insert(self, element):
        self.elements_indexes.append(len(self.heap_positions))      # dodaje do tablicy nową pozycję w kopcu i przypisuje jej kolejny indeks elementu
        self.heap_positions.append(len(self.elements_indexes)-1)    # dodaje kolejny indeks elementu i przypisuje ostatnią pozycję w kopcu
        self.elements.append(element)
        self.up_heap(0, len(self.elements) - 1)

    def remove(self):
        self.swap(0, len(self.elements) - 1)
        self.down_heap(0, len(self.elements) - 2)               # jako max podaję przedostatni indeks żeby nie sortowało tego który chcemy usunąć
        self.heap_positions[self.elements_indexes.pop()] = -1   #usuwa ostatnią pozycję kopca w elind i zaznacza w hpos, że indeks o tym numerze nie znajduje się w kopc (-1)
        return self.elements.pop()

    def set_distance(self, element_index, new_distance):
        h_position = self.heap_positions[element_index]
        if new_distance > self.elements[h_position].distance:       # jeśli nowy dystans większy:
            self.elements[h_position].distance = new_distance
            self.down_heap(h_position, len(self.elements) - 1)      # zepchnij element w dół kopca
        if new_distance < self.elements[h_position].distance:       # jeśli nowy jest mniejszy:
            self.elements[h_position].distance = new_distance
            self.up_heap(0, h_position)                             # wypchnij element w górę

    def set_previous(self, element_index, new_previous):
        h_position = self.heap_positions[element_index]
        self.elements[h_position].previous = new_previous

    def set_path(self, element_index, new_path):
        h_position = self.heap_positions[element_index]
        self.elements[h_position].path = new_path
