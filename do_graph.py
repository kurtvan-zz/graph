#!/usr/bin/python
from graph import *

if __name__ == "__main__":

    g1 = Graph()
    g1.add_vertex(1, 1)
    g1.add_vertex(2, 2)
    g1.add_vertex(3, 3)
    g1.add_vertex(4, 4)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)

    print g1.vertex_values

    print "neighbours of id = 1: " + str(g1.get_neighbours(1))
    print g1
