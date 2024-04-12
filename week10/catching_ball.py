import pygame
from basic_game import BasicGame
from ball import Ball
from bar import Bar

class CatchBall(BasicGame):
    def __init__(self, caption, width, height, bgcolor, ball_color, bar_color):
        super().__init__(caption, width, height, bgcolor)
        self.ball = Ball(self.screen, ball_color)
        self.bar = Bar(self.screen, bar_color, 0, height - 20, 100, 20, 50)
    
    def setup(self):
        self.game_over = False
        self.score = 0
        # set bar in the middle of the screen
        self.bar.x = (self.screen.get_width() - self.bar.width) // 2
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.bar.move_left()
            if event.key == pygame.K_RIGHT:
                self.bar.move_right()
    
    def game_logic(self):
        if self.collided():
            self.score += 1
            self.ball.reset()
            if self.score == 5:
                self.game_over = True
                self.show_message('You win!')
        
        if self.ball.y + self.ball.r >= self.screen.get_height():
            self.game_over = True
            self.show_message('You loose!') 
        
        self.ball.move()
        self.ball.draw()
        self.bar.draw()
    
    def collided(self):
        h_collided = self.ball.x + self.ball.r >= self.bar.x and \
                        self.ball.x - self.ball.r <= self.bar.x + self.bar.width
        v_collided = self.ball.y + self.ball.r >= self.bar.y and \
                        self.ball.y - self.ball.r <= self.bar.y + self.bar.height

        return h_collided and v_collided

    def show_message(self, message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (0, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)

        pygame.time.wait(2000)
        pygame.display.update()

if __name__ == "__main__":
    game = CatchBall("Catch Ball", 800, 600, (255, 255, 255), (255, 0, 0), (0, 255, 0))
    game.run()