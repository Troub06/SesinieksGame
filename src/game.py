import pygame
from src.configs import *
from src.gui.screen_management import ScreenManager

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def main(self):
        while self.running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("lightgreen")

            # RENDER YOUR GAME HERE
            self.guy = ScreenManager(self.screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()