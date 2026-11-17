import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self):
        self.rect = pygame.Rect(275, 275, 50, 50)
        self.color = (51, 255, 51)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)