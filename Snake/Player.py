import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self):
        self.x = 275
        self.y = 275
        self.width = 50
        self.height = 50
        self.color = (51, 255, 51)
        self.snake = [pygame.Rect(self.x, self.y, self.width, self.height)]

    def draw(self, screen):
        for snake_parts in self.snake:
            pygame.draw.rect(screen, self.color, snake_parts)

    def update(self):
        pass