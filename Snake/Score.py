import pygame

from GameObject import GameObject

class Score(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 0
        self.text_color = (102, 255, 102)
        self.font = pygame.font.Font(None, 25)
        self.text_surface = self.font.render(f"{self.score}", True, self.text_color)
        self.text_rect = self.text_surface.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)