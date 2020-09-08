import os,sys,threading,keyboard,pygame,pygame_gui,importlib;sys.dont_write_bytecode=True;os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1';from win32gui import GetWindowText, GetForegroundWindow;from pygame_gui.elements import UIPanel,UIButton;PANEL_LAYER = 10;BUTTON_DIMS = (200, 25);pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(__file__),'image.jpg')))
class Menu(UIPanel):
    manager = None;pos = None;path = None;child = None;elements = None
    def __init__(self, manager, pos, path, elements, loadfunc):super().__init__(pygame.Rect((pos[0] * BUTTON_DIMS[0], pos[1] * BUTTON_DIMS[1]),(BUTTON_DIMS[0] + 5, BUTTON_DIMS[1] * len(elements.keys()) + 5),),starting_layer_height=PANEL_LAYER,manager=manager,);self.pos = pos;self.path = path;self.elements = elements;self.loadfunc = loadfunc;ekeys = list(elements.keys());[UIButton(pygame.Rect((0, i * BUTTON_DIMS[1]), BUTTON_DIMS),text=ekeys[i],manager=manager,container=self,object_id="menu-" + self.path.replace(".", "-"),) for i in range(len(ekeys))]
    def process_event(self, event):
        if event.type != pygame.USEREVENT:return
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == ("panel.menu-" + self.path.replace(".", "-")):uitext = event.ui_element.text
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == ("panel.menu-" + self.path.replace(".", "-")) and self.elements[uitext] == None:self.loadfunc(self.path + "." + uitext)
        if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED and event.ui_object_id == ("panel.menu-" + self.path.replace(".", "-")):uitext = event.ui_element.text
        if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED and event.ui_object_id == ("panel.menu-" + self.path.replace(".", "-")) and self.elements[uitext] != None and self.child is not None:self.child.destroy()
        if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED and event.ui_object_id == ("panel.menu-" + self.path.replace(".", "-")) and self.elements[uitext] != None:self.child = Menu(self.ui_manager,(self.pos[0] + 1, list(self.elements.keys()).index(uitext)),self.path + "." + uitext,self.elements[uitext],self.loadfunc,)
    def destroy(self):
        if self.child is not None:self.child.destroy();self.child = None
        self.kill()
