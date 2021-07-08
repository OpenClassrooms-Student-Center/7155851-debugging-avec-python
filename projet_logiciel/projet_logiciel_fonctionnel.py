# -*- coding: utf8 -*-

from random import randint 
from tkinter import *

class PierreFeuilleCiseaux:
    def __init__(self, nouveau_score_joueur, nouveau_score_ia, label_joueur, label_ia):
        self.score_joueur = 0
        self.score_intelligence_artificielle = 0
        self.nouveau_score_joueur = nouveau_score_joueur
        self.nouveau_score_ia = nouveau_score_ia
        self.label_joueur = label_joueur
        self.label_ia = label_ia

    def maj_scores(self, choix_ia, choix_joueur):
        if choix_ia == 1 and choix_joueur == 2:
            self.score_joueur += 1
        elif choix_ia == 2 and choix_joueur == 1:
            self.score_intelligence_artificielle += 1
        elif choix_ia == 1 and choix_joueur == 3:
            self.score_intelligence_artificielle += 1
        elif choix_ia == 3 and choix_joueur == 1:
            self.score_joueur += 1
        elif choix_ia == 3 and choix_joueur == 2:
            self.score_intelligence_artificielle += 1
        elif choix_ia == 2 and choix_joueur == 3:
            self.score_joueur += 1

    def jouer(self, choix_joueur):
        choix_ia = randint(1,3)
        if choix_ia==1:
            self.label_ia.configure(image=pierre)
        elif choix_ia==2:
            self.label_ia.configure(image=feuille)
        else:
            self.label_ia.configure(image=ciseaux)
        self.maj_scores(choix_ia,choix_joueur)
        self.nouveau_score_joueur.configure(text=str(self.score_joueur))
        self.nouveau_score_ia.configure(text=str(self.score_intelligence_artificielle))
    
    def jouer_pierre(self):
        self.jouer(1)
        self.label_joueur.configure(image=pierre)

    def jouer_feuille(self):
        self.jouer(2)
        self.label_joueur.configure(image=feuille)

    def jouer_ciseaux(self):
        self.jouer(3)
        self.label_joueur.configure(image=ciseaux)

    def rejouer(self):
        self.score_joueur = 0
        self.score_intelligence_artificielle = 0
        self.nouveau_score_joueur.configure(text=str(self.score_joueur))
        self.nouveau_score_ia.configure(text=str(self.score_intelligence_artificielle))
        self.label_joueur.configure(image=zero)
        self.label_ia.configure(image=zero)


fenetre = Tk()
fenetre.title("Pierre Feuille Ciseaux")

zero = PhotoImage(file ='zero.gif')
versus = PhotoImage(file ='vs.gif')
pierre = PhotoImage(file ='pierre.gif')
feuille = PhotoImage(file ='feuille.gif')
ciseaux = PhotoImage(file ='ciseaux.gif')

texte1 = Label(fenetre, text="Vous", font=("Arial", 20, "bold"))
texte1.grid(row=0,column=0)

texte2 = Label(fenetre, text="Intelligence artificielle", font=("Arial", 20, "bold"))
texte2.grid(row=0,column=2)

texte3 = Label(fenetre, text="Pour jouer, cliquez sur une des icônes ci-dessous.",font=("Arial", 20, "bold"))
texte3.grid(row=3, columnspan =3, pady =5)

nouveau_score_joueur = Label(fenetre, text="0", font=("Arial", 20, "bold"))
nouveau_score_joueur.grid(row=1, column=0)

nouveau_score_ia = Label(fenetre, text="0", font=("Arial", 20, "bold"))
nouveau_score_ia.grid(row=1, column=2)

label_joueur = Label(fenetre, image=zero)
label_joueur.grid(row =2, column =0)

label_vs = Label(fenetre, image=versus)
label_vs.grid(row =2, column =1)

label_ia = Label(fenetre, image=zero)
label_ia.grid(row =2, column =2)

jeu = PierreFeuilleCiseaux(nouveau_score_joueur, nouveau_score_ia, label_joueur, label_ia)

bouton_pierre = Button(fenetre,command=jeu.jouer_pierre)
bouton_pierre.configure(image=pierre)
bouton_pierre.grid(row =4, column =0)

bouton_feuille = Button(fenetre,command=jeu.jouer_feuille)
bouton_feuille.configure(image=feuille)
bouton_feuille.grid(row =4, column =1,)

bouton_ciseaux = Button(fenetre,command=jeu.jouer_ciseaux)
bouton_ciseaux.configure(image=ciseaux)
bouton_ciseaux.grid(row =4, column =2)

bouton_recommencer = Button(fenetre,text='Rejouer',command=jeu.rejouer,font=("Courier", 20, "bold"))
bouton_recommencer.grid(row =5, column =0, pady =10, sticky=E)

bouton_quitter = Button(fenetre,text='Quitter',command=quit,font=("Courier", 20, "bold"))
bouton_quitter.grid(row =5, column =2, pady =10, sticky=W)

fenetre.mainloop()
