from random import randint

choices = {1: "Pierre", 2: "Feuille", 3: "Ciseaux"}
player_score = 0
AI_score = 0


def random_choice():
    return randint(1, 3)


def nb_sleeve():
    try:
        return int(input("En combien de round voulez-vous jouer ?"))
    except ValueError:
        print("Seule les nombres entiers sont acceptés !:\n")
        nb_sleeve()


def situation(player_choice, AI_choice):
    if player_choice == AI_choice:
        print("Egalité\n")
    else:
        if player_choice == "Pierre":
            if AI_choice == "Feuille":
                print("L'ordinateur à gagné\n")
            else:
                print("Vous avez gagné\n")
        elif player_choice == "Feuille":
            if AI_choice == "Ciseaux":
                print("L'ordinateur à gagné\n")
            else:
                print("Vous avez gagné\n")
        elif player_choice == "Ciseaux":
            if AI_choice == "Pierre":
                print("L'ordinateur à gagné\n")
            else:
                print("Vous avez gagné\n")


def player_choice():
    choice = input("Que souhaitez-vous jouer entre : Pierre, Feuille ou Ciseaux ?\n")
    if choice == "Pierre" or choice == "Feuille" or choice == "Ciseaux":
        return choice
    print("Vos choix se limitent à : Pierre, Feuille ou Ciseaux\n")
    player_choice()


def main():
    nb_rounds = nb_sleeve()

    for i in range(nb_rounds):
        AI_choice = random_choice()
        pchoice = player_choice()
        print("1 2 3 Pierre Feuille Ciseaux")
        print("Ordinateur : " + choices[AI_choice])
        situation(pchoice, choices[AI_choice])


if __name__ == '__main__':
    main()
