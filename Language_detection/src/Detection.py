#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 9 2020

@authors: Romane GALLIENNE, Cindy PEREIRA
"""

from Fonctions import numb_less
from Fonctions import createDico
from Fonctions import similariteCosinus
from Fonctions import similariteDistanceEuclidienne
from Fonctions import readFile

from sys import argv
import os
import pickle

'''
A LANCER AVEC UN N ET UN NOM DE FICHIER EN ARGUMENT
'''

# Renvoie la similarité cosinus et la similarité DE entre le dictionnaire d'un texte et le dictionnaire d'une langue
def similarite(dicoTrain, language, n) :
    fileName = os.getcwd() + '/variables/' + language + 'Dico' + str(n) + '.pkl'
    data = open(fileName, 'rb')
    dicoCorpus = pickle.load(data)
    data.close()
    return similariteCosinus(dicoCorpus, dicoTrain), similariteDistanceEuclidienne(dicoCorpus, dicoTrain)

#fonction pour chercher la similarité la plus grande
def maxSim(liste) :
    indMax = 0
    for i in range (0, len(liste)) :
        if liste[i] > liste[indMax] :
            indMax = i
    return indMax


#fonction pour chercher la distance euclidienne la plus petite
def minSim(liste) :
    indMin = 0
    for i in range (0, len(liste)) :
        if liste[i] < liste[indMin] :
            indMin = i
    return indMin


# Calcule et affiche le cosinus et la distance euclidienne entre le dictionnaire d'un texte et celui d'une langue
def calculLangue(liste1, liste2, langue, dicoTrain, n) :
    sim1, sim2 = similarite(dicoTrain, langue, n)
    liste1.append(sim1)
    liste2.append(sim2)
    print(langue, ": cos ->", sim1, "DE ->", sim2)

langues = ["allemand", "anglais", "espagnol", "francais", "portugais"]

print()
# Si l'utilisateur a bien entré deux arguments :
# - un n pour les n-grammes
# - un nom de fichier ou un texte directement entré
if len(argv) > 2 :
    txt = ""
    n = int(argv[1])
    # Alors, on récupère le texte (du fichier ou de l'argument)
    if os.path.isfile(argv[2]) :
        txt = readFile(argv[2])
    else :
        words = argv[2:]
        for word in words :
            txt += word + " "
    txt = numb_less(txt)
    # On en crée le dictionnaire en utilisant des n-grammes
    dicoTrain = createDico(txt, n)
    liste1, liste2 = [], []

    # On calcule la similarité pour chaque langue
    for langue in langues :
        calculLangue(liste1, liste2, langue, dicoTrain, n)


    # On récupère l'indice de la langue la plus proche et on l'affiche
    indCos = maxSim(liste1)
    indDE = minSim(liste2)

    print()
    print("D'après le cosinus, le texte semble être en", langues[indCos])
    print("D'après la distance euclidienne, le texte semble être en", langues[indDE])
