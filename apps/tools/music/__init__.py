import glob;import pygame;import pygame_gui;import os;from pygame import mixer
class Mixer(object):
    def __init__(self):mixer.init()
    @classmethod
    def load(cls, file):mixer.music.load(file)
    @classmethod
    def play(cls):mixer.music.play()
    @classmethod
    def pause(cls):cls.isPaused = True;mixer.music.pause()
    @classmethod
    def resume(cls):mixer.music.unpause()
    @classmethod
    def rewind(cls):mixer.music.rewind()
    @classmethod
    def stop(cls):mixer.music.stop()
    @classmethod
    def set_volume(cls, value):mixer.music.set_volume(value)
    @classmethod
    def get_volume(cls):return float(mixer.music.get_volume())
class MusicPlayer(pygame_gui.elements.UIWindow):
    DIMS = (400, 250)
    def __init__(self, pos, manager):
        super().__init__(pygame.Rect(pos, (self.DIMS[0] + 32, self.DIMS[1] + 60)),manager=manager,window_display_title="MusicPlayer",object_id="#musicplayer",);self.mixer = Mixer();app_path = '\\'.join(os.path.dirname(os.path.realpath(__file__)).split('\\')[:-3]);self.musics_path = app_path + "/musics";self.musics = glob.glob(self.musics_path + "/*.ogg");self.musics_dict = dict((music_path.split("/")[-1], music_path) for music_path in self.musics);self.isPaused = False;btns_names = ["play", "pause", "stop", "+", "-"];self.BSIZE = (self.DIMS[0] / len(btns_names), 30)
        for i, btn in enumerate(btns_names):self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((i % len(btns_names) * self.BSIZE[0], self.DIMS[1] - self.BSIZE[1]),self.BSIZE,),text=btn.upper(),manager=manager,container=self,object_id="#op-" + btn + "btn",);self.music_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0), (self.DIMS[0], self.DIMS[1] - self.BSIZE[1])),manager=manager,container=self,object_id="#op-musiclist",item_list=list(self.musics_dict.keys()),)
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-playbtn":selected_music = self.music_list.get_single_selection()
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-playbtn" and selected_music is None:music_path = next(iter(self.musics_dict.values()))
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-playbtn":music_path = self.musics_dict[selected_music]
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-playbtn" and self.isPaused:self.mixer.resume();self.isPaused = False
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-playbtn":self.mixer.load(music_path);self.mixer.play()
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-pausebtn":self.mixer.pause();self.isPaused = True
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-stopbtn":self.mixer.stop()
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op-+btn":volume = min((self.mixer.get_volume() + 0.1), 1.0);self.mixer.set_volume(value=volume)
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#musicplayer.#op--btn":volume = max((self.mixer.get_volume() - 0.1), 0.0);self.mixer.set_volume(value=volume)
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:return True
    def update(self, delta):super().update(delta)
    def kill(self):self.mixer.stop();super().kill()
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    MusicPlayer(pos, manager)
