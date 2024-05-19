class NewNode:
    def __init__(self,value):
        self.value=value
        self.next = None


class Queue:
    def __init__(self,value):
        new_node = NewNode(value)
        self.first = new_node
        self.last = new_node
        self.length=1

    def printQueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def Enqueue(self,value):
        new_node = NewNode(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length+=1
    
    def Dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length-=1

        return temp

myQueue = Queue(4)
myQueue.printQueue()
print("\n")
myQueue.Enqueue(5)
myQueue.printQueue()
print("\n")
myQueue.Dequeue()
myQueue.printQueue()
print("\n")
myQueue.Dequeue()
myQueue.printQueue()
print("\n")