import pygame

class Bar:
    def __init__(self, screen, color, x, y, w, h, speed):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self):
        if self.x + self.width < self.screen.get_width():
            self.x += self.speed