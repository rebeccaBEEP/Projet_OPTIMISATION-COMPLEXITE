

import random
from grid import get_neighbors

# ───────────────────────────────────────
# CONSTANTES
# ─────────────────────────────────────────

MOVES = [(1,0), (-1,0), (0,-1), (0,1)]  # D, G, H, B
CHROMOSOME_LENGTH = 20
POPULATION_SIZE   = 100
GENERATIONS       = 200
MUTATION_RATE     = 0.1

# ─────────────────────────────────────────
# MORCEAU 1 — POPULATION INITIALE
# ─────────────────────────────────────────

def create_population():
    """Crée 100 chromosomes aléatoires."""
    return [
        [random.randint(0, 3) for _ in range(CHROMOSOME_LENGTH)]
        for _ in range(POPULATION_SIZE)
    ]

# ─────────────────────────────────────────
# MORCEAU 2 — FITNESS
# ─────────────────────────────────────────

def heuristic(a, b):
    """Distance de Manhattan."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def decode_chromosome(chromosome, start, grid):
    """
    Convertit une séquence de mouvements en positions.
    Si un mouvement mène à un obstacle ou hors grille → on reste sur place.
    """
    path = [start]
    current = start
    for gene in chromosome:
        dx, dy = MOVES[gene]
        nx, ny = current[0] + dx, current[1] + dy
        # Vérifier que le mouvement est valide
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            if grid[ny][nx] != 'X':
                current = (nx, ny)
        path.append(current)
    return path

def fitness(chromosome, start, goal, grid):
    """
    Évalue la qualité d'un chromosome.
    → Plus on est proche de G, meilleure est la fitness.
    → Bonus si on atteint G (chemin court favorisé).
    """
    path = decode_chromosome(chromosome, start, grid)
    final_pos = path[-1]
    dist = heuristic(final_pos, goal)

    # Bonus si le chemin atteint G
    if goal in path:
        steps = path.index(goal)
        return 1000 - steps   # plus court = meilleur score

    return -dist  # sinon pénalité selon distance restante

# ─────────────────────────────────────────
# MORCEAU 3 — SÉLECTION
# ─────────────────────────────────────────

def selection(population, start, goal, grid):
    """
    Évalue tous les chromosomes et garde les 50% meilleurs.
    """
    # Calculer le score de chaque chromosome
    scored = [
        (fitness(chrom, start, goal, grid), chrom)
        for chrom in population
    ]

    # Trier du meilleur au moins bon
    scored.sort(key=lambda x: x[0], reverse=True)

    # Garder seulement les 50% meilleurs
    survivors = [chrom for _, chrom in scored[:POPULATION_SIZE // 2]]
    return survivors, scored[0]  # survivants + meilleur score

# ─────────────────────────────────────────
# MORCEAU 4 — CROISEMENT ET MUTATION
# ─────────────────────────────────────────

def crossover(parent1, parent2):
    """
    Croisement en un point :
    enfant = début de parent1 + fin de parent2
    """
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    #
    #  parent1 : [0, 3, 1, 2, | 0, 3, 3, 1]
    #  parent2 : [2, 2, 0, 1, | 3, 0, 2, 1]
    #                  ↑ point de coupe
    #  enfant  : [0, 3, 1, 2,   3, 0, 2, 1]
    #
    return parent1[:point] + parent2[point:]

def mutation(chromosome):
    """
    Modifie aléatoirement certains gènes selon MUTATION_RATE.
    """
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = random.randint(0, 3)
    return chromosome

# ─────────────────────────────────────────
# MORCEAU 5 — BOUCLE PRINCIPALE
# ─────────────────────────────────────────

def genetic_algorithm(grid, start, goal):
    """
    Boucle principale de l'algorithme génétique.
    """
    # 1. Population initiale
    population = create_population()
    best_path = None

    for generation in range(GENERATIONS):

        # 2. Sélection des meilleurs
        survivors, (best_score, best_chrom) = selection(population, start, goal, grid)

        # Sauvegarder le meilleur chemin trouvé
        path = decode_chromosome(best_chrom, start, grid)
        if goal in path:
            best_path = path[:path.index(goal) + 1]

        # 3. Croisement — recréer une population complète
        new_population = survivors[:]   # garder les survivants
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(survivors)
            parent2 = random.choice(survivors)
            child = crossover(parent1, parent2)
            new_population.append(child)

        # 4. Mutation sur toute la population
        population = [mutation(chrom) for chrom in new_population]

    return best_path


# ─────────────────────────────────────────
# TEST
# ─────────────────────────────────────────

if __name__ == "__main__":
    grid = [
        ['S', '0', '0', '0', 'X', '0'],
        ['0', 'X', '0', '0', 'X', '0'],
        ['0', 'X', '0', '0', '0', '0'],
        ['0', '0', '0', 'X', '0', 'G']
    ]
    start = (0, 0)
    goal = (5, 3)

    path = genetic_algorithm(grid, start, goal)
    print("Chemin Génétique :", path)