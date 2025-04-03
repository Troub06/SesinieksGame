import pygame
from src.game import Game

def main():
    pass

if __name__ == "__main__":
    game = Game()
    game.main()

# class Game():
#     def __init__(self, width: int, height: int):
#         pygame.init()
#         self.screen = pygame.display.set_mode((width, height))
#         self.clock = pygame.time.Clock()
#         self.running = True

# game = Game(1280, 720)
# while game.running:
#     # poll for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game.running = False

#     # fill the screen with a color to wipe away anything from last frame
#     game.screen.fill("lightgreen")

#     # RENDER YOUR GAME HERE

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     game.clock.tick(60)  # limits FPS to 60

# pygame.quit()
