class MyHashMap:

    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.table = [None]*self.capacity
        self.deleted = object()
        
    def _hash(self,key):
        return key%self.capacity


    def _probe(self,key):  
        index = self._hash(key)
        while self.table[index] is not None and self.table[index] is not self.deleted and self.table[index][0]!=key:
            index = (index + 1)% self.capacity

        return index          

    def _rehash(self):
        old_table = self.table
        self.capacity *=2
        self.table  = [None]*self.capacity
        self.size = 0

        for item in old_table:
            if item is not None and item is not self.deleted:
                self.put(item[0], item[1])   

    def put(self, key: int, value: int) -> None:
        if self.size/self.capacity >= 0.7:
            self._rehash()

        index = self._probe(key)    

        if self.table[index] is None or self.table[index] is self.deleted:
            self.table[index] = [key, value]
            self.size += 1
        else:
            self.table[index][1] = value    


    def get(self, key: int) -> int:
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0]== key:
                return self.table[index][1]

            index = (index + 1) % self.capacity    
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted
                self.size -=1 
                return 

            index = (index + 1) % self.capacity   


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)