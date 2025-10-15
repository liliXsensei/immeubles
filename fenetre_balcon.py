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
    turtle.speed(100)
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
    turtle.goto(x - 6, y)
    turtle.pendown()
    turtle.width(3)
    rectangle(x, y, 42, 25)
    trait(x1 = x - 15, y1 = y, x2 = x - 15, y2 = y + 25)
    trait(x1 = x - 9, y1 = y, x2 = x - 9, y2 = y + 25)
    trait(x1 = x - 3, y1 = y, x2 = x - 3, y2 = y + 25)
    trait(x1 = x + 3, y1 = y, x2 = x + 3, y2 = y + 25)
    trait(x1 = x + 9, y1 = y, x2 = x + 9, y2 = y + 25)
    trait(x1 = x + 15, y1 = y, x2 = x + 15, y2 = y + 25)
    turtle.width(1)



if __name__ == '__main__':
    fenetre_balcon(-200, 0)
    fenetre_balcon(-100, 0)
    fenetre_balcon(0, 0)
    fenetre_balcon(100, 0)
    fenetre_balcon(200, 0)

    fenetre_balcon(-200, 100)
    fenetre_balcon(-100, 100)
    fenetre_balcon(0, 100)
    fenetre_balcon(100, 100)
    fenetre_balcon(200, 100)

    fenetre_balcon(-200, 200)
    fenetre_balcon(-100, 200)
    fenetre_balcon(0, 200)
    fenetre_balcon(100, 200)
    fenetre_balcon(200, 200)

    fenetre_balcon(-200, -100)
    fenetre_balcon(-100, -100)
    fenetre_balcon(0, -100)
    fenetre_balcon(100, -100)
    fenetre_balcon(200, -100)

    fenetre_balcon(-200, -200)
    fenetre_balcon(-100, -200)
    fenetre_balcon(0, -200)
    fenetre_balcon(100, -200)
    fenetre_balcon(200, -200)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()