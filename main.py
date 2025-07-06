import sys
from shot import Shot
import pygame # type: ignore
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    pygame.display.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        
        for item in drawable:
            item.draw(screen)
        
        for item in asteroids: 
            if item.collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collided(item):
                    shot.kill()
                    item.split()

        delta_time = clock.tick(60)
        dt = delta_time / 1000
        
        updatable.update(dt)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
