# Créé par francois, le 05/03/2022 en Python 3.7
https://openclassrooms.com/forum/sujet/coordonnees-de-grille-tkinter
lvl1 = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

l1 = [" ", 9, 1, 3, 2, " ", " ", " ", " " ]
l2 = [" ", " ", 2, " ", " ", " ", " ", " ", 5]
l3 = [" ", 4, " ", 6, " ", 7, 9, " ", " "]
l4 = [4, " ", 9, 8, 1, 6, 3, 2, " "]
l5 = [7, " ", 8, 2, 4, " ", 5, 9, 6]
l6 = [3, " ", 6, " ", " ", " ", " ", " ", 1]
l7 = [" ", " ", 4, " ", " ", " ", 2, 7, " "]
l8 = [" ", " ", " ", 1, " ", 2, " ", 5, 4]
l9 = [" ", 6, " ", " ", 7, " ", " ", " ", " "]

def generateur(lvl1):
    for i in l1:
        Button(main, text= i, borderwidth=5).grid(row=1, column=l1[i]+1)
    for i in l2:
        Button(main, text= i, borderwidth=5).grid(row=2, column=l2[i]+1)
    for i in l3:
        Button(main, text= i, borderwidth=5).grid(row=3, column=l3[i]+1)
    for i in l4:
        Button(main, text= i, borderwidth=5).grid(row=4, column=l4[i]+1)
    for i in l5:
        Button(main, text= i, borderwidth=5).grid(row=5, column=l5[i]+1)
    for i in l6:
        Button(main, text= i, borderwidth=5).grid(row=6, column=l6[i]+1)
    for i in l7:
        Button(main, text= i, borderwidth=5).grid(row=7, column=l7[i]+1)
    for i in l8:
        Button(main, text= i, borderwidth=5).grid(row=8, column=l8[i]+1)
    for i in l9:
        Button(main, text= i, borderwidth=5).grid(row=9, column=l9[i]+1)

lvl1c = [l1c, l2c, l3c, l4c, l5c, l6c, l7c, l8c, l9c]

l1c = [5, 9, 1, 3, 2, 4, 7, 6, 8]
l2c = [6, 7, 2, 9, 8, 1, 4, 3, 5]
l3c = [8, 4, 3, 6, 5, 7, 9, 1, 2]
l4c = [4, 5, 9, 8, 1, 6, 3, 2, 7]
l5c = [7, 1, 8, 2, 4, 3, 5, 9, 6]
l6c = [3, 2, 6, 7, 9, 5, 8, 4, 1]
l7c = [1, 3, 4, 5, 6, 8, 2, 7, 9]
l8c = [9, 8, 7, 1, 3, 2, 6, 5, 4]
l9c = [2, 6, 5, 4, 7, 9, 1, 8, 3]