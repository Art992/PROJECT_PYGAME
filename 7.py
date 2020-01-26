import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
pause_text = pygame.font.SysFont('Consolas', 32).render('Пауза', True, pygame.color.Color('White'))

RUNNING, PAUSE = 0, 1
state = RUNNING

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            break
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_z:
                state = PAUSE
            if i.key == pygame.K_x:
                state = RUNNING
    else:
        screen.fill((0, 0, 0))

        if state == RUNNING:
            pass

        elif state == PAUSE:
            screen.blit(pause_text, (100, 100))

        pygame.display.flip()
        clock.tick(60)
        continue
