import pygame
import random

class Food:

    def __init__(self):
        self.x = random.randint(40, 560)
        self.y = random.randint(40, 560)
        self.height = 40
        self.width = 40
        self.color = (51, 255, 51)
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move_food(self):
        self.rect.x = random.randint(40, 560)
        self.rect.y = random.randint(40, 560)