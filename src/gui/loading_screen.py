from src.configs import loading_image
from pygame import image, transform

class LoadingScreen():
    def __init__(self, screen):
        self.screen = screen
        self.loading_image = image.load(loading_image)
        self.loading_image = transform.scale(self.loading_image, (192, 192))

    def draw_loading(self):
        self.screen.blit(self.loading_image, (500, 500))
