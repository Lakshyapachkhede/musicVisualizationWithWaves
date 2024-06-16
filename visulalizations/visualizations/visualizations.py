import numpy as np
import pygame
from . import getColor

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




def bars_wave(screen, audio_data, background_color):

    if len(audio_data) == 0:
        return False
    
    # Convert audio data to numpy array
    audio_data = np.frombuffer(audio_data, dtype=np.int16)
    
    # Normalize audio data
    audio_data = audio_data / 32768.0
    
    # Clear screen
    screen.fill(background_color)
    
    # Draw waveform
    for x in range(screen.get_width()):
        y = int(screen.get_height() / 2 + audio_data[x % len(audio_data)] * (screen.get_height() / 2))
        # color = getColor.get_gradient_color(audio_data[x % screen.get_width()], -1, 1)
        color = getColor.get_rainbow_color(x, screen.get_width())
        # color = getColor.get_random_color()
        # color = getColor.get_palette_color(x, screen.get_width())
        pygame.draw.line(screen, color, (x, screen.get_height() // 2), (x, y))

    
    return True


def wave_dots(screen, audio_data, background_color):
    if len(audio_data) == 0:
        return False
    
    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    audio_data = audio_data / 32768.0

    screen.fill(background_color)
    for x in range(screen.get_width()):
            y = int(screen.get_height() / 2 + audio_data[x % len(audio_data)] * (screen.get_height() / 2))
            color = getColor.get_gradient_color(audio_data[x % screen.get_width()], -1, 1)
            # color = getColor.get_rainbow_color(x, screen.get_width())
            # color = getColor.get_random_color()
            # color = getColor.get_palette_color(x, screen.get_width())
            pygame.draw.circle(screen, color, (x, y), 1)

    return True



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
