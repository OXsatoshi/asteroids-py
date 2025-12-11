from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event 
import random 
class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__(x,y,radius) 
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            rand_ang = random.uniform(20,50)
            vec1 = self.velocity.rotate(rand_ang) 
            vec2 = self.velocity.rotate(-rand_ang) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_astr = Asteroid(self.position.x,self.position.y,new_radius)
            first_astr.velocity=(1.2)*vec1
            
            second_astr= Asteroid(self.position.x,self.position.y,new_radius)

            second_astr.velocity=(1.2)*vec2
