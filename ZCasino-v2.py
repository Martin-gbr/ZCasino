""" Module permettant de jouer à la roulette. Comme au Casino !"""

from math import ceil           # Pour arrondir un nombre
from random import randrange    # Pour générer des nombre aléatoirement

# Déclaration des variables de départ
Fortune = 500 # Le joueur commence avec une mise de 500$
continuer_partie = True # Booléen qui est vrai tant qu'on doit continuer la partie

print("Bienvenue au ZCasino. Vous vous installez à une table de roulette avec 500$")

while continuer_partie is True :
    
    # On va demander au joueur de choisir une case sur laquelle miser.
    Case = -1
    while Case < 0 or Case > 49 :
        Case = input("Choisissez une case sur laquelle miser (0-49) :")
        #On convertit la variable case en entier
        try :
            Case = int(Case)
        except ValueError :
            print("Vous n'avez pas saisi un nombre")
            Case = -1
            continue
        if Case < 0 or Case > 49 :
            print("Choisissez une case entre 0 et 49 inclu")
            Case = -1
            continue
    
    # 0n demande combien le joueur veut miser
    Mise = -1
    while Mise <= 0 or Mise > Fortune :
        Mise = input("Choisissez une somme à miser :")
        #On convertit la mise en entier
        try :
            Mise = int(Mise)
        except ValueError :
            print("Vous n'avez pas saisi un chiffre")
            Mise = -1
            continue
        if Mise <= 0 or Mise > Fortune :
            print("Vous devez miser au moins 1$ et ne pas miser plus que votre fortune ne le permet.")
            Mise = -1
            continue
    
    # On va tirer un chiffre au hasard pour lancer la roulette
    Numero_gagnant = randrange(50)
    print("La roulette tourne... attention... Le numéro gagnant est :", Numero_gagnant, "!")

    # On calcul le gain ou la perte du joueur
    if Numero_gagnant == Case :
        print("Félicitations ! Vous gagnez :", Mise * 3, "$ !")
        Fortune += Mise * 3
    elif Numero_gagnant % 2 == Case % 2 :
        Mise = ceil(Mise + (0.5 * Mise))
        print("Vous avez misé sur la bonne couleur. Vous remportez :", Mise )
        Fortune += Mise
    else :
        print("Désolé mon vieux... C'est perdu. Vous perdez votre mise.")
        Fortune -= Mise

    # On arrête la partie quand le joueur est à sec ou on lui annonce sa fortune.
    if Fortune <= 0 :
        print("Vous êtes fauché. Vous devez quitter la table. Au revoir.")
        continuer_partie = False
    else : # On affiche la fortune du joueur
        print("Vous avez maintenant : ", Fortune, "$")
        Quitter = input("Voulez-vous continuer la partie ? (1 = oui /2 = non) :")
        try :
            Quitter = int(Quitter)
            if Quitter != 1 and Quitter != 2 :
                raise ValueError("Vous n'avez pas taper le bon chiffre")
        except ValueError : 
            print("Choisissez entre le chiffre 1 et le chiffre 2. Pour oui ou non.")
        if Quitter == 2:
            print("Vous quittez la table. Vous sortez de la table avec votre butin :", Fortune, "$. A la prochaine !")
            continuer_partie = False
        if Quitter == 1:
            continuer_partie = True
      
