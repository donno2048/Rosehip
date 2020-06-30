import os;import pygame;import pygame_gui;from pygame_gui.elements.ui_image import UIImage;from math import floor
class Dance(pygame_gui.elements.UIWindow):
    DIMS = (320, 240);FRAMES = [];FRAMES_LEN = 0;FRAME_INDEX = 0
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (self.DIMS[0] + 32, self.DIMS[1] + 60)),manager=manager,window_display_title="animation",object_id="#animation",);self.dsurf = UIImage(pygame.Rect((0, 0), self.DIMS),pygame.Surface(self.DIMS).convert(),manager=manager,container=self,parent_element=self,);app_path = os.path.dirname(os.path.abspath(__file__));frames_path = app_path + "/frames/";[self.FRAMES.append(pygame.transform.scale(pygame.image.load(frames_path + "frame-" + str(floor(x/2)) + ".png"), self.DIMS)) for x in range(len([name for name in os.listdir('.') if os.path.isfile(name)])*2+1)];self.FRAMES_LEN = len(self.FRAMES)
    def update(self, delta):super().update(delta);self.dsurf.image.blit(self.FRAMES[self.FRAME_INDEX], (0, 0));self.FRAME_INDEX = (self.FRAME_INDEX + 1) % self.FRAMES_LEN
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    Dance(pos, manager)
