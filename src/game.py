import pygame
from src.configs import *
from src.gui.screen_management import ScreenManager

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sešinieks")
        self.clock = pygame.time.Clock()
        self.running = True

        self.bg = pygame.image.load(loading_image)

    def main(self):
        while self.running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # RENDER YOUR GAME HERE
            self.gui = ScreenManager(self.screen)
            # self.screen.blit(self.bg, (0, 0))

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()
