import pygame
import pyaudio
import numpy as np
import wave
import sys
import wave



pygame.init()

# Constants
WIDTH = 800
HEIGHT = 400
FPS = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Wave Visualization")

# Load audio file
file_path = r'..\sampleAudio\youAreMyHeart.wav'
wf = wave.open(file_path, 'rb')

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)



def main():
    run = True
    clock = pygame.time.Clock()
    data = wf.readframes(1024)
    color = GREEN
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if data:
            stream.write(data)
            data = wf.readframes(1024)
        else:
            run = False

        audio_data = np.frombuffer(data, dtype=np.int16)
        audio_data = audio_data / 32768.0

        screen.fill(BLACK)

        for x in range(WIDTH):
            y = int(HEIGHT / 2 + audio_data[x % len(audio_data)] * (HEIGHT / 2))
            # screen.set_at((x, y), GREEN)
            pygame.draw.circle(screen, color, (x, y), 1)

                



        pygame.display.flip()

    pygame.quit()
    stream.stop_stream()
    stream.close()
    p.terminate()
    sys.exit()


main()



