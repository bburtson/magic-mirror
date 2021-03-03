
from lib.mirror_text import MirrorText
from lib.player import Player
import pygame


class App:
    def __init__(self, is_prod=False):
        pygame.init()
        inf = pygame.display.Info()
        pygame.mouse.set_visible(False)
        flags = pygame.FULLSCREEN if is_prod else pygame.RESIZABLE
        window = pygame.display.set_mode([inf.current_w, inf.current_h], flags)
        self.player = Player()
        self.text = MirrorText('', window)
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.player.play()
            self.text.run()
            self.is_running = True

    def stop(self):
        if self.is_running:
            try:
                Player.stop()
                self.text.stop()
                self.is_running = False
            except Exception as err:
                print("[App.stop(self)] threw an exception %d" % err)

    def exit(self):
        self.stop()
        while self.text.thr.isAlive():
            pygame.time.delay(10)
        pygame.quit()
