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
    positions_x = [-40, 40, x]
    choix = 0 # choisit fenetre ou fenetre balcon
    indice = 0
    y_elements = y_sol
    # dessin des murs
    if niveau in [1,2,3,4]:
        for i in range(niveau - 1):
            shuffle(positions_x)
            facade(x, y_sol, couleur, niveau - 1)
            # dessin des 3 Eléments
            for i in range(3):
                choix = randint(1, 2)
                if choix == 1:
                    fenetre(positions_x[indice], y_sol + 20)
                elif choix == 2:
                    fenetre_balcon(positions_x[indice], y_sol)
                indice += 1
            y_elements += 60
            indice = 0
            

if __name__ == '__main__':
    etage(0,0,"red",2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()