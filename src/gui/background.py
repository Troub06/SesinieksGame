from src.configs import *
from pygame import image, transform

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.loading_image = image.load(loading_image)
        # self.loading_image = transform.scale(self.loading_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_background(self):
        self.screen.blit(self.loading_image, (0, 0))
