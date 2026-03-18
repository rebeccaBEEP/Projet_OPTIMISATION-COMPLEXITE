# Projet_OPTIMISATION-COMPLEXITE
#  Projet Optimisation — Recherche de chemin pour un robot

## 📋 Description

Application Python qui simule un robot se déplaçant dans une ville modélisée par une grille.
Le robot doit trouver le meilleur chemin entre un point de départ **(S)** et une destination **(G)**
en évitant les obstacles **(X)**.

Trois algorithmes sont implémentés et comparés :
- 🟢 **Algorithme Glouton** — rapide mais pas toujours optimal
- 🔵 **Algorithme A*** — optimal et fiable
- 🟣 **Algorithme Génétique** — flexible mais plus lent

---

## 🗺️ Modélisation de la grille
```
S 0 0 0 X 0
0 X 0 0 X 0
0 X 0 0 0 0
0 0 0 X 0 G
```

| Symbole | Signification |
|---------|--------------|
| S | Point de départ |
| G | Destination |
| 0 | Case libre |
| X | Obstacle |

---

##  Structure du projet
```
Projet_OPTIMISATION-COMPLEXITE/
├── grid.py        → Chargement de la grille et calcul des voisins
├── greedy.py      → Algorithme Glouton
├── astar.py       → Algorithme A*
├── genetic.py     → Algorithme Génétique
├── main.py        → Comparaison des trois algorithmes
├── grid1.txt      → Grille de test 1
├── grid2.txt      → Grille de test 2
├── grid3.txt      → Grille de test 3
└── README.md      → Documentation
```



---

##  Utilisation
```bash
python main.py
```

Le programme affiche un tableau comparatif des 3 algorithmes :
```
==================================================
             TABLEAU COMPARATIF
==================================================
  Algorithme      Longueur      Temps
--------------------------------------------------
  Glouton         X étapes     0.0001s
  A*              X étapes     0.0002s
  Génétique       X étapes     1.2345s
==================================================
```

---

##  Algorithmes

### 🟢 Algorithme Glouton
- Choisit toujours le voisin le plus proche du but
- Très rapide mais peut se bloquer
- N'utilise que l'heuristique : **h(n)**

### 🔵 Algorithme A*
- Combine coût réel et heuristique : **f(n) = g(n) + h(n)**
- Garantit le chemin optimal
- Utilise une file de priorité (heapq)

### 🟣 Algorithme Génétique
- S'inspire de l'évolution biologique
- Population de 100 chemins sur 200 générations
- Sélection → Croisement → Mutation
- Flexible mais résultat non garanti

---

##  Comparaison

| Algorithme | Chemin optimal | Vitesse     | Fiabilité |
|------------|---------------|-------------|--------------|
| Glouton           | ❌ |  ⚡ Très rapide | Moyenne |
| A*                | ✅ |    🔄 Moyen     | Excellente|
| Génétique         | ❌ |     🐢 Lent     | Variable |

---
