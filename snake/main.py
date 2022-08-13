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

        # position et direction du serpent
        self.snake_x = 300
        self.snake_y = 300
        self.snake_x_direction = 0
        self.snake_y_direction = 0
        self.snake_body = 15

        # coordonnée de la pomme
        self.snack_x = None
        self.snack_y = None
        self.snack = 15

        # fixation des fps
        # self.clock = pygame.time.Clock()

        # sauvegarde des positions du serpent
        self.snake_positions = []

        self.snake_height = 1

    def main(self):
        clock = pygame.time.Clock()
        self.random_snack()
        while self.gaming_mode:  # tant que je suis en jeu
            # pygame.time.delay(10)
            clock.tick(20)
            self.move()

            if self.snake_x <= 105 or self.snake_y >= 530 or self.snake_y <= 55 or self.snake_x >= 680:
                sys.exit()

            # déplacement du serpent
            self.snake_x += self.snake_x_direction
            self.snake_y += self.snake_y_direction

            if self.snack_x == self.snake_x and self.snack_y == self.snake_y:
                # choix aléatoire d'un nouvel emplacement de pomme
                self.random_snack()

                # augmentation taille du serpent
                self.snake_height += 1

            # liste qui stock les positions de la tête du serpent
            snake_head = [self.snake_x, self.snake_y]

            # ajout de la tête à la liste des positions du serpent, car il s'agit d'une partie de son corps
            self.snake_positions.append(snake_head)

            if len(self.snake_positions) > self.snake_height:
                self.snake_positions.pop(0)

            self.screen.fill((0, 0, 0))  # attribution d'une couleur à l'écran du jeu (code RGB)

            # Affichage serpent
            pygame.draw.rect(self.screen, (255, 0, 0), (self.snake_x, self.snake_y, self.snake_body, self.snake_body))

            # Affichage pomme
            pygame.draw.rect(self.screen, (0, 255, 0), (self.snack_x, self.snack_y, self.snack, self.snack))

            # Affichage corps
            for snake_part in self.snake_positions:
                pygame.draw.rect(self.screen, (255, 0, 0), (snake_part[0], snake_part[1], self.snake_body, self.snake_body))

            # si le serpent se mord la queue
            for snake_part in self.snake_positions[:-1]:  # on ne sélectionne pas la tête
                if snake_part == snake_head:
                    sys.exit()

            self.create_limit()
            pygame.display.flip()  # pour mettre à jour en continu l'écran par rapport aux modifications

    def move(self):
        for event in pygame.event.get():  # je récupère les évènements que je parcours un à un
            if event.type == pygame.QUIT:
                # si le type de l'évènement est celui pour quitter le jeu alors je ferme la fenêtre
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.snake_x_direction = 10
                    self.snake_y_direction = 0

                elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    self.snake_x_direction = -10
                    self.snake_y_direction = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_z:
                    self.snake_x_direction = 0
                    self.snake_y_direction = -10

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.snake_x_direction = 0
                    self.snake_y_direction = 10

    def create_limit(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (100, 50, 600, 500), 3)

    def random_snack(self):
        self.snack_x = random.randrange(110, 680, 10)
        self.snack_y = random.randrange(110, 530, 10)

    def message_box(self):
        pass

def main():
    pygame.init()
    Game().main()
    pygame.quit()


if __name__ == "__main__":
    main()
