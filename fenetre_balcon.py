import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''

    # porte-fenetre
    turtle.fillcolor("grey90")
    turtle.begin_fill()
    turtle.penup() 
    turtle.goto(x, y) 
    turtle.pendown()
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(15)
    turtle.end_fill()
    

    # balcon
    turtle.penup()
    turtle.goto(-21, y)
    turtle.pendown()
    turtle.width(3)
    rectangle(0, 0, 42, 25)
    trait(-15, 0, -15, 25)
    trait(-9, 0, -9, 25)
    trait(-3, 0, -3, 25)
    trait(3, 0, 3, 25)
    trait(9, 0, 9, 25)
    trait(15, 0, 15, 25)        



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()