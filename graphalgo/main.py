#!/usr/bin/python
from collections import deque

class Graph:
    def __init__(self):
        self.vertices = set([])
        self.edges    = {}

    def addVertex(self, v):
        self.vertices.add(v)
        self.edges[v] = list([])

    def addEdge(self, v, u):
        assert v in self.vertices and u in self.vertices
        self.edges[v].append(u)

    def dfs(self, start):
        # assert start node is a valid vertex
        assert start in self.vertices
        # keep track of visited nodes
        visited = set([])
        # stack for the dfs
        stack   = list([])
        # pushing to the stack
        stack.append(start)
        # output
        order = list([])
        # traversal
        while stack:
            curr_v = stack.pop()
            if curr_v in visited:
                continue
            order.append(curr_v) #computation
            visited.add(curr_v)
            neighbors = self.edges[curr_v]
            for n in neighbors:
                stack.append(n)
        # return visited order
        return order
    
    def bfs(self, start):
        # assert start node is a valid vertex
        assert start in self.vertices
        # keep track of visited nodes
        visited = set([])
        # stack for the dfs
        queue   = deque([])
        # pushing to the queue 
        queue.append(start)
        # output
        order = list([])
        # traversal
        while queue:
            curr_v = queue.popleft()
            if curr_v in visited:
                continue
            order.append(curr_v) #computation
            visited.add(curr_v)
            neighbors = self.edges[curr_v]
            for n in neighbors:
                queue.append(n)
        # return visited order
        return order

    def visit(self, node, order):
        if node in self.perm_mark: # reached node with no child visit 
            return True
        if node in self.temp_mark: # cycle (i.e. detection of back edge) 
            return False
        self.temp_mark.add(node)
        neighbors = self.edges[node]
        for v in neighbors:
            status = self.visit(v, order) # performing dfs
            if status is False:
                return False
        self.temp_mark.remove(node)
        self.perm_mark.add(node) 
        order.appendleft(node) # adding node to the topological order
        
    def topOrder(self):
        self.perm_mark = set([]) # permanent marking
        self.temp_mark = set([]) # temporary marking
        # unmarked vertices
        no_mark   = list(self.vertices) 
        
        order = deque([]) # topological order

        while no_mark:
            node = list(no_mark).pop()
            status = self.visit(node, order)
            if status is False:
                return None
            no_mark = self.vertices - self.perm_mark - self.temp_mark
        # return the topological order
        return list(order)
        
if __name__ == "__main__":
    G = Graph()
    #vertices
    G.addVertex("A")
    G.addVertex("B")
    G.addVertex("C")
    G.addVertex("D")
    G.addVertex("E")
    G.addVertex("F")
    G.addVertex("G")
    #edges
    G.addEdge("A", "B")
    G.addEdge("A", "C")
    G.addEdge("B", "C")
    G.addEdge("B", "D")
    G.addEdge("B", "E")
    G.addEdge("D", "E")
    G.addEdge("C", "F")
    G.addEdge("C", "G")
    G.addEdge("F", "G")
    #dfs
    print "Depth First Traversal"
    dfo = G.dfs("A")
    print dfo
    #bfs
    print "Breath First Traversal"
    bfo = G.bfs("A")
    print bfo
    #topological sorting
    print "Topological Sorting"
    tpo = G.topOrder()
    if tpo is None:
        print "Graph has a cycle"
    else:
        print tpo










