import pygame

from Snake import Snake

if __name__ == "__main__":
    pygame.init()
    snake_instance = Snake()
    snake_instance.run_game()