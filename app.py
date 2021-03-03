
from lib.mirror_text import MirrorText
from lib.player import Player
import pygame
import sys


class App:
    def __init__(self, isProduction = False):
        pygame.init()
        info = pygame.display.Info()
        pygame.mouse.set_visible(False)
        if (isProduction):
            flags = pygame.FULLSCREEN
        else:
            flags = pygame.RESIZABLE
            
        win = pygame.display.set_mode([info.current_w,info.current_h], flags)
        self.player = Player()
        self.text = MirrorText('', win)
        self.isRunning = False
        
    def start(self):
        if(self.isRunning): return
        self.player.play()
        self.text.run()
        self.isRunning = True
##        while self.isRunning:
##            pygame.time.delay(10)
##            for e in pygame.event.get():
##                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
##                    self.exit()
        
    def stop(self):
        if(self.isRunning):
            try:
                Player.stop()
                self.text.stop()
                self.isRunning = False
            except Exception as err:
                print("Stop app threw an exception %d" % err)
        
        
    def exit(self):
        self.stop()
        while self.text.thr.isAlive():
            pygame.time.delay(10)
        pygame.quit()    
