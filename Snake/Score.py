import pygame

class Score:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 0
        self.text_color = (102, 255, 102)
        self.font = pygame.font.Font(None, 25)

    def draw(self, screen):
        text_surface = self.font.render(f"{self.score}", True, self.text_color)
        text_rect = text_surface.get_rect(topleft=(self.x, self.y))
        screen.blit(text_surface, text_rect)

    def increment_score(self):
        self.score += 5