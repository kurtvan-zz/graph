# Graph
A basic set of undirected graph methods in Python to support creation of graphs and execution of graph algorithms.

This implementation uses an adjacency list to store graph verticies, although there are no assumptions made about the sparseness of the graph.


## Maze example
Included in this repository is an example implementation of this graph class that generates random mazes using prim's algorithm

```
------------------------------------------------------------
|           |                 |                             |  
      ------      ------------                              
|                       |     |     |     |     |     |     |  
      ------      ------                  ------------      
|     |     |                       |           |           |  
            ------            ------      ------------      
|     |           |     |           |           |           |  
                        ------      ------------------------
|           |     |           |           |                 |  
            ------------------      ------------      ------
|     |           |     |     |     |           |           |  
                              ------------                  
|     |     |           |           |                 |     |  
      ------                  ------            ------      
|           |     |                 |     |     |           |  
      ------      ------      ------      ------------------
|     |     |     |                 |                       |  
                  ------                  ------------------
|           |     |           |                             |  
------------------------------------------------------------
```
