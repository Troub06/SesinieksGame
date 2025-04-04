import pygame
from src.gui.background import Background
from src.gui.grid import Grid

class ScreenManager():
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.background.draw_background()
        self.grid = Grid(self.screen)
        self.grid.draw_grid()
