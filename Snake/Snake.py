import pygame
import sys

from Player import Player
from Food import Food
from Score import Score

class Snake:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.screen_height = 600
        self.screen_width = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_background_color = (5, 18, 8)

        self.player = Player()
        self.food = Food()
        self.score = Score()

    def draw(self):
        self.screen.fill(self.screen_background_color)

        self.player.draw(self.screen)
        self.food.draw(self.screen)
        self.score.draw(self.screen)

        pygame.display.update()

    def run_game(self):
        running = True

        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.move()

            self.draw()

        pygame.quit()
        sys.exit()