import pygame

class GameDemo:
    def __init__(self, caption, width, heigt, bgcolor):
        pygame.init()
        self.screen = pygame.display.set_mode((width, heigt))
        pygame.display.set_caption(caption)
        self.bgcolor = bgcolor
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.bgcolor)
            self.draw_circle((255, 0, 0), 400, 300, 50)
            pygame.display.update()
        pygame.quit()

    def draw_circle(self, color, x, y, r):
        pygame.draw.circle(self.screen, color, (x, y), r)

if __name__ == "__main__":
    game = GameDemo("Game Demo", 800, 600, (0, 255, 0))
    game.run()