import sys
import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import * 
from shot import *

def main ():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    astroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if CircleShape.collision(asteroid, player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt += clock.tick(30) / 1000

if __name__ == "__main__":
    main()
