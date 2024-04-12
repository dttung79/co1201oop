import pygame

class BasicGame:
    def __init__(self, caption, width, height, bgcolor):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.bgcolor = bgcolor
        self.speed = pygame.time.Clock()
        self.game_over = False
    def run(self):
        self.setup()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                
                self.handle_events(event)
            
            self.screen.fill(self.bgcolor)
            self.game_logic()
            pygame.display.update()
            self.speed.tick(30)
        pygame.quit()