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
    turtle.speed(200)

    # Autoriser les couleurs RVB 0-255
    turtle.colormode(255)

    # Nombre d'étage (aléatoire entre 0 et 4)
    nb_etages = randint(0, 4)

    c_facade = couleur_aleatoire()
    c_porte = couleur_aleatoire()

    # Dessin du RDC
    rdc(x, y_sol, c_facade, c_porte)

    # Dessin des étages
    for niveau in range(1, nb_etages + 1):
        etage(x, y_sol, c_facade, niveau)

    # Dessin du toit
    toit(x, y_sol, nb_etages)

if __name__ == '__main__':
    immeuble(0,0)