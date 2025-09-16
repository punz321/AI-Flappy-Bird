import pygame
import sys
from game.bird import Bird

def run():
    pygame.init()

    # window setup
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("AI Flappy Bird")

    clock = pygame.time.Clock()
    bird = Bird(400//2, 600//2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()
    

        # background
        screen.fill((135, 206, 250))  # sky blue

        bird.update()
        bird.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()