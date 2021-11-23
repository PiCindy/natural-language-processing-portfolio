# ProjetTal Groupe B : Détection de la langue d'un texte

Auteurs : *GALLIENNE Romane, PEREIRA Cindy*


**Avant de lancer les différents programmes, se placer dans le répertoire src du projet.**
**Pour exécuter la Detection, il est absolument nécessaire d'entrer un n. Pour les autres fonctionnalités du programme, si n n'est pas précisé, 2 est pris par défaut.**
*cd L3GroupeBDetection/src*


**Partie 0 facultative : Vectorisation des dictionnaires**

Lancer le programme avec le fichier VectorisationCorpus.py
Argument facultatif : n (taille des n-grammes)
Exemple d'utilisation :
*python3 VectorisationCorpus.py 5*


**Partie 1 : Détection de la langue d'un texte**

Lancer le programme avec le fichier Detection.py
Arguments nécessaires : n (taille des n-grammes), texte (nom d'un fichier au format txt ou texte directement entré)
Exemples d'utilisations :
*python3 Detection.py 2 Bonjour*
*python3 Detection.py 2 train.txt*


**Partie 2 : Évaluation et graphiques**

* Partie 2A facultative : Évaluation
Lancer le programme avec le fichier Evaluation.py
Argument facultatif : n (taille des n-grammes).
Exemple d'utilisation :
*python3 Evaluation.py 2*

* Partie 2B : Graphiques
Peut être lancé sans avoir lancé Evaluation au préalable.
Lancer le programme avec le fichier Graphes.py
Argument facultatif : n (taille des n-grammes).
Exemple d'utilisation :
*python3 Graphes.py 2*
