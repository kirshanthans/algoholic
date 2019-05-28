#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.data = data
        self.l    = None
        self.r    = None

class Tree:
    def __init__(self, arr):
        self.root = self.build(arr, 0, len(arr)) 

    def build(self, arr, s, e):
        # construct a balanced binary tree
        if s == e:
            return None

        p = (s+e) // 2
        n = Node(arr[p])
        n.l = self.build(arr, s, p)
        n.r = self.build(arr, p+1, e)
        return n

    def traverse(self, n):
        # traverse a binary tree
        if n == None:
            return

        self.dfs(n.l)
        print n.data
        self.dfs(n.r)

def main():
    t = Tree(range(10))
    t.traverse(t.root)

if __name__ == "__main__":
    main()

