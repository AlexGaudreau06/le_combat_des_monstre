
import random
import time
nbr_vie = 20


def choix_1():
    global nbr_vie
    lancer_de = random.randint(1, 6)
    print("Vous avez eu", lancer_de)
    print("Combat en cours")
    time.sleep(random.randint(3, 8))
    if

        nbr_vie = nbr_vie - difficulte_adversaire
        print("Vous avez PERDUE!")
    elif difficulte_adversaire < lancer_de:
        nbr_vie
        print("Vous avez GAGNER!")


while True:
    difficulte_adversaire = random.randint(1, 5)
    print("Vous tombez face à face avec un adversaire de difficulté", difficulte_adversaire, "et\n"
          "vous avez", nbr_vie, "vie")
    choix = int(input("Que voulez-vous faire?\n"
                      "   1- Combattre cet adversaire\n"
                      "   2- Contourner cet adversaire et aller ouvrir une autre porte\n"
                      "   3- Afficher les regles du jeu\n"
                      "   4- Quitter la partie\n"
                      "_"))
    if choix == 1:
        choix_1()
    elif choix == 2:
        nbr_vie = nbr_vie - 1
    elif choix == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a lieu\n"
              "lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans \n"
              "ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se termine \n"
              "lorsque les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter chaque \n"
              "adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
    else:
        print("Merci et au revoir...")
        break
