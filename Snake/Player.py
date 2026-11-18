import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self):
        self.snake = [pygame.Rect(275, 275, 50, 50)]
        self.color = (51, 255, 51)

    def draw(self, screen):
        for snake_parts in self.snake:
            pygame.draw.rect(screen, self.color, snake_parts)