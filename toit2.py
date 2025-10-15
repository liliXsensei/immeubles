import turtle
from trait import trait

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''

    turtle.penup()
    turtle.setx(x)
    turtle.sety((niveau+1)*60)
    turtle.width(10)
    turtle.goto(x - 80, (niveau+1) *60)
    turtle.pendown()
    turtle.forward(160)


if __name__ == '__main__':
    toit2(0,0,2)
    toit2(100, 0, 1)
    toit2(200, 0, 4)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()