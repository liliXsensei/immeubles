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
    # dessin des murs
    x_fenetre_1 = 0
    if niveau in [1,2,3,4]:
        for i in range(niveau - 1):
            facade(x, y_sol, couleur, niveau - 1)
            # dessin des 3 Eléments
            fenetre(30, 40)
            fenetre_balcon(30, y_sol)

if __name__ == '__main__':
    etage(0,0,"red",2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()