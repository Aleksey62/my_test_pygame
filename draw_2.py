import pygame

pygame.init()

width, height = 400, 400
FPS = 30

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pi = 3.14
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.draw.rect(window, (0, 255, 0), (100, 100, 200, 300))
    pygame.draw.ellipse(window, (255, 255, 0), (100, 100, 200, 300))
    pygame.draw.arc(window, (255, 0, 0), (100, 100, 200, 150), 2 *pi, pi )
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()