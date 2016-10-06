#!/usr/bin/python

class Graph:
    """
    A class to encompass an undirected graph data structure

    """

    def __init__(self):
        self.adjacency_list = {} # to hold the edges
        self.num_edges = 0
        self.num_vertices = 0
        self.vertex_values = {}

    # The following methods return data about specific verticies

    def adjacent(self, x, y):
        if y in self.adjacency_list[x]:
            return True

        return False

    def get_neighbours(self, id):
        if id in self.adjacency_list:
            return self.adjacency_list[id]
        else:
            return -1

    # The following methods modify the structure of the graph

    def add_vertex(self, id, value):
        if id not in self.adjacency_list:
            self.vertex_values[id] = value
            self.adjacency_list[id] = []
            self.num_vertices += 1
            return 0
        else:
            return 1

    def remove_vertex(self, id):
        if self.adjacency_list.pop(id, None) != None:
            for node in self.adjacency_list:
                if id in self.adjacency_list[node]: #vertex exists so delete it
                    self.adjacency_list[node].remove(id)
                    self.verticies.pop(key, 1)
            return 0
        else:
            return 1

    def add_edge(self, x, y):
        if y not in self.adjacency_list[x]:
            self.adjacency_list[x].append(y)
        if x not in self.adjacency_list[y]:
            self.adjacency_list[y].append(x)
        return 0

    def remove_edge(self, x, y):
        if y in self.adjacency_list[x]:
            self.adjacency_list[x].remove(y)
        else:
            return 1
        if x in self.adjacency_list[y]:
            self.adjacency_list[y].remove(x)
        else:
            return 1

        return 0

    # Setter and getter for verticies
    def get_vertex_value(self, id):
        return self.vertex_values[id]

    def set_vertex_value(self, id, new_value):
        if id in self.vertex_values:
            return self.vertex_values[key]
        else:
            return 1

    # Method prototypes (Not implemented yet)
    def get_edge_value(self, x, y):
        pass
    def set_edge_value(self, x, y, new_value):
        pass

    # string conversion: just return the adjacency list
    def __str__(self):
        return str(self.adjacency_list)
