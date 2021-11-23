#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 2020

@author: Romane GALLIENNE, Cindy PEREIRA
"""

from sys import argv

from Fonctions import recuperationTextes
from Fonctions import createDico
from Fonctions import numb_less

from Detection import calculLangue
from Detection import maxSim
from Detection import minSim


n = 2
# Si l'utilisateur a bien entré un n, on le récupère
if len(argv) > 1 :
    n = int(argv[1])

langues = ["allemand", "anglais", "espagnol", "francais", "portugais"]
textes = []

# On récupère tous les textes de chaque langue
for langue in langues :
    textes.extend(recuperationTextes(langue))


# Indices de chaque langue :
# 0 <= i <= 8 : Allemand
# 9 <= i <= 17 : Anglais
# 18 <= i <= 26 : Espagnol
# 27 <= i <= 35 : Francais
# 36 <= i <= 44 : Portugais

# Creation de la liste des langues
languesTextes = ["allemand"]*9
languesTextes.extend(["anglais"]*9)
languesTextes.extend(["espagnol"]*9)
languesTextes.extend(["francais"]*9)
languesTextes.extend(["portugais"]*9)


testsCos, testsDE = [], []
tailleTextes = []
i = 0

# Pour chaque texte du corpus, on trouve la langue la plus proche
for texte in textes :
    print("Texte", i+1, ":")
    tailleTextes.append(len(texte))
    texte = numb_less(texte)
    dicoTrain = createDico(texte, n)
    liste1, liste2 = [], []

    for langue in langues :
        calculLangue(liste1, liste2, langue, dicoTrain, n)

    indCos = maxSim(liste1)
    indDE = minSim(liste2)

    # Si la langue trouvée est correcte, alors on ajoute un True, sinon un False
    if langues[indCos] == languesTextes[i] :
        testsCos.append(True)
    elif langues[indCos] != languesTextes[i]:
        testsCos.append(False)

    if langues[indDE] == languesTextes[i] :
        testsDE.append(True)
    elif langues[indDE] != languesTextes[i] :
        testsDE.append(False)

    i+=1
    print()


# Renvoie le nombre de bons résultats
def evaluation(liste):
    bonRes = 0
    for res in liste :
        if res == True :
            bonRes += 1
    return bonRes


# Renvoie deux listes :
# - differentes tailles de textes rencontrees
# - pourcentages de textes bien étiquetés par taille
def pourcentageParTaille(tailleTextes, testsCos) :
    taillesUniq = []
    nbTextesParTaille = []
    nbCorrects = []

    for i in range (0, len(tailleTextes)) :
        if tailleTextes[i] not in taillesUniq :
            taillesUniq.append(tailleTextes[i])
            nbTextesParTaille.append(1)
            if testsCos[i] :
                nbCorrects.append(1)
            else :
                nbCorrects.append(0)
        else :
            index = taillesUniq.index(tailleTextes[i])
            nbTextesParTaille[index] += 1
            if testsCos[i] :
                nbCorrects[index] += 1

    pourcentages = []
    for i in range (0, len(nbTextesParTaille)) :
        pourcentages.append(nbCorrects[i]*100/nbTextesParTaille[i])

    return taillesUniq, pourcentages



print("Pourcentage de réussite pour la similarité cosinus :", evaluation(testsCos)*100/len(testsCos), "/", 100)
print("Pourcentage de réussite pour la distance euclidienne :", evaluation(testsDE)*100/len(testsDE), "/", 100)
