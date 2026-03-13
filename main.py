
from grid import load_grid
from algorithms.greedy import greedy_search
from algorithms.astar import astar_search

grid,start,goal = load_grid("data/grid1.txt")

path_greedy = greedy_search(grid,start,goal)
print("Greedy path:",path_greedy)

path_astar = astar_search(grid,start,goal)
print("A* path:",path_astar)
