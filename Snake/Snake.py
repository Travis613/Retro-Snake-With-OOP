import pygame
import sys

class Snake:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_height = 600
        self.screen_width = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_background_color = (12, 34, 20)

    def draw(self):
        self.screen.fill(self.screen_background_color)
        pygame.display.update()

    def runGame(self):
        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()

        pygame.quit()
        sys.exit()

snake_instance = Snake()
snake_instance.runGame()