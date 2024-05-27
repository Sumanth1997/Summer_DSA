class Graph:
    def __init__(self):
        self.adj_list = {}


    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        
        return False
    
    def print_vertex(self):
        for vertex in self.adj_list:
            print(vertex, ' : ',self.adj_list[vertex])

    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
            

myGraph = Graph()
myGraph.add_vertex(2)
myGraph.add_vertex(4)
myGraph.add_vertex(6)
myGraph.print_vertex()
myGraph.add_edge(2,4)
myGraph.add_edge(4,6)
myGraph.add_edge(2,6)

myGraph.print_vertex()

# myGraph.remove_edge(4,6)
# myGraph.remove_edge(2,6)
# myGraph.remove_edge(2,6)

myGraph.remove_vertex(6)
myGraph.print_vertex()
