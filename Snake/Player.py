import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self):
        self.x = 275
        self.y = 275
        self.width = 50
        self.height = 50
        self.color = (51, 255, 51)
        self.last_point = {"axis": "y", "direction": "down"}
        self.snake = [pygame.Rect(self.x, self.y, self.width, self.height)]

    def draw(self, screen):
        for snake_parts in self.snake:
            pygame.draw.rect(screen, self.color, snake_parts, width=3)

    def update(self):
        if self.last_point["axis"] == "x" and self.last_point["direction"] == "right":
            self.snake.append(pygame.Rect(self.x - self.width, self.y, self.height, self.width))
        elif self.last_point["axis"] == "x" and self.last_point["direction"] == "left":
            self.snake.append(pygame.Rect(self.x + self.width, self.y, self.height, self.width))
        if self.last_point["axis"] == "y" and self.last_point["direction"] == "up":
            self.snake.append(pygame.Rect(self.x, self.y + self.height, self.width, self.height))
        if self.last_point["axis"] == "y" and self.last_point["direction"] == "down":
            self.snake.append(pygame.Rect(self.x, self.y - self.height, self.width, self.height))