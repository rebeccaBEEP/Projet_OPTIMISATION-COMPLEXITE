from grid import get_neighbors

#heuristic(a, b) : distance de Manhattan entre a et b

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])



# greedy_search(grid, start, goal) : implémente l'algorithme glouton

def greedy_search(grid, start, goal): 
    path = [start]
    current = start
    visited = set()
    visited.add(start)
    while current != goal:
        neighbors = get_neighbors(grid, current[0], current[1])
        neighbors = [n for n in neighbors if n not in visited]
        if not neighbors:
            return None
        current = min(neighbors, key=lambda n: heuristic(n, goal))
        visited.add(current)
        path.append(current)
    return path 

# TEST

if __name__ == "__main__":
    grid = [
        ['S', '0', '0', '0', 'X', '0'],
        ['0', 'X', '0', '0', 'X', '0'],
        ['0', 'X', '0', '0', '0', '0'],
        ['0', '0', '0', 'X', '0', 'G']
    ]
    start = (0, 0)
    goal = (5, 3)
    path = greedy_search(grid, start, goal)
    print("Chemin glouton :", path)