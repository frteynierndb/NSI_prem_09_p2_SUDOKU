# projet-NSi-SUDOKU
proposition de projet au chef de projet.
10/12/2021 : validation : structure de donnée liste pour chaque ligne avec dictionnaire pour toute les valeurs avec "content"{erase, noterase}
documentation sur comment creer une grille + interface graphique.
lein utiles : https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
 François Teynier et Alexandre valdevit
 
 ce projet consite à faire un sudoku et il sera continué sur le 3 eme projet afin d'y apporté des modifications, améliorations et différents ajouts
 
 c'est un sudoku donc un jeu consistant à remplir une grille 9*9 tout en faisaisant attention à ne pas avoir le même chiffre sur une même colonne ou ligne
 
 ce projet est passé part différentes étapes:
 -tout d'abord l'écriture des lignes de code lié à l'interface graphique
 -ensuite une longue reflexion avec le chef des projets a été réalisé sur un des problèmes du projet ce qui a mené à un report de cette fonctionnalité
 -puis le travail à été réparti entre les deux acteurs du projets:
    - Alexandre s'occupe de la grille ainsi que le début du Read.me
    - François réalise les fonctions correspondantes aux actions dans le sudoku ainsi que la partie technique pour le read.me concernant les précisions
    
 GRILLE: 45l
 la grille est une liste appelé lvl1 (des niveéaux différents seront rajouté au fur et à mesure), cette lo*iste contient 9 liste appélé respectivement l1, l2... pour les différentes lignes de la grille, les cases soont des boutons généré grâce à une variable i qui traverse la lioste afin de donner la valeur grâce à la commande l1[i], ainsi que la colonne avec i, la ligne étant donné grâce au nom de la liste. les listes  sont composés d'éléments vide pour les cases non remplies.
 
Il y a ensuite une deuxième liste lvl1c qui correspond à la correction de la grille, elle sert de référence pour la fonction check qui sera expliquée plus tard.

MAIN: 34l
au début du programme nous avons attribué au ligne (row) des boutons une varaible x et une variable y pour les colones des boutons 
le main est constitué de 3 fonctions:
-check--> elle sert à comparer les valeurs sur une même position des listes lvl1 et lvl1c , si il y a une différence, un message apparait indiquant l'erreur.elle prend en compte lvl1 et lvl1c ainsi que x et y
-end_game--> c'est la fonction qui quand le sudoku sera terminé, cet-à-dire qu'il n'y a plus d'éléments vide dans les sous liste de la liste de la grille, vous enverra un message de fin, vous pourrez donc ensuite quitter le jeu. elle prend en compte la liste lvl1
-change-val--> c'est la fonction qui correspond à l'évènement d'un clique gauche qui permet de changer la valeur d'une case, elle applique ainsi les fonction check puis end_game
 
INTERFACE: 26l

cette partie du programme est très majoritairement tiré du site dont le lien est affiché en haut de ce read me, elle constitue l'interface graphique du sudoku où les fonctions ont été insipré et modifié : l11_13 pour le menu des niveaux; l16 : (def callback) pour quitter le jeu: elle permet de faire un choix entre vraiment quitter ou finalement rester. l23 permet d 'executer callback

vous n'aurez besoin que de tkinter pour faire fonctionner le programme


Difficultés:
nous avons été confrontés à plusieurs difficultés comme pour la génération de la grille que nous ne pouvons paz encore automatiser et rendre autonome, mais al plus grande difficulté est le fait que nous ne sommes pas arrivés a relier les fichiers entre eux , ce quio induit que nous n'avons pas pu essayer le fonctionnement de notre programme, et surtout le fichier main. malgré une recherche et plusieurs essais

nous esperont pouvoir régler ce problème afin de proposer une meilleure expérience à l'utilisateur.
