class MinHeap:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def swap(self, first, second):
        temp = self.elements[first]
        self.elements[first] = self.elements[second]
        self.elements[second] = temp

    def up_heap(self, min, max):
        child = max                         # indeks dziecka - nowego elementu
        parent = int((child - 1)/2)         # indeks  rodzica nowododanego elementu (ostatniego)
        value = self.elements[child]        # zapamiętanie przesuwanego w górę elementu
        while(child > min) and (self.elements[parent] > value):     # dopóki nad dzieckiem jest mniejsza wartość popycha dziecko w górę
            self.elements[child] = self.elements[parent]
            child = parent
            parent = int((child - 1)/2)
        self.elements[child] = value

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
        self.elements.append(element)
        self.up_heap(0, len(self.elements) - 1)

    def remove(self):
        self.swap(0, len(self.elements) - 1)
        self.down_heap(0, len(self.elements) - 2)        # jako max podaję przedostatni indeks żeby nie sortowało tego który chcemy usunąć
        return self.elements.pop()
