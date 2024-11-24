import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    astfield = AsteroidField()

    player1 = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
                    asteroid.split()

            if asteroid.collision(player1):
                print("Game over!")
                sys.exit()

        screen.fill((0, 0, 0))  # Заполняем экран черным цветом

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()    # Обновляем экран

        dt = clock.tick(165) / 1000


if __name__ == "__main__":
    main()
