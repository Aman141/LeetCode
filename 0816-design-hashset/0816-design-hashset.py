class Node:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.head = None
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return 
        if not self.head:
            self.head = Node(val=key)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = Node(val = key)            
        

    def remove(self, key: int) -> None:
        if self.head and self.head.val == key:
            self.head = self.head.next
            return

        curr = self.head
        while curr and curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return 
            curr = curr.next
    def contains(self, key: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False          
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)