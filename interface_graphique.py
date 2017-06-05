from tkinter import*
from random import randint
from random import choice
import jeu


fenetre = Tk()
FRAME=Frame(fenetre, width=100, height =50).place(x=700,y=400)
LABEL=Label(FRAME, text='', font = 'Papyrus 20 bold', fg="blue")
BRAVO=Label(FRAME, text='', font = 'Papyrus 20 bold', fg="green")
DOMMAGE=Label(FRAME, text='', font = 'Papyrus 20 bold', fg="red")
ent = Entry(fenetre)
Score = 0
Total = 0
Niveau = 1


#cette fonction consiste à dessiner une zone de réponse
#ou l'utilisateur peut entrer sa réponse.
def affiche_zone_reponse():
    ent.insert(0, '')
    ent.pack(side=LEFT, fill=X)
    ent.bind('<Return>', reponse)

#cette fonction permet de prendre la réponse entrée et la vérifier.
def reponse(event):
    x= int(ent.get())
    test_reponse(x)

#Cette fonction permet de vérifier la réponse entrée
#et afficher un label qui dépend de la réponse
#
def test_reponse(reponse):
    global Score
    global Niveau
    global Total
    if reponse==jeu.reponse(jeu.Question[0:2], jeu.Question[2]):
        Score = Score+1
        DOMMAGE.place_forget()
        BRAVO.config(text="Bonne Réponse BRAVO!")
        BRAVO.place(x=120, y=320)
        if Score == 5:
            Niveau += 1
            Total += Score
            Score = 0
        if Niveau <4:
            question()
        else:
            print(Total)
    else:
        BRAVO.place_forget()
        DOMMAGE.config(text="FAUX! Essayez encore!")
        DOMMAGE.place(x=120, y=320)



#Cette fonction permet d'afficher la question dans un label
def affiche_question():
    if jeu.Question[2]==0:
        c = "Calculer la somme "+str(jeu.Question[0])+'+'+str(jeu.Question[1])
    elif jeu.Question[2]==1:
        c = "Calculer la différence "+str(jeu.Question[0])+'-'+str(jeu.Question[1])
    elif jeu.Question[2]==2:
        c = "Calculer le produit de "+str(jeu.Question[0])+' et '+str(jeu.Question[1])
    elif jeu.Question[2]==3:
        c = "Calculer le quotient de la division euclidienne "+str(jeu.Question[0])+'/'+str(jeu.Question[1])
    LABEL.config(text=c)
    LABEL.pack(side=LEFT)

#cette fonction permet d'exécuter les deux fonctions qui permettent
#d'afficher la question et la zone de saisie.
def affiche_jeu():
    affiche_question()
    affiche_zone_reponse()


#Cette fonction permet de créer une zone de saisie.
def zone_de_saisie(label, stringvar):
    text = stringvar.get()
    label.config(text=text)


#Cette fonction permet de déterminer l'operation en fonction du niveau.
def question():
    if Niveau == 1:
        x =[0,1,2]
    else:
        x =[0,1,2,3]
    operation = choice(x)
    n = jeu.adapt_level(Niveau, operation)
    jeu.Question_graphique(n, operation)
    affiche_jeu()
    
#Affichage d'une Image
    
photo = PhotoImage(file="enfant.gif")
canvas = Canvas(fenetre,width=300, height=203, bd=8)
canvas.create_image(0, 20, anchor=NW, image=photo)
canvas.pack()


# bouton de sortie qui permet de quitter le jeu
bouton=Button(fenetre, text="Quitter", command=fenetre.quit)
bouton.pack(side=BOTTOM)

#bouton de relance
##def recommencer():
##    main()
##    button1 = Tkinter.Button(fenetre, text="RECOMMENCER", command=x)
    
def main():
    
    fenetre.geometry("700x400")
    question()
    fenetre.mainloop()
    fenetre.destroy()
        
if __name__=="__main__":
        main()
 


