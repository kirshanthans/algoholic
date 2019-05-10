#!/usr/local/bin/python
from collections import deque

def dfs(vertices, edges, start):
    # assert start node is a valid vertex
    assert start in vertices
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
        neighbours = edges[curr_v]
        for n in neighbours:
            stack.append(n)

def bfs(vertices, edges, start):
    # assert start node is a valid vertex
    assert start in vertices
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
        neighbours = edges[curr_v]
        for n in neighbours:
            queue.append(n)






