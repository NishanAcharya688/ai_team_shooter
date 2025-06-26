# ai_team_shooter/src/main.py
import pygame
import sys
from pathlib import Path
# Project root directory (for asset loading)
ROOT_DIR = Path(__file__).parent.parent
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AI Team Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self): pass
    def render(self): 
        self.screen.fill((100, 100, 100))
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    from utils.logger import setup_logging
    setup_logging()  # Initialize logging system
    
    game = Game()
    game.run()