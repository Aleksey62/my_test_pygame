import pygame
pygame.init()

width, height = 400, 400
FPS = 30

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
