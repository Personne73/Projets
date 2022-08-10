import sys
import random
import pygame


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))  # dimension de l'écran
        pygame.display.set_caption("Snake Game")  # titre de la fenêtre

        self.gaming_mode = True  # vérification qu'on est bien en jeu

    def main(self):
        while self.gaming_mode:  # tant que je suis en jeu
            for event in pygame.event.get():  # je récupère les évènements que je parcours un à un
                if event.type == pygame.QUIT:
                    # si le type de l'évènement est celui pour quitter le jeu alors je ferme la fenêtre
                    sys.exit()

            self.screen.fill((234, 225, 247))  # attribution d'une couleur à l'écran du jeu (code RGB)
            pygame.display.flip()  # pour mettre à jour en continu l'écran par rapport aux modifications


def main():
    pygame.init()
    Game().main()
    pygame.quit()


if __name__ == "__main__":
    main()
