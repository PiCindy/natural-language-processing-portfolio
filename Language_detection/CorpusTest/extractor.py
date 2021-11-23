#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:28:03 2020

@author: Romane Gallienne, Cindy Pereira
"""

#penser à installer wikipedia -> pip3 install wikipedia
import wikipedia 

#fichier = open("french.txt", "w")

wikipedia.set_lang('pt')

writers = ['Pierre Corneille',"Jean Racine",'Victor Hugo','Gustave Flaubert','Honoré de Balzac','Emile Zola','Charles Baudelaire','Arthur Rimbaud','Paul Verlaine']

corpus = ""

'''
for auteur in writers:
    fichier = open("auteur.txt", "w")
    corpus += wikipedia.summary(auteur)
    fichier.write(corpus)
'''

#corpus  = wikipedia.summary(auteur) for auteur in writers

for auteur in writers:
    fichier = "{}.txt".format(auteur)
    with open(fichier, 'w') as f:
        corpus = wikipedia.summary(auteur)
        f.write(corpus)
