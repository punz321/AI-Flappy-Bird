import pygame

class Bird:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bird.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80)) #shrinking the brid
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = self.jump_strength

    def draw(self, screen):
        screen.blit(self.image, self.rect)