import pygame
import numpy as np
import wave
import sys
from visualizations import visualizations, getColor

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Wave Visualization")

# Load audio file
file_path = r'..\sampleAudio\fav.wav'
wf = wave.open(file_path, 'rb')

# PyAudio setup
import pyaudio
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# Read initial audio data




def main():
    global data, mode
    run = True
    clock = pygame.time.Clock()
    data = wf.readframes(1024)
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # if not visualizations.radial_bars(screen, data, BLACK):
        #     run = False

        # if not visualizations.bars_wave(screen, data, BLACK):
        #     run = False

        # if not visualizations.wave_dots(screen, data, BLACK):
        #     run = False

        # if not visualizations.circle_visualization(screen, data, BLACK):
        #     run = False

        if not visualizations.wave_visualization(screen, data, BLACK):
            run = False

        if len(data) > 0:
            stream.write(data)
            data = wf.readframes(1024)
        
        pygame.display.flip()

    pygame.quit()
    stream.stop_stream()
    stream.close()
    p.terminate()
    sys.exit()

# Run the main function
main()