class NewNode:
    def __init__(self,value):
        self.value = value
        self.next=None
        
class Stack:
    def __init__(self,value):
        new_node = NewNode(value)
        self.top = new_node
        self.height=1 

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = NewNode(value)
        if self.height == 0:
            self.top = new_node
        else:    
            new_node.next = self.top
            self.top = new_node
        self.height+=1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height-=1

        return temp

myStack = Stack(2)
myStack.printStack()
print("\n")
myStack.push(3)
myStack.printStack()
print("\n")
myStack.pop()
myStack.printStack()
print("\n")
myStack.pop()
myStack.printStack()
print("\n")
myStack.printStack()
print("\n")
