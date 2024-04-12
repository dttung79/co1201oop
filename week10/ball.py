import pygame
import random as rd
class Ball:
    def __init__(self, screen, color, r=10, speed=10):
        self.screen = screen
        self.color = color
        self.x = rd.randint(0, self.screen.get_width())
        self.y = 0
        self.r = r
        self.speed = speed
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
    
    def move(self):        
        if self.y + self.r <= self.screen.get_height():
            self.y += self.speed

    def reset(self):
        self.x = rd.randint(0, self.screen.get_width())
        self.y = 0
        