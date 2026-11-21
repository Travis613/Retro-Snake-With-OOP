import pygame

class Player:
    def __init__(self):
        self.x = 275
        self.y = 275
        self.width = 50
        self.height = 50
        self.speed = 3
        self.color = (51, 255, 51)
        self.direction = "down"
        self.last_point = {"axis": "y", "direction": "down"}
        self.snake = [pygame.Rect(self.x, self.y, self.width, self.height)]

    def draw(self, screen):
        for snake_parts in self.snake:
            pygame.draw.rect(screen, self.color, snake_parts, width=3)

    def move_head(self):
        if self.direction == "up":
            self.snake[0].y -= self.speed
        elif self.direction == "down":
            self.snake[0].y += self.speed
        elif self.direction == "right":
            self.snake[0].x += self.speed
        elif self.direction == "left":
            self.snake[0].x -= self.speed

    def add_another_snake_part(self):
        if self.last_point["axis"] == "x" and self.last_point["direction"] == "right":
            self.snake.append(pygame.Rect(self.x - self.width, self.y, self.height, self.width))
        elif self.last_point["axis"] == "x" and self.last_point["direction"] == "left":
            self.snake.append(pygame.Rect(self.x + self.width, self.y, self.height, self.width))
        if self.last_point["axis"] == "y" and self.last_point["direction"] == "up":
            self.snake.append(pygame.Rect(self.x, self.y + self.height, self.width, self.height))
        if self.last_point["axis"] == "y" and self.last_point["direction"] == "down":
            self.snake.append(pygame.Rect(self.x, self.y - self.height, self.width, self.height))