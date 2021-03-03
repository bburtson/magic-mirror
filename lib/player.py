import pygame
import os
import mutagen
import time
from random import *

class Player:
    def __init__(self):
        # os.system('amixer sset "PCM" 100%')
##        os.system('amixer -c 0 cset numid=3 2')
        pygame.mixer.init()
        self.library = {}
        self.now_playing = None
        self.base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.audio_dir = os.path.join(self.base_path, '../cache/audio')

    def _load_library(self):
        self.library = {}
        for file in os.listdir(self.audio_dir):
            filename = os.path.join(self.audio_dir, file)
            if self._verify_format(filename):
                self.library[filename] = self.audio_format(filename)

    def play(self):
        # reload the library each time in case the list has changed
        self._load_library()

        # If we have no music to play, don't play any music.
        if len(self.library.items()) == 0:
            return

        # If we're muted, don't play music
        if os.path.isfile(os.path.join(self.audio_dir, 'mute_audio.lock')):
            return

        filename, metadata = choice(list(self.library.items()))
        self._init_mixer(metadata)
        pygame.mixer.music.load(filename)
        self.now_playing = pygame.mixer.music.play(-1)

    # The mixer does not understand on its own how to play files at 48000Hz, etc.
    @staticmethod
    def _init_mixer(metadata):
        pygame.mixer.quit()
        frequency = int(metadata.sample_rate / metadata.channels)
        pygame.mixer.pre_init(frequency=frequency, channels=metadata.channels)
        pygame.mixer.init()

    @staticmethod
    def _verify_format(file):
        valid_format = True
        audio = mutagen.File(file)
        if type(audio) is not mutagen.mp3.MP3:
            valid_format = False

        return valid_format

    @staticmethod
    def audio_format(file):
        audio = mutagen.File(file)
        return audio.info

    @staticmethod
    def stop(fade_delay=3000):
        pygame.mixer.music.fadeout(fade_delay)
        time.sleep(fade_delay / 1000)
        pygame.mixer.music.stop()

    @staticmethod
    def is_busy():
        return pygame.mixer.music.get_busy()

