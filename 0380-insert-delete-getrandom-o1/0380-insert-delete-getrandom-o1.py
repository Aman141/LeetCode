class RandomizedSet:

    def __init__(self):
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False
        else:
            self.lst.append(val)
            return True    
        

    def remove(self, val: int) -> bool:
        if val in self.lst:
            self.lst.remove(val)
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