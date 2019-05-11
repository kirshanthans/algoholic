#!/usr/local/bin/python
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
        # traversal
        while stack:
            curr_v = stack.pop()
            if curr_v in visited:
                continue
            # computation
            visited.add(curr_v)
            neighbours = self.edges[curr_v]
            for n in neighbours:
                stack.append(n):
    
    def bfs(self, start):
        # assert start node is a valid vertex
        assert start in self.vertices
        # keep track of visited nodes
        visited = set([])
        # stack for the dfs
        queue   = deque([])
        # pushing to the stack
        queue.append(start)
        # traversal
        while queue:
            curr_v = queue.popleft()
            if curr_v in visited:
                continue
            #computation
            visited.add(curr_v)
            neighbours = self.edges[curr_v]
            for n in neighbours:
                queue.append(n)

    def topOrder(self):
        pass

if __name__ == "__main__":
    





