#!/usr/bin/python
from graph import *
from maze import *
from random import *


def prim_mazegen(maze):
    """
    Mutate a newly initialized maze to
    """

    # start with random cell
    start_point = 1
    end_point = 100
    visited_cells = [start_point]

    while len(visited_cells) < maze.num_cells:
        step_maze(maze, visited_cells)


def step_maze(maze, visited_cells):

    next_cell = choice(get_frontier(visited_cells, maze))
    visited_cells.append(next_cell)

    possible_links = []

    for cell in visited_cells:
        if cell in maze.adjGraph.get_neighbours(next_cell):
            possible_links.append(cell)



    maze.pathGraph.add_edge(next_cell, choice(possible_links))


def get_frontier(visited_cells, maze):

    frontier = []

    for cell in visited_cells:
        for neighbour in maze.adjGraph.get_neighbours(cell):
            if neighbour not in frontier and neighbour not in visited_cells:
                frontier.append(neighbour)

    return frontier



if __name__ == "__main__":

    new_maze = Maze(10)
    new_maze.show_ids = False
    prim_mazegen(new_maze)

    print new_maze
