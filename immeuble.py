# module immeuble

from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)

    pass

    turtle.speed(100)

    # Autoriser les couleurs RVB 0-255
    turtle.colormode(255)

    pass
    # Nombre d'étage (aléatoire entre 1 et 5)
    nb_etages = randint(1, 5)

    c_facade = couleur_aleatoire()
    c_porte = couleur_aleatoire()

    pass
    # Dessin du RDC
    rdc(x, y_sol, c_facade, c_porte)

    # Dessin des étages

    pass
    for niveau in range(1, nb_etages):
        etage(x, y_sol + 60, c_facade, niveau)

    # Dessin du toit

    pass
    toit(x, y_sol, nb_etages)

if __name__ == '__main__':
    immeuble(0,0)