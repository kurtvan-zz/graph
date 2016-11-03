#!/usr/bin/python
from graph import *
from prim_mazegen import *

class Maze:

    def __init__(self, width):
        self.show_ids = True;
        self.cells = []
        self.width = width
        self.num_cells = self.width * self.width

        self.adjGraph = Graph()
        self.pathGraph = Graph()

        for i in range(width*width):
            self.cells.append(i + 1)
            self.adjGraph.add_vertex(i + 1, 0)
            self.pathGraph.add_vertex(i + 1, 0)

        # populate the adjacency edge list
        for i in range(self.num_cells):

            # top edge
            if self.cells[i] - self.width >= 1:
                self.adjGraph.add_edge(self.cells[i], self.cells[i] - self.width)
            # right edge
            if (self.cells[i]) % self.width != 0 and self.cells[i] + 1 < self.num_cells: # if the cell to the right exists
                self.adjGraph.add_edge(self.cells[i], self.cells[i] + 1)
            # bottom edge
            if self.cells[i] + self.width <= self.num_cells:
                self.adjGraph.add_edge(self.cells[i], self.cells[i] + self.width)
            # left edge
            if ((self.cells[i] - 1) == 1 or ((self.cells[i] - 1) % (self.width + 1)) == 0) and self.cells[i] - 1 != 0:
                self.adjGraph.add_edge(self.cells[i], self.cells[i] - 1)

    def open_below(self, cell):
        if self.pathGraph.adjacent(cell, cell + self.width):
            return True
        else:
            return False

    def open_above(self, cell):
        if self.pathGraph.adjacent(cell, cell - self.width):
            return True
        else:
            return False

    def open_left(self, cell):
        if self.pathGraph.adjacent(cell, cell - 1):
            return True
        else:
            return False

    def open_right(self, cell):
        if self.pathGraph.adjacent(cell, cell + 1):
            return True
        else:
            return False

    def add_wall(self, x, y):
        self.pathGraph.remove_edge(x, y)

    def remove_wall(self, x, y):
        self.pathGraph.add_edge(x, y)

    def __str__(self):
        """
        Return a string representation of the Maze.
        """

        maze_output = ""
        maze_output += "------" * (self.width) + "\n" # top line

        # Generate a string to represent the maze
        # for all rows
        for i in range(self.width):

            # add the left wall
            maze_output += "|  "

            # for each cell in that row
            for j in range(self.width):

                index = self.width*i + j

                if self.show_ids:
                    maze_output += str(self.cells[index]) + " "*(3 - len(str(self.cells[index])))
                else:
                    maze_output += "   "


                #print the right wall if there is no gap there
                if not self.open_right(self.cells[index]):
                    maze_output += "|  "
                else:
                    maze_output += "   "

            # bring down to next line
            maze_output += "\n"

            # for each spot below a cell in that row
            for j in range(self.width):

                index = self.width*i + j

                if not self.open_below(self.cells[index]):
                    maze_output += "------"
                else:
                    maze_output += "      "

            maze_output += "\n"

        return maze_output
