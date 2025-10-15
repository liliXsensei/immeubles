from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

# 15 pixels extrémitées, 10 pixels entre fenêtres, 10 pixels entre haut fenêtre/étage
#140 pixels de large, 60 de haut
def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc

    @@ -14,12 +17,16 @@ def etage(x, y_sol, couleur, niveau):
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    turtle.speed(50)
    positions_x = [x - 40, x + 40, x]
    choix = 0 # choisit fenetre ou fenetre balcon
    indice = 0
    y_elements = y_sol

    # dessin des murs
    shuffle(positions_x)
    facade(x, y_sol, couleur, niveau)
    # dessin des 3 Eléments
    for i in range(3):
        choix = randint(1, 2)
        if choix == 1:
            fenetre(positions_x[indice], y_sol + niveau*60 + 20)
        elif choix == 2:
            fenetre_balcon(positions_x[indice], y_sol + niveau*60)
        indice += 1
    y_elements += 60
    indice = 0
            

if __name__ == '__main__':
    etage(50,0,"blue",4)
    etage(0,0,"red",1)
    etage(100,0,"pink",2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()