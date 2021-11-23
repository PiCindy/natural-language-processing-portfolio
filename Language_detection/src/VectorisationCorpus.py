#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 9 2020

@authors: Romane GALLIENNE, Cindy PEREIRA
"""

from Fonctions import createDico
from Fonctions import readFile
import os
import pickle
from sys import argv

"""
Fichier permettant de vectoriser les corpus tests
NE PAS LANCER, LES VARIABLES SONT DEJA SAUVEGARDEES
"""

# Permet d'extraire le texte de tous les fichiers d'une langue -> str
def recuperationTextesCorpus(langue) :
    path = os.getcwd()
    directory = os.path.abspath(os.path.join(path, os.pardir)) + '/Corpus/' + langue
    txt = ""
    for fileName in os.listdir(directory) :
        txt += readFile(directory + "/" + fileName)
    return txt


# Crée le dictionnaire n-gramme de chaque langue et le sérialise
def recuperationDico(langue, n) :
    text = recuperationTextesCorpus(langue)
    dico = createDico(text, n)
    fileName = os.getcwd() + '/variables/' + langue + 'Dico' + str(n) + '.pkl'
    f = open(fileName, 'wb')
    pickle.dump(dico, f)
    f.close()


n = 2
# Si l'utilisateur a entré un n, on le récupère, sinon on le fixe à 2
if len(argv) > 1 :
    n = int(argv[1])

recuperationDico("anglais", n)
recuperationDico("allemand", n)
recuperationDico("espagnol", n)
recuperationDico("francais", n)
recuperationDico("portugais", n)
