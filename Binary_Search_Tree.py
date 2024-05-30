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
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return results
    

    def DFS_Pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)

            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def DFS_Post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results
    
    def DFS_In_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)     
            if current_node.right is not None:
                traverse(current_node.right)
            

        traverse(self.root)
        return results


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


print(myTree.BFS())
print(myTree.DFS_Pre_order())
print(myTree.DFS_Post_order())
print(myTree.DFS_In_order())