import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for o in updateable:
            o.update(dt)
        for o in drawable:
            o.draw(screen)

        for aster in asteroids:
            if(aster.is_colliding(player)):
                print("Game over!")
                return
            for shot in shots:
                if(aster.is_colliding(shot)):
                    shot.kill()
                    aster.split()

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()