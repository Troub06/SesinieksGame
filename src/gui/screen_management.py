import pygame
from src.gui.loading_screen import LoadingScreen

class ScreenManager():
    def __init__(self, screen):
        self.screen = screen
        self.loading_screen = LoadingScreen(self.screen)