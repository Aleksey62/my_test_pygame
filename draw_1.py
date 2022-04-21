import pygame

pygame.init()

width, height = 400, 400
FPS = 30

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.draw.rect(window, (255, 0, 255), (100, 100, 200, 200))
pygame.draw.rect(window, (0, 0, 255), (100, 100, 200, 200), 5)
pygame.draw.polygon(window, (255, 255, 0), [(100, 100), (200, 50),
                                            (300, 100), (100, 100)])
pygame.draw.polygon(window, (0, 0, 255), [(100, 100), (200, 50),
                                          (300, 100), (100, 100)], 5)
pygame.draw.circle(window, (0, 255, 0), (200, 175), 50)
pygame.draw.circle(window, (255, 255, 255), (200, 175), 50, 5)
pygame.display.update()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
