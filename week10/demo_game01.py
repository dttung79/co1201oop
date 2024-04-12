import pygame

class GameDemo:
    def __init__(self, caption, width, height, bgcolor):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.bgcolor = bgcolor
        self.speed = pygame.time.Clock() 
    def run(self):
        running = True
        x = 400
        y = 300
        moving = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN: # a key is pressed
                    if event.key == pygame.K_SPACE:  # if key is a space key
                        moving = not moving
            
            self.screen.fill(self.bgcolor)
            self.draw_circle((255, 0, 0), x, y, 50)
            pygame.display.update()
            self.speed.tick(30)
            if moving:
                if x + 50 < 800:
                    x += 10
                else:
                    x = 0
        pygame.quit()

    def draw_circle(self, color, x, y, r):
        pygame.draw.circle(self.screen, color, (x, y), r)

if __name__ == "__main__":
    game = GameDemo("Game Demo", 800, 600, (0, 255, 0))
    game.run()