class Node:
    def __init__(self, key, link=None):
        self.data = key
        self.link = link

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hashFn(self, key):
        return key % self.size

    def insert(self, key):
        k = self.hashFn(key)
        n = Node(key)
        n.link = self.table[k]
        self.table[k] = n

    def search(self, key):
        k = self.hashFn(key)
        n = self.table[k]
        while n is not None:
            if n.data == key:
                return n.data
            n = n.link
        return None

    def delete(self, key):
        k = self.hashFn(key)
        n = self.table[k]
        before = None
        while n is not None:
            if n.data == key:
                if before == None:
                 self.table[k] = n.link
                else:
                    before.link = n.link
                return
            before = n
            n = n.link
