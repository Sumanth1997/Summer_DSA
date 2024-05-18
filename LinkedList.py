print("Linked List")

class NewNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self,value):
        new_node = NewNode(value)
        self.value = value
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = NewNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = NewNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre=temp
            temp=temp.next        
        self.tail = pre
        self.tail.next = None
        self.length-=1

        return temp
    
    def get(self,index):
        if index < 0 or index > self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = NewNode(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1

        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.tail = None

        return temp
    
    def set(self,index,value):
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        
        return False

    def remove(self,index):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length-=1

        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


        
       



l1 = LinkedList(4)
l1.append(3)
l1.prepend(5)
l1.printList()
print("\n")
# l1.pop()
l1.printList()
print("\n")
print(l1.get(2).value)
print("\n")
l1.insert(2,10)
l1.printList()
print("\n")
l1.set(1,50)
l1.printList()
print("\n")
l1.pop_first()
l1.printList()
print("\n")
# l1.remove(2)
l1.printList()
print("\n")
l1.reverse()
l1.printList()

        