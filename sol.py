# Module par sebastien chanthery

import turtle
from trait import trait

# ----- Sol de la rue -----
def sol(y_sol):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    turtle.penup()
    turtle.sety(y_sol)
    turtle.width(3)
    turtle.pendown()
    turtle.forward(100)


if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()