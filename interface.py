# Créé par francois, le 06/03/2022 en Python 3.7
from tkinter import *
from tkinter import ttk


fenetre = Tk()

menubar = Menu(fenetre)


menu1 = Menu(menubar, tearoff=1)
menu1.add_command(label="lvl1", command=generateur())
menubar.add_cascade(label="niveaux", menu=menu1)


def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'à une prochaine')
    else:
        showinfo('Titre 3', 'bonne chance')
        showerror("Titre 4", "hehe")

Button(text='quitter', command=callback).pack(side=BOTTOM, padx=10, pady=10)

fenetre.config(menu=menubar)
fenetre.mainloop()
