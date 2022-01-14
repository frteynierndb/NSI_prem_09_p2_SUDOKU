# Créé par teynier, le 16/12/2021 en Python 3.7
from tkinter import *
from tkinter import ttk

fenetre = Tk()

menubar = Menu(fenetre)


liste = 5

menu1 = Menu(menubar, tearoff=1)
menu1.add_command(label="lvl1", command=liste)
menu1.add_command(label="lvl2", command=liste)
menu1.add_command(label="lvl3", command=liste)
menubar.add_cascade(label="niveaux", menu=menu1)

s = Spinbox(fenetre, from_=1, to=9)
s.pack(side=RIGHT)

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'à une prochaine')
    else:
        showinfo('Titre 3', 'bonne chance')
        showerror("Titre 4", "hehe")

Button(text='quitter', command=callback).pack(side=BOTTOM, padx=10, pady=10)


fenetre.config(menu=menubar)
fenetre.mainloop()