def load_grid(file):
    grid=[]
    start=None
    goal=None
    with open(file) as f:
        for y,line in enumerate(f):
            row=line.strip().split()
            for x,val in enumerate(row):
                if val=="S":
                    start=(x,y)
                if val=="G":
                    goal=(x,y)
            grid.append(row)
    return grid,start,goal

def get_neighbors(grid, x, y):
    neighbors = []
    directions = [(0,-1), (0,1), (-1,0), (1,0)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            if grid[ny][nx] != 'X':
                neighbors.append((nx, ny))
    
    return neighbors

# TEST - Grille définie directement dans le code
grid = [
    ['S', '0', '0', '0', 'X', '0'],
    ['0', 'X', '0', '0', 'X', '0'],
    ['0', 'X', '0', '0', '0', '0'],
    ['0', '0', '0', 'X', '0', 'G']
]
start = (0, 0)
goal = (5, 3)

print("Grille chargée :")
for row in grid:
    print(row)
print("Départ :", start)
print("Arrivée :", goal)
print("Voisins de start :", get_neighbors(grid, start[0], start[1]))