
from grid import load_grid
from greedy import greedy_search
from astar import astar_search
from genetic import genetic_algorithm
import time


grid,start,goal = load_grid("grid1.txt")

print(f"\nDépart : {start}")
print(f"Arrivée : {goal}")



# ── Glouton ──
t0 = time.perf_counter()
path_greedy = greedy_search(grid, start, goal)
t_greedy = time.perf_counter() - t0

# ── A* ──
t0 = time.perf_counter()
path_astar = astar_search(grid, start, goal)
t_astar = time.perf_counter() - t0

# ── Génétique ──
t0 = time.perf_counter()
path_genetic = genetic_algorithm(grid, start, goal)
t_genetic = time.perf_counter() - t0

# Tableau comparatif

print("\n" + "="*50)
print(f"  {'TABLEAU COMPARATIF':^46}")
print("="*50)
print(f"  {'Algorithme':<15} {'Longueur':>10} {'Temps':>10}")
print("-"*50)

for name, path, t in [
    ("Glouton",   path_greedy,  t_greedy),
    ("A*",        path_astar,   t_astar),
    ("Génétique", path_genetic, t_genetic),
]:
    length = f"{len(path)-1} étapes" if path else "Échec"
    print(f"  {name:<15} {length:>10} {t:>10.4f}s")

print("="*50)
