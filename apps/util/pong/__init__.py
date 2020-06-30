import pygame;import pygame_gui;from pygame_gui.ui_manager import UIManager;from pygame_gui.elements.ui_window import UIWindow;from pygame_gui.elements.ui_image import UIImage;from pygame.locals import *;import math;import random
class Score:
    def __init__(self, font):self.player_1_score = 0;self.player_2_score = 0;self.font = font;self.score_string = None;self.score_text_render = None;self.update_score_text()
    def update_score_text(self):self.score_string = str(self.player_1_score) + " - " + str(self.player_2_score);self.score_text_render = self.font.render(self.score_string, True, pygame.Color(200, 200, 200))
    def render(self, screen, size):screen.blit(self.score_text_render,self.score_text_render.get_rect(centerx=size[0] / 2, centery=size[1] / 10),)
    def increase_player_1_score(self):self.player_1_score += 1;self.update_score_text()
    def increase_player_2_score(self):self.player_2_score += 1;self.update_score_text()
class ControlScheme:
    def __init__(self):self.up = K_UP;self.down = K_DOWN
class Bat:
    def __init__(self, start_pos, control_scheme, court_size):self.control_scheme = control_scheme;self.move_up = False;self.move_down = False;self.move_speed = 450.0;self.court_size = court_size;self.length = 30.0;self.width = 5.0;self.position = [float(start_pos[0]), float(start_pos[1])];self.rect = pygame.Rect((start_pos[0], start_pos[1]), (self.width, self.length));self.colour = pygame.Color("#FFFFFF")
    def process_event(self, event):
        if event.type == KEYDOWN and event.key == self.control_scheme.up:self.move_up = True
        if event.type == KEYDOWN and event.key == self.control_scheme.down:self.move_down = True
        if event.type == KEYUP and event.key == self.control_scheme.up:self.move_up = False
        if event.type == KEYUP and event.key == self.control_scheme.down:self.move_down = False
    def update(self, dt):
        if self.move_up:self.position[1] -= dt * self.move_speed
        if self.move_up and self.position[1] < 10.0:self.position[1] = 10.0
        if self.move_up:self.rect.y = self.position[1]
        if self.move_down:self.position[1] += dt * self.move_speed
        if self.move_down and self.position[1] > self.court_size[1] - self.length - 10:self.position[1] = self.court_size[1] - self.length - 10
        if self.move_down:self.rect.y = self.position[1]
    def render(self, screen):pygame.draw.rect(screen, self.colour, self.rect)
class Ball:
    def __init__(self, start_position):self.rect = pygame.Rect(start_position, (5, 5));self.colour = pygame.Color(255, 255, 255);self.position = [float(start_position[0]), float(start_position[1])];self.start_position = [self.position[0], self.position[1]];self.ball_speed = 120.0;self.max_bat_bounce_angle = 5.0 * math.pi / 12.0;self.collided = False;self.velocity = [0.0, 0.0];self.create_random_start_vector()
    def render(self, screen):pygame.draw.rect(screen, self.colour, self.rect)
    def create_random_start_vector(self):
        y_random = random.uniform(-0.5, 0.5);x_random = 1.0 - abs(y_random)
        if random.randint(0, 1) == 1:x_random = x_random * -1.0
        self.velocity = [x_random * self.ball_speed, y_random * self.ball_speed]
    def reset(self):self.position = [self.start_position[0], self.start_position[1]];self.create_random_start_vector()
    def update(self, dt, bats, walls):
        self.position[0] += self.velocity[0] * dt;self.position[1] += self.velocity[1] * dt;self.rect.x = self.position[0];self.rect.y = self.position[1];collided_this_frame = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):collided_this_frame = True
            if self.rect.colliderect(wall.rect) and not self.collided:self.collided = True;self.velocity[1] = self.velocity[1] * -1
        for bat in bats:
            if self.rect.colliderect(bat.rect):collided_this_frame = True
            if self.rect.colliderect(bat.rect) and not self.collided:self.collided = True;bat_y_centre = bat.position[1] + (bat.length / 2);ball_y_centre = self.position[1] + 5;relative_intersect_y = (bat_y_centre - ball_y_centre);normalized_relative_intersect_y = relative_intersect_y / (bat.length / 2);bounce_angle = (normalized_relative_intersect_y * self.max_bat_bounce_angle);self.velocity[0] = self.velocity[0] * -1;self.velocity[1] = self.ball_speed * -math.sin(bounce_angle)
        if not collided_this_frame:self.collided = False
class Wall:
    def __init__(self, top_left, bottom_right):self.rect = pygame.Rect(top_left, (bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]));self.colour = pygame.Color("#C8C8C8")
    def render(self, screen):pygame.draw.rect(screen, self.colour, self.rect)
class PongGame:
    def __init__(self, size):self.size = size;self.background = pygame.Surface(size);self.background = self.background.convert();self.background.fill((0, 0, 0));font = pygame.font.Font(None, 24);self.score = Score(font);self.walls = [Wall((5, 5), (size[0] - 10, 10)),Wall((5, size[1] - 10), (size[0] - 10, size[1] - 5)),];self.bats = [];control_scheme_1 = ControlScheme();control_scheme_1.up = K_w;control_scheme_1.down = K_s;control_scheme_2 = ControlScheme();control_scheme_2.up = K_UP;control_scheme_2.down = K_DOWN;self.bats.append(Bat((5, int(size[1] / 2)), control_scheme_1, self.size));self.bats.append(Bat((size[0] - 10, int(size[1] / 2)), control_scheme_2, self.size));self.ball = Ball((int(size[0] / 2), int(size[1] / 2)))
    def process_event(self, event):
        for bat in self.bats:bat.process_event(event)
    def update(self, time_delta):
        for bat in self.bats:bat.update(time_delta)
        self.ball.update(time_delta, self.bats, self.walls)
        if self.ball.position[0] < 0:self.ball.reset();self.score.increase_player_2_score()
        elif self.ball.position[0] > self.size[0]:self.ball.reset();self.score.increase_player_1_score()
    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        for wall in self.walls:wall.render(surface)
        for bat in self.bats:bat.render(surface)
        self.ball.render(surface);self.score.render(surface, self.size)
class PongWindow(UIWindow):
    def __init__(self, position, ui_manager):super().__init__(pygame.Rect(position, (320, 240)),ui_manager,window_display_title="pong",object_id="#pong_window",);game_surface_size = self.get_container().get_size();self.game_surface_element = UIImage(pygame.Rect((0, 0), game_surface_size),pygame.Surface(game_surface_size).convert(),manager=ui_manager,container=self,parent_element=self,);self.pong_game = PongGame(game_surface_size);self.is_active = False
    def focus(self):self.is_active = True
    def unfocus(self):self.is_active = False
    def process_event(self, event):
        handled = super().process_event(event)
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#pong_window.#title_bar" and event.ui_element == self.title_bar:handled = True;event_data = {"user_type": "window_selected","ui_element": self,"ui_object_id": self.most_specific_combined_id,};window_selected_event = pygame.event.Event(pygame.USEREVENT, event_data);pygame.event.post(window_selected_event)
        if self.is_active:handled = self.pong_game.process_event(event)
        return handled
    def update(self, time_delta):
        if self.alive() and self.is_active:self.pong_game.update(time_delta)
        super().update(time_delta)
        self.pong_game.draw(self.game_surface_element.image)
def load(manager, params):
    pos = (50, 50)
    if params is not None and len(params) > 0:pos = params[0]
    PongWindow(pos, manager)
