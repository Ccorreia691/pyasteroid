import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    
    # set up game groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # create player object and initiate game loop
    gameExit = False
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while not gameExit:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #player.update(dt)
        updatable.update(dt)
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
            
       


if __name__ == "__main__":
    main()
