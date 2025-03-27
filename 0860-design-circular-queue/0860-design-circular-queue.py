class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * k
        self.head = None
        self.tail = None
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():  
            return False
        if self.head is None and self.tail is None:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.k
        
        self.queue[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:  # Last element being dequeued
            self.head = None
            self.tail = None
        else:
            self.head = (self.head + 1) % self.k  # Move head forward
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        
    def isEmpty(self) -> bool:
        return self.head is None
        

    def isFull(self) -> bool:
        if self.head is None: 
            return False
        return (self.tail + 1) % self.k == self.head
