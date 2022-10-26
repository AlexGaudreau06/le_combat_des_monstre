"""
Cree par Alex Gaudreau le 26./0.22
Code qui simule des combats de monstres avec des lancers de des.
"""
import random
import time
nbr_vie = 20
nbr_combat = 0
combat_gagner = 0
victoire_daffilee = 0


def choix_3():
    """
    Cette fonction donne les regles du jeu.
    :return:
    """
    print("Pour réussir un combat, il faut que la valeur du dé lancé est supérieure à la force d'adversaire. \n"
          "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a\n"
          "lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire\n"
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se\n"
          "termine lorsque les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter\n"
          "chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")


def choix_1_normal():
    """
    quand que le joueur clique 1 et il n'y a pas 3 victoire daffiler.
    Cette fonction fait tout le combat entre le joueur et l'enemi.
    :return:
    """
    global nbr_vie
    global nbr_combat
    global combat_gagner
    global victoire_daffilee
    lancer_de_1 = random.randint(1, 6)
    lancer_de_2 = random.randint(1, 6)
    combiner_de = lancer_de_1 + lancer_de_2
    print(f"Vous avez eu {lancer_de_1} et {lancer_de_2} ({combiner_de})")
    print("Combat en cours")
    time.sleep(random.randint(2, 6))
    nbr_combat += 1
    if combiner_difficulte_adversaire < combiner_de:
        print("Vous avez GAGNER!")
        nbr_vie += combiner_difficulte_adversaire
        combat_gagner += 1
        victoire_daffilee += 1
    else:
        nbr_vie -= combiner_difficulte_adversaire
        print("Vous avez PERDUE!")
        victoire_daffilee = 0


def choix_1_boss():
    """
    Quand que le joueur clique 1 et il a 3 victoire daffiler.
    Cette fonction fait rour le combat entre le joueur et le boss.
    :return:
    """
    global nbr_vie
    global nbr_combat
    global combat_gagner
    global victoire_daffilee
    lancer_de_1 = random.randint(1, 6)
    lancer_de_2 = random.randint(1, 6)
    combiner_de = lancer_de_1 + lancer_de_2
    print(f"Vous avez eu {lancer_de_1} et {lancer_de_2} ({combiner_de})")
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
    difficulte_adversaire_1 = random.randint(1, 5)
    difficulte_adversaire_2 = random.randint(1, 5)
    combiner_difficulte_adversaire = difficulte_adversaire_1 + difficulte_adversaire_2
    boss = random.randint(10, 11)
    if nbr_vie < 1:
        print(f"Vous n'avez plus de vie apres {nbr_combat} combat et vous avez gagner {combat_gagner} combats!")
        rejouer = str(input("Voulez-vous rejouer? o/n_"))
        if rejouer == "o":
            nbr_vie = 20
            nbr_combat = 0
            combat_gagner = 0
        else:
            break
    else:
        if victoire_daffilee == 3:
            print(f"Vous tombez face à face avec un BOSS de difficulté {boss} et\n"
                  f"vous avez {nbr_vie} vie")
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
            print(f"Vous tombez face à face de 2 adversaires de difficulté {difficulte_adversaire_1} et\n"
                  f"{difficulte_adversaire_2} ({combiner_difficulte_adversaire}) vous avez {nbr_vie} vie")
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
