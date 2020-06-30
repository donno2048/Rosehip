import pygame;import pygame_gui
class SnakeCalc(pygame_gui.elements.UIWindow):
    OPS = "789+" "456-" "123*" "p0=/" "C";BSIZE = (67, 75);USERCALC = ""
    def __init__(self, pos, manager):
        super().__init__(pygame.Rect(pos, (300, 475)),manager=manager,window_display_title="snakecalc",object_id="#snaketerm",resizable=True,);self.textbox = pygame_gui.elements.UITextBox("",relative_rect=pygame.Rect(0, 1, 268, 40),manager=manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},)
        for i in range(len(self.OPS)):
            op = self.OPS[i]
            if op == "x":continue
            pygame_gui.elements.UIButton(relative_rect=pygame.Rect((i % 4 * self.BSIZE[0], 40 + int(i / 4) * self.BSIZE[1]), self.BSIZE),text="." if op == "p" else op,manager=manager,container=self,object_id="#op-" + op,)
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:self.input_op(event.ui_object_id[-1]);return True
    def set_text(self, text):self.textbox.html_text = text;self.textbox.rebuild()
    def append_text(self, text):self.textbox.html_text = self.textbox.html_text + text;self.textbox.rebuild()
    def calculate(self, expression):
        result = ""
        try:result = str(eval(expression))
        except Exception:result = "Error"
        self.set_text(result)
    def input_op(self, op):
        if op in self.OPS and op == "=":self.calculate(self.textbox.html_text)
        elif op in self.OPS and op == "C":self.set_text("")
        elif op in self.OPS and op == "p":self.append_text(".")
        elif op in self.OPS:self.append_text(op)
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    SnakeCalc(pos, manager)
