import numpy as np
import pygame
import getColor

def radial_bars(screen, audio_data, background_color):

    if len(audio_data) == 0:
        return False
    
    # Convert audio data to numpy array
    audio_data = np.frombuffer(audio_data, dtype=np.int16)
    
    # Normalize audio data
    audio_data = audio_data / 32768.0
    
    # Clear screen
    screen.fill(background_color)
    radius = min(screen.get_width(), screen.get_height()) // 3
    center_x, center_y = screen.get_width() // 2, screen.get_height() // 2
    num_bars = len(audio_data)
    
    for i in range(num_bars):
        angle = 2 * np.pi * i / num_bars
        audio_value = audio_data[i] * radius
        x_end = int(center_x + (radius + audio_value) * np.cos(angle))
        y_end = int(center_y + (radius + audio_value) * np.sin(angle))
        color = getColor.get_gradient_color(audio_value, -radius, radius)
        # color = getColor.get_rainbow_color(i, num_bars)
        # color = getColor.get_random_color()
        # color = getColor.get_palette_color(i, num_bars)
        pygame.draw.line(screen, color, (center_x, center_y), (x_end, y_end), 1)

    return True




