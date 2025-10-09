import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    y_etage = y_sol
    if niveau not in [0,1,2,3,4]:
        print("Niveau invalide")
    else:
        for etage in range(niveau + 1):
            turtle.color(couleur)
            turtle.begin_fill()
            rectangle(x, y_etage, 140, 60)
            turtle.end_fill()
            turtle.color("black")
            rectangle(x, y_etage, 140, 60)
            y_etage += 60


if __name__ == '__main__':
    facade(0,0,"red",1)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()