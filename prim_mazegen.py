#!/usr/bin/python
from graph import *
from maze import *
from random import *


def prim_mazegen(maze):
    """
    Mutate a newly initialized maze to carve a path from the start to
    the finish
    """

    # start in the top left, end in the bottom right
    start_point = 1
    end_point = maze.num_cells

    # this list will hold the cells that the algorithm has touched
    visited_cells = [start_point]

    # step further and further until the algorithm has visited
    # every cell
    while len(visited_cells) < maze.num_cells:
        step_maze(maze, visited_cells)


def step_maze(maze, visited_cells):
    """
    Increment the algorithm by one step. Generate frontier, choose a next cell
    and carve a path to it from one of the existing cells in visited_cells
    """

    # Generate the frontier and get our next cell from it
    next_cell = choice(get_frontier(maze, visited_cells))

    # This next cell is now part of the maze
    visited_cells.append(next_cell)

    # we need to pick a cell to connect to this new cell
    possible_links = []

    # pick connection cell that is adjacent to the new cell
    for cell in visited_cells:
        if cell in maze.adjGraph.get_neighbours(next_cell):
            possible_links.append(cell)

    # carve path between these 2 cells
    maze.pathGraph.add_edge(next_cell, choice(possible_links))


def get_frontier(maze, visited_cells):
    """

    """

    frontier = []

    for cell in visited_cells:
        # for every adjacent cell to this visited cell
        for neighbour in maze.adjGraph.get_neighbours(cell):
            # add it to the frontier if its newly discovered
            if neighbour not in frontier and neighbour not in visited_cells:
                frontier.append(neighbour)

    return frontier


if __name__ == "__main__":

    maze_width = 15

    new_maze = Maze(maze_width)
    new_maze.show_ids = False
    prim_mazegen(new_maze)

    print new_maze
