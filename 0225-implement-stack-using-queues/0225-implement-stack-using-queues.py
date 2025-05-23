class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        return

    def pop(self) -> int:
        temp = self.queue[-1]
        self.queue = self.queue[:-1]
        return temp
        

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False    
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()