import sys;import io;from js2py import eval_js;import os;os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide";import pygame;from io import StringIO;pygame.init();pygame.display.set_caption('python');font = pygame.font.Font(None, 32);clock = pygame.time.Clock();input_box = pygame.Rect(100, 100, 140, 32);out_box=pygame.Rect(100,200, 140, 32);from pygame_gui.elements import UIWindow;from pygame_gui.elements import UITextBox;from pygame_gui.elements import UITextEntryLine;from pygame_gui.elements import UITextBox;import pygame_gui;import concurrent.futures
class py(UIWindow):
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (400, 300)), manager, window_display_title="javascript", object_id="#js",resizable=True);self.textbox = pygame_gui.elements.UITextBox("",relative_rect=pygame.Rect(0, 0, 368, 200),manager=manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},);self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, -35, 368, 30),manager=manager,container=self,anchors={"left": "left","right": "right","top": "bottom","bottom": "bottom",},);self.text='';self.manager=manager;self.input.focus()
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            try:self.text+='<br>'+eval_js(self.input.get_text().replace('document.write','return ').replace('|','\n')).replace('\n','<br>')
            except:self.text+='<br>'+str(sys.exc_info()[1])
            self.input.kill();self.textbox.kill();self.textbox = pygame_gui.elements.UITextBox(self.text,relative_rect=pygame.Rect(0, 0, 368, 200),manager=self.manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},);self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, -35, 368, 30),manager=self.manager,container=self,anchors={"left": "left","right": "right","top": "bottom","bottom": "bottom",},);self.input.focus()
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    py(pos, manager)
