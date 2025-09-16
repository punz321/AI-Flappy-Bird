import pygame
import sys
import random
from game.bird import Bird

class Pipe:
    GAP = 150  #gap between top and bottom pipes
    SPEED = 5  #how fast pipes move left

    def __init__(self, x, screen_height):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_WIDTH = 70

        #set random pipe height
        self.screen_height = (screen_height)

        self.pipe_top_img = pygame.transform.scale(pygame.image.load("assets/pipe_upside_down.png"),
                                                   (self.PIPE_WIDTH, screen_height))

        self.pipe_bot_img = pygame.transform.scale(pygame.image.load("assets/pipe.png"), 
                                                   (self.PIPE_WIDTH, screen_height))

        self.set_height(screen_height)

    def set_height(self, screen_height):
        self.height = random.randint(50, screen_height - self.GAP - 50)
        self.top = self.height
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.SPEED

    def draw(self, win, screen_height):
        #Top pipe (drawn upside down)
        win.blit(self.pipe_top_img, (self.x, self.top - self.pipe_top_img.get_height()))
        #Bottom pipe
        win.blit(self.pipe_bot_img, (self.x, self.bottom))

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, bird.WIDTH, bird.HEIGHT)
        top_pipe = pygame.Rect(self.x, 0, self.PIPE_WIDTH, self.top)
        bottom_pipe = pygame.Rect(self.x, self.bottom, self.PIPE_WIDTH, self.screen_height - self.bottom)

        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)

def run():
    pygame.init()

    screen_width, screen_height = 400, 600
    #window setup
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("AI Flappy Bird")

    clock = pygame.time.Clock()
    bird = Bird(400//2, 600//2)

    pipes = []
    spawn_timer = 0
    spawn_interval = 1500 #ms

    running = True
    while running:
        dt = clock.tick(60) #get delta time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()
    

        #bg
        screen.fill((135, 206, 250))  #light blue

        bird.update()
        bird.draw(screen)

        #pipe spawning
        spawn_timer += dt
        if spawn_timer > spawn_interval:
            pipes.append(Pipe(screen_width, screen_height))
            spawn_timer = 0

        for pipe in pipes[:]:
            pipe.move()
            pipe.draw(screen, screen_height)
            if pipe.x + pipe.PIPE_WIDTH < 0:
                pipes.remove(pipe)

        pygame.display.update()

    pygame.quit()
    sys.exit()