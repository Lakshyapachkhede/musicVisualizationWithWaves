import pygame
import numpy as np
import getColor

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
        color = getColor.get_gradient_color(audio_data[x % screen.get_width()], -1, 1)
        pygame.draw.line(screen, color, (x, screen.get_height() // 2), (x, y))

    
    return True

