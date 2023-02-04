import pygame 
from settings_ import Settings
import sys



class Alieninvasion :
    def __init__(self) :
        pygame.init()
        #self.screen = pygame.display.set_mode((1200,800))
        self.settings= Settings()
        self.screen= pygame.display.set_mode((self.settings.screen_width, self.settings.screen_lenth))
        pygame.display.set_caption('Alien Invasion ')
        self.bg_color = (0 ,255,230)
    def run_game(self) :
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            pygame.display.flip()
            self.screen.fill(self.bg_color)
if __name__ == '__main__':
    ai=Alieninvasion()
    ai.run_game()