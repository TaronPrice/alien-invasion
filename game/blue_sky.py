import sys
import pygame
from frank import Frank

class BlueSky:
    """open a blue window"""
    def __init__(self):
        """game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.frank = Frank(self)
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (255, 255, 255)
        

    def run_game(self):
        """start a loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.frank.blitme()
            pygame.display.flip()

if __name__ =='__main__':
    bs = BlueSky()
    bs.run_game()