class OS:
    SCREEN = None;DIMS = None;BG = None;MANAGER = None;BG_COLOR = (255, 128, 0);PAINT = False;PAINT_RADIUS = 10;PAINT_COLOR = 0;PAINT_COLOR_LIST = [(255, 255, 255),(192, 192, 192),(128, 128, 128),(0, 0, 0),(0, 255, 0),(0, 128, 0),(128, 128, 0),(0, 128, 128),(255, 0, 0),(128, 0, 0),(128, 0, 128),(255, 0, 255),(0, 0, 255),(0, 0, 128),(0, 255, 255),(255, 255, 0),];PAINT_SHAPE = 0;NUM_SHAPES = 3;FOCUS = None;APPS = {};APPMENU = None
    def __init__(self):apps_path = os.path.dirname(os.path.abspath(__file__)) + "/apps";OS.iter_dir(self.APPS, apps_path);pygame.init();pygame.display.set_caption('my os');os.putenv("SDL_FBDEV", "/dev/fb0");pygame.display.init();self.DIMS = (pygame.display.Info().current_w, pygame.display.Info().current_h);self.SCREEN = pygame.display.set_mode(self.DIMS, pygame.FULLSCREEN);self.BG = pygame.Surface((self.DIMS));self.BG.fill(self.BG_COLOR);self.BRUSH_SURF = pygame.Surface((self.DIMS), flags=pygame.SRCALPHA);self.BRUSH_SURF.fill((0, 0, 0, 0));self.MANAGER = pygame_gui.UIManager(self.DIMS);pygame.mouse.set_visible(True);pygame.display.update()
    def iter_dir(tree, path):
        for f in os.listdir(path):
            if os.path.isfile(path + "/" + f + "/__init__.py"):tree[f] = None
            elif os.path.isdir(path + "/" + f):tree[f] = {};OS.iter_dir(tree[f], path + "/" + f)
    def appmenu_load(self, app,params=None):
        if self.APPMENU is not None:self.APPMENU.destroy();self.APPMENU = None
        importlib.import_module(app).load(self.MANAGER, params)
    def set_bg_color(self, color):self.BG = pygame.Surface((self.DIMS));self.BG_COLOR = color;self.BG.fill(self.BG_COLOR)
    def set_bg_image(self, file):
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".jpg" or file_extension == ".png":self.BG = pygame.transform.scale(pygame.image.load(file), self.DIMS)
    def run(self):
        clock = pygame.time.Clock();running = True
        while running:
            delta = clock.tick(60) / 1000.0;pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_HOME and self.APPMENU is None:self.APPMENU = Menu(self.MANAGER,(0, 0),"apps",self.APPS,self.appmenu_load,)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_HOME:self.APPMENU.destroy();self.APPMENU = None
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_INSERT:self.PAINT = not self.PAINT;self.BRUSH_SURF.fill((0, 0, 0, 0))
                if not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and event.button == 4 and  pressed[pygame.K_LALT]:self.PAINT_COLOR = (self.PAINT_COLOR + 1) % len(self.PAINT_COLOR_LIST)
                elif not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and event.button == 4 and pressed[pygame.K_LCTRL]:self.PAINT_SHAPE = (self.PAINT_SHAPE + 1) % self.NUM_SHAPES
                elif not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and event.button == 4:self.PAINT_RADIUS += 2
                if not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and event.button == 5 and event.button != 4 and pressed[pygame.K_LALT]:self.PAINT_COLOR = (self.PAINT_COLOR - 1) % len(self.PAINT_COLOR_LIST)
                elif not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and event.button == 5 and event.button != 4 and pressed[pygame.K_LCTRL]:self.PAINT_SHAPE = (self.PAINT_SHAPE - 1) % self.NUM_SHAPES
                elif not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and event.button == 5 and event.button != 4:self.PAINT_RADIUS -= 2
                if not event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and self.PAINT and self.PAINT_RADIUS < 2 and event.button == 5 and event.button != 4:self.PAINT_RADIUS = 2
                if event.type == pygame.USEREVENT and not event.type == pygame.KEYDOWN and not event.type == pygame.MOUSEBUTTONDOWN and event.user_type == "window_selected" and self.FOCUS is not None:self.FOCUS.unfocus()
                if event.type == pygame.USEREVENT and not event.type == pygame.KEYDOWN and not event.type == pygame.MOUSEBUTTONDOWN and event.user_type == "window_selected":self.FOCUS = event.ui_element;self.FOCUS.focus()
                elif event.type == pygame.USEREVENT and not event.type == pygame.KEYDOWN and not event.type == pygame.MOUSEBUTTONDOWN and event.user_type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED and event.ui_object_id == "#desktop_colour_picker":self.set_bg_color(event.colour[:-1])
                elif event.type == pygame.USEREVENT and not event.type == pygame.KEYDOWN and not event.type == pygame.MOUSEBUTTONDOWN and event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED and event.ui_object_id == "#background_picker":self.set_bg_image(event.text)
                self.MANAGER.process_events(event)
            self.MANAGER.update(delta)
            if self.PAINT:mpos = pygame.mouse.get_pos();draw_surf = self.BRUSH_SURF
            if self.PAINT and pygame.mouse.get_pressed()[0]:draw_surf = self.BG
            if self.PAINT and self.PAINT_SHAPE == 0:pygame.draw.circle(draw_surf,self.PAINT_COLOR_LIST[self.PAINT_COLOR],mpos,self.PAINT_RADIUS,)
            elif self.PAINT and self.PAINT_SHAPE == 1:pygame.draw.rect(draw_surf,self.PAINT_COLOR_LIST[self.PAINT_COLOR],pygame.Rect((mpos[0] - self.PAINT_RADIUS, mpos[1] - self.PAINT_RADIUS),(self.PAINT_RADIUS * 2, self.PAINT_RADIUS * 2),),)
            elif self.PAINT and self.PAINT_SHAPE == 2:pygame.draw.polygon(draw_surf,self.PAINT_COLOR_LIST[self.PAINT_COLOR],((mpos[0] - self.PAINT_RADIUS, mpos[1] + self.PAINT_RADIUS),(mpos[0] + self.PAINT_RADIUS, mpos[1] + self.PAINT_RADIUS),(mpos[0], mpos[1] - self.PAINT_RADIUS),),)
            if self.PAINT:self.SCREEN.blit(self.BG, (0, 0));self.SCREEN.blit(self.BRUSH_SURF, (0, 0));self.BRUSH_SURF.fill((0, 0, 0, 0))
            if not self.PAINT:self.SCREEN.blit(self.BG, (0, 0))
            self.MANAGER.draw_ui(self.SCREEN);pygame.display.update()
def switch():
    window = GetWindowText(GetForegroundWindow());keyboard.send('alt+tab')
    while GetWindowText(GetForegroundWindow()) in [window,"Task Switching",""]:pass
    keyboard.send('alt+F4')
if len(sys.argv)!=1:threading.Thread(target=switch).start()
OS().run()
