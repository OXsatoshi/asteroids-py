import pygame
from constants import SCREEN_WIDTH 
from constants import SCREEN_HEIGHT 
import sys
from logger import log_state
from logger import log_event 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids =  pygame.sprite.Group()
    shots=  pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable) 
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") 
        for draw in drawable:
            draw.draw(screen)

        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if ast.collides_with(s):
                    log_event("asteroid_shot")
                    s.kill()
                    ast.split()

        updatable.update(dt)
        pygame.display.flip()
        dt = clock_object.tick(60)/1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
