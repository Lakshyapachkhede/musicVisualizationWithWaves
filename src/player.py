import pyaudio
import wave
import threading
import time
import numpy as np
import pygame
import sys


pygame.init()

# Constants
WIDTH = 800
HEIGHT = 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Wave Visualization")
clock = pygame.time.Clock()

class AudioPlayer:
    def __init__(self, file, screen):
        self.screen = screen
        self.file = file
        self.wf = wave.open(self.file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                  channels=self.wf.getnchannels(),
                                  rate=self.wf.getframerate(),
                                  output=True)
        self.data = self.wf.readframes(1024)
        self.playing = threading.Event()
        self.paused = threading.Event()
        self.stop_flag = False

    def play(self):
        self.playing.set()
        self.paused.clear()
        threading.Thread(target=self._play_audio).start()
        threading.Thread(target=self.visulalization, args=(BLACK, RED)).start()


    def _play_audio(self):
        self.wf.rewind()

        while self.data and not self.stop_flag:
            if self.paused.is_set():
                time.sleep(0.1)
                continue
            self.stream.write(self.data)
            self.data = self.wf.readframes(1024)
        self.playing.clear()

    def pause(self):
        self.paused.set()

    def resume(self):
        self.paused.clear()

    def stop(self):
        self.stop_flag = True
        self.playing.clear()
        self.paused.set()
        time.sleep(0.1)
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        pygame.quit()
        sys.exit()

    def seek(self, seconds):
        self.wf.setpos(int(seconds * self.wf.getframerate()))

    
    def visulalization(self, background_color, visulaization_color):
        
        while not self.stop_flag:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    return

            if self.data:
                # Convert audio data to numpy array
                audio_data = np.frombuffer(self.data, dtype=np.int16)
            
                # Normalize audio data
                audio_data = audio_data / 32768.0
                
                # Clear screen
                self.screen.fill(background_color)
                
                # Draw waveform
                for x in range(self.screen.get_width()):
                    y = int(self.screen.get_height() / 2 + audio_data[x % len(audio_data)] * (self.screen.get_height() / 2))
                    pygame.draw.line(self.screen, visulaization_color, (x, self.screen.get_height() // 2), (x, y))

            pygame.display.flip()

    # def controls(self):
        

# Example usage
audio_player = AudioPlayer(r'..\sampleAudio\brotherlouie98.wav', screen)
audio_player.play()

# time.sleep(5)  # Play for 5 seconds
# audio_player.pause()
# time.sleep(2)  # Pause for 2 seconds
# audio_player.resume()
# time.sleep(5)  # Play for 5 more seconds
# audio_player.seek(10)  # Seek to 10 seconds
# time.sleep(5)  # Play for 5 seconds from 10 seconds mark
# audio_player.stop()
