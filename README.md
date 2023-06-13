INTRODUCTION :

Après une acquisition du cours de technique de compilation, moi, tant qu'étudiant en 2eme année de la filière DATA AND SOFTWARE ENGINEERING, j'ai réalisé ce travail qui consiste à faire un micro compilateur basé sur le langage PYTHON qui se compose de quatre phases dépendantes

1-Analyse lexicale
2-Analyse syntaxique
3-Analyse sémantique
4-Interpréteur
                                          


# C'EST QUOI UN COMPILATEUR ?

Un compilateur est tout simplement un programme qui lit un fichier texte de code source écrit dans un langage de programmation et produit du code
assembleur pour l’architecture de l'ordinateur cible. Il est généralement divisé en plusieurs modules, qui sont décrits dans le diagramme de flux de données à droite. Ce diagramme décrit toutes les étapes nécessaires pour convertir un code source de langage de haut niveau en code assembleur pour une machine cible. Tous les modules utilisent une structure de données partagée appelée Tables des symboles (nous en parlerons plus tard) et ont leurs propres routines de gestion des
erreurs.
Voici une image qui resume tout cela: ![Alt text](img/compila.jpg)

# PHASE ANALYSEUR LEXICALE:
La toute première étape consiste à diviser le code du programme d'entrée en un groupe d'unités sémantiquement significatives appelées Tokens. Intuitivement, chaque mot et symbole du code source transmet une signification et nous voulons extraire ces Unités lexicales dans une liste ordonnée pour un traitement ultérieur. C'est aussi le travail de l'analyseur lexical de se débarrasser des commentaires de code. La sortie de l'analyseur lexical pour notre exemple de programme ressemblerait à celle afficher dans l’image.     #![Alt text](img/compila-1.jpg)
Ci joint un texte d'éxécution:   #![Alt text](img/compila-2.jpg)
En cliquant sur Analyse lexicale, le résultat s'affiche directement sur le résultat;

# PHASE ANALYSEUR SYNTAXIQUE:
L'analyseur syntaxique (Parser) est le cœur du compilateur. Il appelle les autres modules, tels que l'analyseur lexical pour récupérer les unités lexicales suivant, et agit comme la boucle principale du compilateur. Il reçoit le flux de tokens du parser en tant qu'entrée et
produit une structure de données appelée arbre syntaxique (arbre de syntaxe abstraite) en tant que sortie.
Voici une image démontrant le test sur l'interface graphique:
#![Alt text](img/image.png)

# PHASE ANALYSEUR SEMANTIQUE:
L’analyseur sémantique fait principalement des rapports d'erreurs pour aider le programmeur à corriger ses erreurs. En plus de cela, il met à jour les types d'identificateurs dans la table de symboles, ce qui est une connaissance précieuse pour le générateur de code plus tard.
La partie de vérification des erreurs n'est pas obligatoire, mais fortement recommandée car le comportement du programme compilé peut être indéfini si, par exemple, nous permettons de passer plus d'arguments à une fonction qu'elle n'est conçue pour gérer. Nous finissons
probablement par écraser quelque chose dans la mémoire et ce n'est généralement pas un bon signe pour un comportement correct du programme.
Voici des exemples des errurs générées: #![Alt text](img/compila-3.jpg)
#![Alt text](img/compila-4.jpg)


# CONCLUSION :
Ce projet m'a permis de comprendre parfaitement la chaine de
compilation d’un code est nous a donné l’occasion de découvrir
énormément de problèmes, de les résoudre au fil du temps et de
lever certaines ambiguïté.

L’expérience était très intéressante non seulement elle m'a
permis de passer de la partie théorique à la partie pratique mais
aussi de s’entrainer et de m'ouvrir la porte vers le monde infini de programmation.                  #python #tkinter
