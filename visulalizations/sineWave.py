import pygame
import math
import time
pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
x0 = 0
y0 = HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wave visualization")



def main():
    run = True
    theta = 0
    x = 0
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    time.sleep(3)


        screen.fill(BLACK)

        for x in range(WIDTH):
            y = HEIGHT // 2  + 100 * math.sin(math.radians(x + theta))
            screen.set_at((x, int(y)), GREEN)


        theta = theta + 1 if theta < 360 else 0
        pygame.display.flip()

    pygame.quit()
main()