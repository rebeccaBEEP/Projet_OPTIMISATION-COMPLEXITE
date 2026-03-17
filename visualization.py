import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def draw_grid(ax, grid, path, title):
    """Affiche une grille avec son chemin sur un axe matplotlib."""

    path_set = set(path) if path else set()
    nrows = len(grid)
    ncols = len(grid[0])

    # Créer une image vide (hauteur x largeur x RGB)
    img = np.zeros((nrows, ncols, 3))

    for y in range(nrows):
        for x in range(ncols):
            cell = grid[y][x]

            if cell == 'X':
                img[y, x] = [0.2, 0.2, 0.2]   # ⬛ obstacle
            elif cell == 'S':
                img[y, x] = [0.2, 0.8, 0.2]   # 🟩 départ
            elif cell == 'G':
                img[y, x] = [0.9, 0.2, 0.2]   # 🟥 arrivée
            elif (x, y) in path_set:
                img[y, x] = [0.2, 0.5, 0.9]   # 🟦 chemin
            else:
                img[y, x] = [0.9, 0.9, 0.9]   # ⬜ case libre

    ax.imshow(img)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.axis('off')

def show_all(grid, path_greedy, path_astar, path_genetic):
    """Affiche les 3 grilles côte à côte."""

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Comparaison des algorithmes", fontsize=14, fontweight='bold')

    # Longueur de chaque chemin
    l1 = f"{len(path_greedy)-1} étapes"  if path_greedy  else "Échec"
    l2 = f"{len(path_astar)-1} étapes"   if path_astar   else "Échec"
    l3 = f"{len(path_genetic)-1} étapes" if path_genetic else "Échec"

    draw_grid(axes[0], grid, path_greedy,  f"Glouton\n{l1}")
    draw_grid(axes[1], grid, path_astar,   f"A*\n{l2}")
    draw_grid(axes[2], grid, path_genetic, f"Génétique\n{l3}")

    # Légende
    legend = [
        mpatches.Patch(color=[0.2, 0.8, 0.2], label='Départ (S)'),
        mpatches.Patch(color=[0.9, 0.2, 0.2], label='Arrivée (G)'),
        mpatches.Patch(color=[0.2, 0.5, 0.9], label='Chemin'),
        mpatches.Patch(color=[0.2, 0.2, 0.2], label='Obstacle (X)'),
        mpatches.Patch(color=[0.9, 0.9, 0.9], label='Case libre'),
    ]
    fig.legend(handles=legend, loc='lower center', ncol=5, fontsize=10)

    plt.tight_layout()
    plt.show()