class MyLinkedList:

    def __init__(self):
        self.val = -1
        self.next = None
        self.head = None
        
    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next 
            count +=1  
        return -1

    def addAtHead(self, val: int) -> None:
        new_head = MyLinkedList()
        new_head.val = val
        new_head.next = self.head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next  

        new_tail = MyLinkedList()
        new_tail.val = val
        curr.next= new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return

        curr = self.head
        count = 0
        while curr and count<index-1:
            curr = curr.next  
            count +=1  
        if not curr:
            return

        new_node = MyLinkedList()
        new_node.val = val
        new_node.next= curr.next
        curr.next = new_node


        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return 
        curr = self.head
        count = 0
        while curr and count<index-1:
            curr = curr.next   
            count +=1 
        if curr and curr.next:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)