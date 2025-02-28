class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        else:
            self.lst.append(val)
            self.indices[val] = len(self.lst)-1
            return True    
        

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index = self.indices[val]
            self.indices[self.lst[-1]] = index
            self.lst[index] = self.lst[-1]
            self.lst[-1] = val

            self.indices.pop(val)
            self.lst.pop()
            return True
        else:
            return False    
        

    def getRandom(self) -> int:
        import random 
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()