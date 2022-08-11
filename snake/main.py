import sys
import random
import pygame


class Game:

    def __init__(self):
        width = 800
        height = 600
        self.screen = pygame.display.set_mode((width, height))  # dimension de l'écran
        pygame.display.set_caption("Snake Game")  # titre de la fenêtre

        self.gaming_mode = True  # vérification qu'on est bien en jeu

        self.snake_x = 300
        self.snake_y = 300
        self.snake_x_direction = 0
        self.snake_y_direction = 0
        self.snake_body = 15

        self.snack_x = None
        self.snack_y = None
        self.snack = 15

    def main(self):
        self.random_Snack()
        while self.gaming_mode:  # tant que je suis en jeu
            self.move()

            if self.snake_x <= 100 or self.snake_y >= 535 or self.snake_y <= 55 or self.snake_x >= 685:
                sys.exit()

            # déplacement du serpent
            self.snake_x += self.snake_x_direction
            self.snake_y += self.snake_y_direction

            if self.snack_x == self.snake_x and self.snack_y == self.snake_y:
                self.random_Snack()
                pass

            self.screen.fill((0, 0, 0))  # attribution d'une couleur à l'écran du jeu (code RGB)

            # Affichage serpent
            pygame.draw.rect(self.screen, (255, 0, 0), (self.snake_x, self.snake_y, self.snake_body, self.snake_body))

            # Affichage pomme
            pygame.draw.rect(self.screen, (0, 255, 0), (self.snack_x, self.snack_y, self.snack, self.snack))

            self.create_limit()
            pygame.display.flip()  # pour mettre à jour en continu l'écran par rapport aux modifications

    def move(self):
        for event in pygame.event.get():  # je récupère les évènements que je parcours un à un
            if event.type == pygame.QUIT:
                # si le type de l'évènement est celui pour quitter le jeu alors je ferme la fenêtre
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake_x_direction = 0.12
                    self.snake_y_direction = 0

                elif event.key == pygame.K_LEFT:
                    self.snake_x_direction = -0.12
                    self.snake_y_direction = 0

                elif event.key == pygame.K_UP:
                    self.snake_x_direction = 0
                    self.snake_y_direction = -0.12

                elif event.key == pygame.K_DOWN:
                    self.snake_x_direction = 0
                    self.snake_y_direction = 0.12

    def create_limit(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (100, 50, 600, 500), 3)

    def random_Snack(self):
        self.snack_x = random.randrange(110, 690, 10)
        self.snack_y = random.randrange(110, 590, 10)


def main():
    pygame.init()
    Game().main()
    pygame.quit()


if __name__ == "__main__":
    main()
