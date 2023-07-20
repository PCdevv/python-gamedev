import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

pygame.quit()
