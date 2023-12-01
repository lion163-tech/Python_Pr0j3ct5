# Made by B0YM3R
# From a tutorial in python crash course book by

# Imports
import sys
import pygame
from settings import Settings

# Managing Director(class for all game assets)
class AlienInvasion:
    # Initializes game resources
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # Start main game loop
        while True:
            # Watch for input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(print('Game closed'))

                self.screen.fill(self.settings.bg_color)
                # Make the most recently drawn screen visible
                pygame.display.flip()
                self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
