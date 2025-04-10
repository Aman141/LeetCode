class MyHashSet:

    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.table = [None]*self.capacity
        self.deleted = object()

    def _hash(self, key:int) -> int:
        return key % self.capacity        

    def _probe(self, key:int) -> int:
        index = self._hash(key)
        while self.table[index] is not None and self.table[index]!=key:
            index = (index + 1)% self.capacity

        return index    

    def _rehash(self) ->None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None]*self.capacity
        self.size = 0
        for item in old_table:
            if item is not None and item is not self.deleted:
                self.add(item)

    def add(self, key: int) -> None:
        if self.size / self.capacity >= 0.7:
            self._rehash()
        index = self._probe(key)
        if self.table[index]!=key:
            self.table[index]=key
            self.size +=1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.deleted
                self.size -=1
                return

            index = (index + 1)%self.capacity    

        

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return True

            index = (index + 1)%self.capacity  

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)