import numpy as np
import pygame
import getColor


def circle_visualization(screen, audio_data, background_color):
    if len(audio_data) == 0:
        return False
    centerX = screen.get_width() // 2
    centerY = screen.get_height() // 2
    radius = min(screen.get_width(), screen.get_height()) // 3
    audio_data = np.frombuffer(audio_data, dtype=np.int16)
    audio_data = audio_data / 32768.0

    num_points = len(audio_data)
    screen.fill(background_color)
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = int(centerX + radius * np.cos(angle))
        y = int(centerY + radius * np.sin(angle))
        audio_value = audio_data[i] * radius
        x_end = int(centerX + (radius + audio_value) * np.cos(angle))
        y_end = int(centerY + (radius + audio_value) * np.sin(angle))
        color = getColor.get_gradient_color(audio_value, -radius, radius)
        # color = getColor.get_rainbow_color(i, num_points)
        # color = getColor.get_random_color()
        # color = getColor.get_palette_color(i, num_points)
        pygame.draw.line(screen, color, (x, y), (x_end, y_end), 1)


    return True



