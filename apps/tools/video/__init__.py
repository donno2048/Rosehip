import os,cv2;import pygame;import pygame_gui;from pygame_gui.elements.ui_image import UIImage;from math import floor;import numpy
class Video(pygame_gui.elements.UIWindow):
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (352,300)),manager=manager,window_display_title="Video",object_id="#video",);self.dsurf = UIImage(pygame.Rect((0, 0),(320, 240)),pygame.Surface((320, 240)).convert(),manager=manager,container=self,parent_element=self,);self.video=cv2.VideoCapture(os.path.dirname(os.path.abspath(__file__))+'\\video.mp4')
    def update(self, delta):
        super().update(delta)
        if not self.video.read()[0]:self.video=cv2.VideoCapture(os.path.dirname(os.path.abspath(__file__))+'\\video.mp4')
        else:self.dsurf.image.blit(pygame.surfarray.make_surface(numpy.rot90(cv2.cvtColor(cv2.cvtColor(self.video.read()[1],cv2.COLOR_RGB2BGR),cv2.COLOR_BGR2RGB))), (0, 0))
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    Video(pos, manager)
