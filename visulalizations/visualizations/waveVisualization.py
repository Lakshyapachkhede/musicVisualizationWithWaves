import numpy as np
import pygame
import getColor


def wave_visualization(screen, audio_data, background_color):
    if len(audio_data) == 0:
        return False
    
    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    audio_data = audio_data / 32768.0

    screen.fill(background_color)
    oldx = 0
    oldy = screen.get_height() // 2
    for x in range(screen.get_width()):
        y = int(screen.get_height() / 2 + audio_data[x % len(audio_data)] * (screen.get_height() / 2))
        # screen.set_at((x, y), GREEN)
        # color = getColor.get_gradient_color(audio_data[x % screen.get_screen.get_width()()], -1, 1)
        # color = getColor.get_rainbow_color(x, screen.get_screen.get_width()())
        color = getColor.get_random_color()
        # color = getColor.get_palette_color(x, screen.get_screen.get_width()())
        pygame.draw.line(screen, color, (oldx, oldy), (x, y), 2)
        oldx = x
        oldy = y

    return True



