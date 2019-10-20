import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x_pos = 0
running = True
x, y = [], []
r, g, b = [], [], []
yy = []
i = -1
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())

drawing = False  # режим рисования выключен\

while running:
    x_pos += clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # Запоминаем координаты мыши
            x1, y1 = event.pos[0], event.pos[1]
            i = i + 1
            x.append(x1)
            y.append(y1)
            rr, gg, bb = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
            r.append(rr)
            g.append(gg)
            b.append(bb)
            pygame.draw.circle(screen, (r[i], g[i], b[i]), event.pos, 10)
            yy.append(y1)

    if x_pos >= 10:
        if i > -1:
            for j in range(i):
                if yy[j] < 300:
                    yy[j] = yy[j] + 1
                pygame.draw.circle(screen, (r[j], g[j], b[j]), (x[j], int(yy[j])), 10)
        x_pos = 0
        pygame.display.flip()
    screen.fill((0, 0, 0))
pygame.quit()