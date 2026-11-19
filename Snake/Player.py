import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self):
        self.x = 275
        self.y = 275
        self.width = 50
        self.height = 50
        self.color = (51, 255, 51)
        self.direction_moving = {"axis": "y", "direction": "down"}
        self.snake = [pygame.Rect(self.x, self.y, self.width, self.height)]

    def draw(self, screen):
        for snake_parts in self.snake:
            pygame.draw.rect(screen, self.color, snake_parts)

    def update(self):
        if self.direction_moving["axis"] == "x" and self.direction_moving["direction"] == "right":
            self.snake.append(pygame.Rect(self.x - self.width, self.y, self.height, self.width))
        elif self.direction_moving["axis"] == "x" and self.direction_moving["direction"] == "left":
            self.snake.append(pygame.Rect(self.x + self.width, self.y, self.height, self.width))
        if self.direction_moving["axis"] == "y" and self.direction_moving["direction"] == "up":
            self.snake.append(pygame.Rect(self.x, self.y + self.height, self.width, self.height))
        if self.direction_moving["axis"] == "y" and self.direction_moving["direction"] == "down":
            self.snake.append(pygame.Rect(self.x, self.y - self.height, self.width, self.height))