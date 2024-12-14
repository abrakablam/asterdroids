import pygame
from constants import *
<<<<<<< HEAD

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
=======
from player import Player
>>>>>>> 2188b51 (adding players)


def main():
    pygame.init()
<<<<<<< HEAD
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()

=======
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # black RGB values

        player.draw(screen)
        pygame.display.flip()

        # limiting the framerate to 60 fps
        dt = clock.tick(60) / 1000

>>>>>>> 2188b51 (adding players)

if __name__ == "__main__":
    main()
