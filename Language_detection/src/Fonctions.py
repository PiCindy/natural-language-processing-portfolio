#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 2020

@authors: Romane GALLIENNE, Cindy PEREIRA
"""

import string as str
from nltk.util import ngrams
import re
import math
import os


# On ouvre un fichier
def readFile(fileName) :
    fic = open(fileName, "r")
    text = fic.read()
    fic.close()
    return text


# Permet d'extraire le texte de tous les fichiers d'une langue -> liste
def recuperationTextes(langue) :
    path = os.getcwd()
    directory = os.path.abspath(os.path.join(path, os.pardir)) + '/CorpusTest/' + langue
    txt = []
    for fileName in os.listdir(directory) :
        txt.append(readFile(directory + "/" + fileName))
    return txt

# Fonction qui enlève la ponctuation
def punct_less(text):
    for punct in str.punctuation:
        text = text.replace(punct, "")
    return text


# Fonction qui enlève les nombres
def numb_less(texte):
    return re.sub("[0-9]+", "", texte)


#crée un dictionnaire
def createDico(texte, n) :
    list_ngrams = list(ngrams(texte, n))
    dico = {}
    for gram in list_ngrams :
        if gram not in dico:
            dico[gram] = 0
        dico[gram] += 1
    return dico

#calcul des similarités par la distance euclidienne
def similariteDistanceEuclidienne(dicoCorpus, dicoTrain) :
    distance = 0
    for elmt in set(dicoCorpus.keys()).intersection(dicoTrain.keys()) :
        distance += (dicoCorpus[elmt]-dicoTrain[elmt])**2
    return math.sqrt(distance)

#calcul des similarités par similarité des cosinus
def similariteCosinus(dicoCorpus, dicoTrain) :
    prodScal, normCorpus, normTrain = 0, 0, 0
    for elmt in set(dicoCorpus.keys()).intersection(dicoTrain.keys()) :
        prodScal += dicoCorpus[elmt]*dicoTrain[elmt]
        normCorpus += dicoCorpus[elmt]**2
        normTrain += dicoTrain[elmt]**2
    norm = math.sqrt(normCorpus)*math.sqrt(normTrain)
    return prodScal / norm
