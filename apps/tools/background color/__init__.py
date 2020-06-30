def load(manager, params):
    pos = (100, 100);import pygame;import pygame_gui
    if params is not None and len(params) > 0:pos = params[0]
    pygame_gui.windows.UIColourPickerDialog(rect=pygame.Rect(pos, (600, 400)),manager=manager,window_title="Set Background Color",object_id="#desktop_colour_picker",)
