#!/usr/bin/python

class FreeTree:
    def __init__(self, v):
        self.vertices = v
        self.edges = {}

    def add_edge(self, u, v):
        assert u in self.vertices
        assert v in self.vertices
        # add u->v
        if u in self.edges:
            self.edges[u].append(v)
        else:
            self.edges[u] = [v]
        # add v->u
        if v in self.edges:
            self.edges[v].append(u)
        else:
            self.edges[v] = [u]
