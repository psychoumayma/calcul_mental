from random import randint
from random import choice

Question = [0,0,0]

#Cette fonction prends en paramètre une liste de deux
#valeur (n) aléatoires qui dépendent du niveau.
#et une valeur (operation) qui détermine l'opération du calcul.
def question(n, operation): 
    if operation==0:
        c = "calculer la somme "+str(n[0])+'+'+str(n[1])
    elif operation==1:
        c = "calculer la différence "+str(n[0])+'-'+str(n[1])
    elif operation==2:
        c = "calculer le produit "+str(n[0])+'x'+str(n[1])
    elif operation==3:
        c = "calculer le quotient de la division euclidienne "+str(n[0])+'/'+str(n[1])
    print(c)

#Cette fonction crée une liste avec 3 valeurs qui servent à déterminer la question sur l'interface graphique
def Question_graphique(n, operation):
    global Question
    Question = [n[0], n[1], operation]

    
#Cette fonction calcule les réponses des questions posées.
def reponse(n, operation):
    if operation==0:
        return n[0]+n[1]
    elif operation==1:
        return n[0]-n[1]
    elif operation==2:
        return n[0]*n[1]
    elif operation==3:
        return n[0]//n[1]

#Cette fonction vérifie si la réponse donnée par l'utilisateur est vraie ou fausse.
def jeu(operation, question, n):
    question(n, operation)
    r = (reponse(n,operation))
    i = int(input())
    if r == i:
        print("bonne réponse, BRAVO!!!!")
        return 1
    else:
        print("Oh non mauvaise réponse!!!!!!!!")
        return 0

#Cette fonction permet de déterminer les valeurs choisies pour une opération en fonction du niveau.
def adapt_level(niveau, operation):
    if (niveau == 1):
        if operation == 1:
            a = randint(2,10)
            b = randint(1,a-1)          #Par exemple ici on a pris a-1 pour la deuxième valeur car le niveau 1 ne doit pas contenir de soustraction négatives.
            return (a,b)
        else:
            return(randint(1,10),randint(1,10))
    elif (niveau == 2):
        if operation==3:
            a = randint(10,30)
            b = randint(1,a)
            return (a,b)
        else:
            return (randint(10, 30),randint(10, 30))
    elif (niveau == 3):
        return (randint(30, 100),randint(10, 30))


#le main controle le score qui permet de definir le niveau du jeu.
def main():
    score = 0
    total = 0
    niveau = 1
    while niveau < 4:
        while score < 5 :
            for l in range (5):
                if niveau == 1:
                    x =[0,1,2]
                elif niveau > 1:
                    x =[0,1,2,3]
            operation = choice(x)
            n = adapt_level(niveau, operation)
            c = ''
            score = score + jeu(operation, question, n)
        niveau = niveau + 1
        total = total + score
        score = 0
        print("score: ", total)
        print("niveau: ", niveau)
    
        
if __name__=="__main__":
    main()
