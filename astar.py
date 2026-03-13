import heapq
from grid import get_neighbors

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar_search(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, 0, start))  # ✅ 3 valeurs
    came_from = {}
    g_score = {start: 0}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:          # ✅ au bon endroit
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path              # ✅ return dans le if

        for neighbor in get_neighbors(grid, current[0], current[1]):
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                h = heuristic(neighbor, goal)
                f = tentative_g + h
                heapq.heappush(open_list, (f, tentative_g, neighbor))
                came_from[neighbor] = current

    return None  # ✅ aucun chemin trouvé


# TEST - Grille définie directement dans le code
grid = [
    ['S', '0', '0', '0', 'X', '0'],
    ['0', 'X', '0', '0', 'X', '0'],
    ['0', 'X', '0', '0', '0', '0'],
    ['0', '0', '0', 'X', '0', 'G']
]

start = (0, 0)
goal  = (5, 3)

path = astar_search(grid, start, goal)
print("Chemin A* :", path)