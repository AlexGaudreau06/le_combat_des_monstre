
import random
import time
nbr_vie = 20
nbr_combat = 0
combat_gagner = 0
victoire_daffilee = 0


def choix_3():
    print("Pour réussir un combat, il faut que la valeur du dé lancé est supérieure à la force d'adversaire. \n"
          "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a\n"
          "lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire\n"
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se\n"
          "termine lorsque les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter\n"
          "chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")


def choix_1_normal():
    global nbr_vie
    global nbr_combat
    global combat_gagner
    global victoire_daffilee
    lancer_de_1 = random.randint(1, 6)
    lancer_de_2 = random.randint(1, 6)
    combiner_de = lancer_de_1 + lancer_de_2
    print("Vous avez eu", lancer_de_1, "et", lancer_de_2, "(", combiner_de, ")")
    print("Combat en cours")
    time.sleep(random.randint(0, 0))
    nbr_combat += 1
    if difficulte_adversaire < combiner_de:
        print("Vous avez GAGNER!")
        nbr_vie += difficulte_adversaire
        combat_gagner += 1
        victoire_daffilee += 1
    else:
        nbr_vie -= difficulte_adversaire
        print("Vous avez PERDUE!")
        victoire_daffilee = 0


def choix_1_boss():
    global nbr_vie
    global nbr_combat
    global combat_gagner
    global victoire_daffilee
    lancer_de_1 = random.randint(1, 6)
    lancer_de_2 = random.randint(1, 6)
    combiner_de = lancer_de_1 + lancer_de_2
    print("Vous avez eu", lancer_de_1, "et", lancer_de_2, "(", combiner_de, ")")
    print("Combat en cours")
    time.sleep(random.randint(0, 0))
    nbr_combat += 1
    if boss < combiner_de:
        print("Vous avez GAGNER!")
        nbr_vie += boss
        combat_gagner += 1
        victoire_daffilee = 0
    else:
        nbr_vie -= boss
        print("Vous avez PERDUE!")
        victoire_daffilee = 0


while True:
    difficulte_adversaire = random.randint(2, 9)
    boss = random.randint(10, 11)
    if nbr_vie < 1:
        print("Vous n'avez plus de vie apres", nbr_combat, "combat et vous avez gagner", combat_gagner, "combats!")
        rejouer = str(input("Voulez-vous rejouer? o/n_"))
        if rejouer == "o":
            nbr_vie = 20
            nbr_combat = 0
            combat_gagner = 0
        else:
            break
    else:
        if victoire_daffilee == 3:
            print("Vous tombez face à face avec un BOSS de difficulté", boss, "et\n"
                  "vous avez", nbr_vie, "vie")
            choix = int(input("Que voulez-vous faire?\n"
                              "   1- Combattre cet adversaire\n"
                              "   2- Afficher les regles du jeu\n"
                              "   3- Quitter la partie\n"
                              " "))
            if choix == 1:
                choix_1_boss()
            elif choix == 2:
                choix_3()
            else:
                print("Merci et au revoir...")
                break
        else:
            print("Vous tombez face à face avec un adversaire de difficulté", difficulte_adversaire, "et\n"
                  "vous avez", nbr_vie, "vie")
            choix = int(input("Que voulez-vous faire?\n"
                              "   1- Combattre cet adversaire\n"
                              "   2- Contourner cet adversaire et aller ouvrir une autre porte\n"
                              "   3- Afficher les regles du jeu\n"
                              "   4- Quitter la partie\n"
                              " "))
            if choix == 1:
                choix_1_normal()
            elif choix == 2:
                nbr_vie -= 1
            elif choix == 3:
                choix_3()
            else:
                print("Merci et au revoir...")
                break
