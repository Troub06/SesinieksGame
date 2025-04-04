from src.configs import *
from pygame import image

class Grid():
    def __init__(self, screen):
        self.screen = screen
        self.grid = image.load(grid_image)
        self.player_grid = image.load(player_grid_image)

    def draw_grid(self):
        self.screen.blit(self.grid, GRID_IMAGE_POSITION)
        self.screen.blit(self.player_grid, PLAYER_GRID_IMAGE_POSITION)