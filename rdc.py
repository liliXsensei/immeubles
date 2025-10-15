from facade import facade
from random import shuffle
from porte import porte
from porte2 import porte2
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''


    turtle.setx(x)
    turtle.sety(y_sol)

    portes = [porte, porte2]
    shuffle(portes) 
    positions = [-40, 40 , x]
    shuffle(positions)

    facade(x, y_sol, c_facade, 0)

    if portes[0] == porte:
        portes[0](x + positions[0], y_sol, c_porte)
    elif portes[0] == porte2:
        portes[0](x + positions[0], y_sol, c_porte)
        
    fenetre(x + positions[2], y_sol + 20)
    fenetre(x + positions[1], y_sol + 20)


if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()