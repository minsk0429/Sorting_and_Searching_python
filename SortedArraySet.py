class SortedArraySet:
    def __init__(self, capacity=100):
        self.array = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def isFull(self):
        return self.size >= self.capacity

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self, e):
        if self.contains(e) or self.isFull():
            return
    
        self.array[self.size] = e
        self.size += 1

        for i in range(self.size - 1, 0, -1):
            if self.array[i - 1] <= self.array[i]:
                break
            self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]

    def __eq__(self, setB):
        if self.size != setB.size:
            return False
    
        for i in range(self.size):
            if self.array[i] != setB.array[i]:
                return False
        return True

    def union(self, setB):
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                setC.insert(b)
                j += 1

        while i < self.size:
            setC.insert(self.array[i])
            i += 1
        while j < setB.size:
            setC.insert(setB.array[j])
            j += 1

        return setC
    
    def __str__(self):
        return str(self.array[:self.size])

