import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill((0, 0, 0))  # black RGB values

        player.draw(screen)
        pygame.display.flip()

        # limiting the framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
