import turtle

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''

    turtle.penup()
    turtle.setx(x)
    turtle.sety(niveau+(1)*60)
    turtle.goto(x, y_sol)
    turtle.pendown()
    turtle.forward(80)
    turtle.goto(x, y_sol + 60)
    turtle.goto(x - 80, y_sol)
    turtle.forward(80)


if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()