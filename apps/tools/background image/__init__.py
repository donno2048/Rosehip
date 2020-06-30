def load(manager, params):
    pos = (30, 30);import pygame;import pygame_gui;import os
    if params is not None and len(params) > 0:pos = params[0]
    pygame_gui.windows.UIFileDialog(rect=pygame.Rect(pos, (600, 400)),manager=manager,window_title="Set Background Image",initial_file_path='\\'.join(os.path.dirname(os.path.realpath(__file__)).split('\\')[:-3])+'/images',object_id="#background_picker",)
