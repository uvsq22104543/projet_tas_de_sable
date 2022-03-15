################################

# MIASHS TD2
# Can DOYURUR
# Kamel ALICHE
# Guillaume FOSSO
# https://github.com/uvsq22104543/projet_tas_de_sable

################################


# import des librairies

import tkinter as tk

from random import randint 

racine = tk.Tk()

# définition des constantes

# définition des variables globales

# définition des fonctions 

def confaleatoire():   
    ff

    

# programme principal 

canvas = tk.Canvas(racine, bg="black", height=750, width=750)
canvas.grid(row=1, column=1)


## Les boutons

confi_aleatoire = tk.Button(text="Configuration aléatoire", font=("helvetica", "12"))
confi_aleatoire.grid(row=0, column=1)

confi_vide = tk.Button(text="Configuration vide", font=("helvetica", "12"))
confi_vide.grid(row=0, column=2)





#lignes horizontales et verticales 

canvas.create_line((0, 750/3), (750, 750/3), fill="gray", width=4)

canvas.create_line((0, 750/3*2), (750, 750/3*2), fill="gray", width=4)

canvas.create_line((750/3, 0), (750/3, 750), fill="gray", width=4)

canvas.create_line((750/3*2, 0), (750/3*2, 750), fill="gray", width=4)





racine.mainloop()