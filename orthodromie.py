#Python 3.5

from tkinter import *
import math



#############Calcul#####################################
def calcul():
    try:
        #Recup variables
        La=float(entree.get())
        La=math.radians(La)
        la=float(entree1.get())
        la=math.radians(la)
        Lb=float(entree2.get())
        Lb=math.radians(Lb)
        lb=float(entree3.get())
        lb=math.radians(lb)
        #Calcul
        cosp=(math.sin(La)*math.sin(Lb))+(math.cos(La)*math.cos(Lb)*math.cos(la-lb))
        p=math.acos(cosp)
        p=math.degrees(p)
        p=p*60
        #Sortie resultats
        Label(fenetre, text="Distance=").place(x=5, y=200)
        Label(fenetre, text=p).place(x=70, y=200)
        Label(fenetre, text="NM").place(x=220, y=200)
        d=(p/0.00053996)/1000
        d="= "+str(d)+"km"
        Label(fenetre, text=d).place(x=250, y=200)
    except ValueError:
        Label(fenetre, text="Les donnees ne sont pas valides").place(x=35, y=170)


###########Def fenetre#####################################
fenetre= Tk()
fenetre.geometry ('500x300+40+40')
fenetre.title ("Calcul de l'orthodromie")

La=StringVar() 
La.set("")
la=StringVar() 
la.set("")
Lb=StringVar() 
Lb.set("")
lb=StringVar() 
lb.set("")


############Point A######################################
Label(fenetre, text="Point A").place(x=10, y=5)
 
Label(fenetre, text="Lattitude :").place (x=20, y=20)

entree = Entry(fenetre, textvariable=La, width=10)
entree.place(x=100, y=20)

Label(fenetre, text="°").place(x=200, y=20)

Label(fenetre, text="Longitude:").place (x=20, y=50)

entree1 = Entry(fenetre, textvariable=la, width=10)
entree1.place(x=100, y=50)

Label(fenetre, text="°").place(x=200, y=50)


############Point B######################################
Label(fenetre, text="Point B").place(x=10, y=75)
 
Label(fenetre, text="Lattitude :").place (x=20, y=100)

entree2 = Entry(fenetre, textvariable=Lb, width=10)
entree2.place(x=100, y=100)

Label(fenetre, text="°").place(x=200, y=100)

Label(fenetre, text="Longitude:").place (x=20, y=130)

entree3 = Entry(fenetre, textvariable=lb, width=10)
entree3.place(x=100, y=130)

Label(fenetre, text="°").place(x=200, y=130)

##############Bouton###################################
Button(fenetre, text="Calculer", command=calcul).place(x=250, y=75)



