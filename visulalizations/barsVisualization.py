import pygame
import numpy as np
import wave
import sys

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
file_path = r'E:\projects\musicPlayerWithVisualization\sampleAudio\boom.wav'
wf = wave.open(file_path, 'rb')

# PyAudio setup
import pyaudio
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# Read audio data

def visulalization():
    global run
    data = wf.readframes(1024)
# Play audio
    if data:
        stream.write(data)
        data = wf.readframes(1024)
    else:
        run = False
    
    # Convert audio data to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)
    
    # Normalize audio data
    audio_data = audio_data / 32768.0
    
    # Clear screen
    screen.fill(BLACK)


    # Draw waveform
    for x in range(WIDTH):
        y = int(HEIGHT / 2 + audio_data[x % len(audio_data)] * (HEIGHT / 2))
        pygame.draw.line(screen, RED, (x, HEIGHT // 2), (x, y))



# Main function
def main():
    global run
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        visulalization()

  
        pygame.display.flip()

    pygame.quit()
    stream.stop_stream()
    stream.close()
    p.terminate()
    sys.exit()
# Run the main function
main()
