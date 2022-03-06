

x = Button(row)
y = Button(column)

def end ():
    for i in lvl1:
        for j in i:
            if j == " ":
                count = count + 1
        if count == 0:
            fin = Label(fenetre, text="vous avez fini!")
        else:
            pass

def check(x, y):
    if l+str(x)[y] =! l+str(x)c[y]:
        erreur = label(fenetre, text = "il y a une erreur dans la valeur que vous avez donné")




def changer_valeur(event):
    touche = event.keysim
    if touche == "<Button-1>":
          val = input(val)
          l+str(x).append(y, val)
          check()
          end()



erreur.pack()

fin.pack
