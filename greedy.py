def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_neighbors(grid, x, y):
    neighbors = []
    directions = [(0,-1), (0,1), (-1,0), (1,0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            if grid[ny][nx] != 'X':
                neighbors.append((nx, ny))
    return neighbors

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
grid = [
    ['S', '0', '0', '0', 'X', '0'],
    ['0', 'X', '0', '0', 'X', '0'],
    ['0', 'X', '0', '0', '0', '0'],
    ['0', '0', '0', 'X', '0', 'G']
]
start = (0, 0)
goal = (5, 3)

path = greedy_search(grid, start, goal)
print("Chemin Greedy :", path)