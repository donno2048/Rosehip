from random import randint;import pygame;from pygame_gui.elements.ui_window import UIWindow;from pygame_gui.elements.ui_image import UIImage;import os;from math import cos, sin, tan, pi, floor, ceil, sqrt;two_pi = pi * 2;half_pi = pi * 0.5;three_half_pi = pi * 1.5;NUMBER_OF_RAYS = 320
class Maze3D:
    def __init__(self, size):self.map=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,0,0,0,0,0,0,0,0,2,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1],[1,0,1,0,1,1,1,0,1,0,2,2,0,2,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1],[1,1,1,0,1,0,0,0,1,0,2,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1],[1,0,0,0,0,0,1,1,1,0,2,0,2,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,1],[1,0,1,0,1,1,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1],[1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],[1,1,1,0,1,0,0,1,0,2,2,2,2,2,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1],[1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1],[1,1,1,1,0,1,1,1,1,0,0,2,0,2,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1],[1,0,0,1,0,1,0,1,0,1,2,0,0,2,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1],[1,1,0,1,0,1,0,0,0,2,0,0,2,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1],[1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1],[1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1],[1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1],[1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1],[1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1],[1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,2,1,0,0,0,0,1,0,0,1,0,0,1],[1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1],[1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1],[1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1],[1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1],[1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1],[1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1],[1,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1],[1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1],[1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]];app_path = os.path.dirname(os.path.abspath(__file__));assets_path = app_path + "/assets";self.size = size;self.width = self.size[0];self.height = self.size[1];self.walldark = [None];self.walllight = [None];self.walldark.append(pygame.image.load(assets_path + "/1.png").convert());self.walllight.append(pygame.image.load(assets_path + "/2.png").convert());self.walldark.append(pygame.image.load(assets_path + "/3.png").convert());self.walllight.append(pygame.image.load(assets_path + "/4.png").convert());self.textureSize = self.walldark[1].get_size();self.bg_img = pygame.image.load(assets_path + "/background.png").convert();self.bg_img = pygame.transform.scale(self.bg_img, size);self.playerX = 1.5;self.playerY = 1.5;self.playerDir = 0.0;self.playerStep = 0.05;self.angleStep = 5.0 * pi / 180.0;self.toggleTurnLeft = False;self.toggleTurnRight = False;self.toggleMoveFw = False;self.toggleMoveBw = False;self.defaultHeight = 400.0;self.numRays = NUMBER_OF_RAYS;self.viewAngle = 65 * pi / 180.0;self.rayAngleStep = self.viewAngle / (self.numRays - 1);self.columnWidth = self.width / (self.numRays - 1)
    def updatePos(self):
        if self.toggleTurnLeft:self.playerDir = (self.playerDir + self.angleStep) % (two_pi)
        if self.toggleTurnRight:self.playerDir = (self.playerDir - self.angleStep) % (two_pi)
        if self.toggleMoveFw:self.move(1)
        if self.toggleMoveBw:self.move(-1)
    def move(self, dir):
        flag = False;x, y = self.playerX, self.playerY;nx = x + self.playerStep * dir * cos(self.playerDir);ny = y - self.playerStep * dir * sin(self.playerDir)
        if self.map[floor(ny)][floor(nx)] == 0:self.playerX, self.playerY = nx, ny;return
        if floor(x) == floor(nx) and floor(y) == floor(ny) + 1:self.playerX, self.playerY = nx, ceil(ny) + 0.01;return
        if floor(x) == floor(nx) and floor(y) == floor(ny) - 1:self.playerX, self.playerY = nx, floor(ny) - 0.01;return
        if floor(x) == floor(nx) + 1 and floor(y) == floor(ny):self.playerX, self.playerY = ceil(nx) + 0.01, ny;return
        if floor(x) == floor(nx) - 1 and floor(y) == floor(ny):self.playerX, self.playerY = floor(nx) - 0.01, ny;return
        if self.map[floor(ny)][floor(x)] == 0 and self.map[floor(y)][floor(nx)] == 0:flag = True
        self.playerX, self.playerY = nx, ny
        if floor(x) == floor(nx) + 1 and floor(y) == floor(ny) + 1:
            if self.map[floor(ny)][floor(x)] != 0 or flag:self.playerY = ceil(ny) + 0.01
            if self.map[floor(y)][floor(nx)] != 0 or flag:self.playerX = ceil(nx) + 0.01
            return
        if floor(x) == floor(nx) - 1 and floor(y) == floor(ny) + 1:
            if self.map[floor(ny)][floor(x)] != 0 or flag:self.playerY = ceil(ny) + 0.01
            if self.map[floor(y)][floor(nx)] != 0 or flag:self.playerX = floor(nx) - 0.01
            return
        if floor(x) == floor(nx) - 1 and floor(y) == floor(ny) - 1:
            if self.map[floor(ny)][floor(x)] != 0 or flag:self.playerY = floor(ny) - 0.01
            if self.map[floor(y)][floor(nx)] != 0 or flag:self.playerX = floor(nx) - 0.01
            return
        if floor(x) == floor(nx) + 1 and floor(y) == floor(ny) - 1:
            if self.map[floor(ny)][floor(x)] != 0 or flag:self.playerY = floor(ny) - 0.01
            if self.map[floor(y)][floor(nx)] != 0 or flag:self.playerX = ceil(nx) + 0.01
            return
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:self.toggleTurnLeft = True;return True
            elif event.key == pygame.K_RIGHT:self.toggleTurnRight = True;return True
            elif event.key == pygame.K_UP:self.toggleMoveFw = True;return True
            elif event.key == pygame.K_DOWN:self.toggleMoveBw = True;return True
            return False
        if event.type != pygame.KEYUP:return False
        if event.key == pygame.K_LEFT:self.toggleTurnLeft = False;return True
        elif event.key == pygame.K_RIGHT:self.toggleTurnRight = False;return True
        elif event.key == pygame.K_UP:self.toggleMoveFw = False;return True
        elif event.key == pygame.K_DOWN:self.toggleMoveBw = False;return True
        return False
    def draw(self, surface):
        surface.blit(self.bg_img, (0, 0))
        for r in range(self.numRays):
            rayAngle = (self.playerDir + (self.viewAngle / 2) - r * self.rayAngleStep) % (two_pi);distH = 100000;propH = 0
            if rayAngle != half_pi and rayAngle != three_half_pi:
                if rayAngle < half_pi or rayAngle > three_half_pi:tanRayAngle = tan(rayAngle);x = ceil(self.playerX);y = self.playerY - tanRayAngle * (x - self.playerX);dir = 1
                else:tanRayAngle = tan(rayAngle);x = floor(self.playerX);y = self.playerY - tanRayAngle * (x - self.playerX);dir = -1
                while y > 0 and y < len(self.map) and self.map[floor(y)][floor(x + 0.1 * dir)] == 0:x += dir;y -= dir * tanRayAngle
                if y > 0 and y < len(self.map):wallTypeH = self.map[floor(y)][floor(x + 0.1 * dir)];distH = sqrt((self.playerX - x) * (self.playerX - x) + (self.playerY - y) * (self.playerY - y));propH = y % 1 if dir == 1 else 1 - (y % 1)
            distV = 100000;propV = 0
            if rayAngle != 0 and rayAngle != pi:
                if rayAngle < pi:arctanRayAngle = 1.0 / tan(rayAngle);y = floor(self.playerY);x = self.playerX + arctanRayAngle * (self.playerY - y);dir = -1
                else:arctanRayAngle = 1.0 / tan(rayAngle);y = ceil(self.playerY);x = self.playerX + arctanRayAngle * (self.playerY - y);dir = 1
                while x > 0 and x < len(self.map[0]) and self.map[floor(y + 0.1 * dir)][floor(x)] == 0:y += dir;x -= dir * arctanRayAngle
                if x > 0 and x < len(self.map[0]):wallTypeV = self.map[floor(y + 0.1 * dir)][floor(x)];distV = sqrt((self.playerX - x) * (self.playerX - x) + (self.playerY - y) * (self.playerY - y));propV = x % 1 if dir == -1 else 1 - (x % 1)
            if distH < distV:dist = distH;prop = propH;wallImg = self.walllight[wallTypeH]
            else:coeffLight = 1.0;dist = distV;prop = propV;wallImg = self.walldark[wallTypeV]
            z = max(0.01, dist * cos((rayAngle - self.playerDir)));calculatedHeight = self.defaultHeight * (1 / z)
            if calculatedHeight > self.height:h = self.height;cropHeight = self.height / calculatedHeight * self.textureSize[1];offset = (self.textureSize[1] - cropHeight) / 2
            else:h = calculatedHeight;cropHeight = self.textureSize[1];offset = 0
            cropArea = (self.textureSize[0] * prop, offset, 1, cropHeight);croppedImg = wallImg.subsurface(cropArea);sliceShape = (ceil(self.columnWidth), floor(h + 0.5));wallSliceImg = pygame.transform.scale(croppedImg, sliceShape);surface.blit(wallSliceImg, (r * self.columnWidth, (self.height - h) / 2))
class Maze3DWindow(UIWindow):
    def __init__(self, position, ui_manager):super().__init__(pygame.Rect(position, (640, 480)),ui_manager,window_display_title="Maze 3D",object_id="#maze3d_window",);game_surface_size = self.get_container().get_size();self.game_surface_element = UIImage(pygame.Rect((0, 0), game_surface_size),pygame.Surface(game_surface_size).convert(),manager=ui_manager,container=self,parent_element=self,);self.maze3d = Maze3D(game_surface_size)
    def process_event(self, event):super().process_event(event);return self.maze3d.process_event(event)
    def update(self, time_delta):super().update(time_delta);self.maze3d.updatePos();self.maze3d.draw(self.game_surface_element.image)
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    Maze3DWindow(pos, manager)
