 
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