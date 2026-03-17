
# les imports

from grid import load_grid # pour charger la grille depuis un fichier
from greedy import greedy_search # algorithme glouton
from astar import astar_search # algorithme A*
from genetic import genetic_algorithm # algorithme génétique
from visualization import show_all # pour afficher les chemins trouvés pour les différents algorithmes
import time # pour mesurer le temps d'exécution de chaque algorithme


# menu pour choisir la grille à tester
def choisir_grille():
    print("\n" + "="*40)
    print("       ROBOT - RECHERCHE DE CHEMIN")
    print("="*40)
    print("  1 - grid1.txt  (grille simple)")
    print("  2 - grid2.txt  (grille moyenne)")
    print("  3 - grid3.txt  (grille difficile)")
    print("="*40)
    choix = input("  Ton choix (1/2/3) : ")
    grilles = {
        "1": "grid1.txt",
        "2": "grid2.txt",
        "3": "grid3.txt"
    }
    if choix in grilles:
        return grilles[choix]
    else:
        print("  Choix invalide → grid1.txt par défaut")
        return "grid1.txt"

# main() : point d'entrée du programme
def main():
    while True:
        fichier = choisir_grille()
        grid, start, goal = load_grid(fichier)
        print(f"\n  Départ : {start}  |  Arrivée : {goal}")

        t0 = time.perf_counter()
        path_greedy = greedy_search(grid, start, goal)
        t_greedy = time.perf_counter() - t0

        t0 = time.perf_counter()
        path_astar = astar_search(grid, start, goal)
        t_astar = time.perf_counter() - t0

        print("\n   Génétique en cours...")
        t0 = time.perf_counter()
        path_genetic = genetic_algorithm(grid, start, goal)
        t_genetic = time.perf_counter() - t0
        
        
        print(f"\n  Glouton  : {path_greedy}")
        print(f"  A*       : {path_astar}")
        print(f"  Génétique: {path_genetic}")


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
            length = f"{len(path)-1} etapes" if path else "Echec"
            print(f"  {name:<15} {length:>10} {t:>10.4f}s")
        print("="*50)

        show_all(grid, path_greedy, path_astar, path_genetic)

        rejouer = input("\n  Essayer une autre grille ? (o/n) : ")
        if rejouer.lower() != "o":
            print("\n  Au revoir ! 👋")
            break
        


main()