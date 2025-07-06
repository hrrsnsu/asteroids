import pygame # type: ignore
from constants import * 
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.container = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        
        for item in drawable:
            item.draw(screen)
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        updatable.update(dt)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
