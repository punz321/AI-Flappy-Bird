import pygame
import sys

def run():
    pygame.init()

    # window setup
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("AI Flappy Bird")

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # background
        screen.fill((135, 206, 250))  # sky blue

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()