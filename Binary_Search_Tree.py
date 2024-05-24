class NewNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = NewNode(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
            
                temp = temp.right

    def contains(self,value):
        temp = self.root
        while(temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False


myTree = BinarySearchTree()
print(myTree.root)
myTree.insert(47)
myTree.insert(21)
myTree.insert(76)
myTree.insert(18)
myTree.insert(27)
myTree.insert(52)
myTree.insert(82)


print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)


print(myTree.contains(18))
print(myTree.contains(50))
