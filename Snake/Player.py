import pygame

class Player:
    def __init__(self):
        self.x = 275
        self.y = 275
        self.width = 50
        self.height = 50
        self.speed = 3
        self.color = (51, 255, 51)
        self.last_point = {"axis": "y", "direction": "down"}
        self.snake = [pygame.Rect(self.x, self.y, self.width, self.height)]

    def draw(self, screen):
        for snake_parts in self.snake:
            pygame.draw.rect(screen, self.color, snake_parts, width=3)

    def move(self):
        for snake_parts in self.snake:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_w]:
                snake_parts.y -= self.speed
            elif pressed_keys[pygame.K_s]:
                snake_parts.y += self.speed
            elif pressed_keys[pygame.K_d]:
                snake_parts.x += self.speed
            elif pressed_keys[pygame.K_a]:
                snake_parts.x -= self.speed

    def add_another_snake_part(self):
        if self.last_point["axis"] == "x" and self.last_point["direction"] == "right":
            self.snake.append(pygame.Rect(self.x - self.width, self.y, self.height, self.width))
        elif self.last_point["axis"] == "x" and self.last_point["direction"] == "left":
            self.snake.append(pygame.Rect(self.x + self.width, self.y, self.height, self.width))
        if self.last_point["axis"] == "y" and self.last_point["direction"] == "up":
            self.snake.append(pygame.Rect(self.x, self.y + self.height, self.width, self.height))
        if self.last_point["axis"] == "y" and self.last_point["direction"] == "down":
            self.snake.append(pygame.Rect(self.x, self.y - self.height, self.width, self.height))