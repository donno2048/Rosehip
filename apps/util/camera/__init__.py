import pygame;import os;import pygame_gui;from pygame_gui.elements.ui_image import UIImage;import cv2;import numpy;camera=cv2.VideoCapture(0,cv2.CAP_DSHOW);camera.set(3,640);camera.set(4,480)
class Camera(pygame_gui.elements.UIWindow):
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (352, 300)),manager=manager,window_display_title="camera",object_id="#camera",);self.dsurf = UIImage(pygame.Rect((0, 0),(320,240)),pygame.Surface((320,240)).convert(),manager=manager,container=self,parent_element=self,)
    def update(self, delta):super().update(delta);self.dsurf.image.blit(pygame.surfarray.make_surface(numpy.rot90(cv2.cvtColor(camera.read()[1],cv2.COLOR_BGR2RGB))), (0, 0))
def load(x,y):
    pos = (100, 100)
    if y is not None and len(y) > 0:pos = y[0]
    Camera(pos, x)
