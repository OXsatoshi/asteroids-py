import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from shot import Shot
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED 
from constants import  SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
class Player(CircleShape):

    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self,screen):
        x  = self.triangle()
        pygame.draw.polygon(screen,"WHITE",x,LINE_WIDTH,)
    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -=dt
        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        else:
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x,self.position.y)
            shot.velocity=pygame.Vector2(0,1)
            angle_of_rotation = shot.velocity.angle_to(self.velocity)
            shot.velocity = shot.velocity.rotate(self.rotation)
            shot.velocity.scale_to_length(PLAYER_SHOOT_SPEED)

