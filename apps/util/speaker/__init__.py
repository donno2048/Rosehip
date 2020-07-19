import threading;import pygame;import pygame_gui;from pygame_gui.elements import UILabel;from pygame_gui.elements import UITextEntryLine;import pyttsx3
class Speaker(pygame_gui.elements.UIWindow):
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (400, 128)),manager=manager,window_display_title="speaker",object_id="#speaker",);self.label = UILabel(relative_rect=pygame.Rect(-20, 10, 400, 20),text="",manager=manager,container=self,);self.input = UITextEntryLine(relative_rect=pygame.Rect(0, 40, 368, 30), manager=manager, container=self);self.engine = pyttsx3.init();self.engine.setProperty("rate", 150);self.speakthrd = None
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.USEREVENT and event.ui_element == self.input and event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and (self.speakthrd is None or not self.speakthrd.is_alive()) and self.input.get_text!="":self.engine.say(self.input.get_text);self.speakthrd = threading.Thread(target=self.engine.runAndWait, args=());self.speakthrd.start();self.label.set_text(self.input.get_text);self.input.set_text("")
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    Speaker(pos, manager)
