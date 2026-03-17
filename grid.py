

# grid.py : fonctions pour charger la grille et trouver les voisins
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


# get_neighbors(grid, x, y) : retourne les cases accessibles autour de (x,y)
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

if __name__ == "__main__":

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
   print("Arrivée :", goal)
   print("Voisins de start :", get_neighbors(grid, start[0], start[1]))
