from tkinter import *



def grid():
    for ligne in range(9):
        for colonne in range(9):
            Button(fenetre, val = '%s' % (ligne, colonne),borderwidth=1).grid(row=ligne, column=colonne)

