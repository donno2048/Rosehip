from random import randint;import pygame,random;from pygame_gui.elements.ui_window import UIWindow;from pygame_gui.elements.ui_image import UIImage;import os;from math import cos, sin, tan, pi, floor, ceil, sqrt;two_pi = pi * 2;half_pi = pi * 0.5;three_half_pi = pi * 1.5;NUMBER_OF_RAYS = 320
class DisjointSet:
	class Element:
		def __init__(self, key):self.key = key;self.parent = self;self.rank = 0
		def __eq__(self, other):return self.key ==  other.key
		def __ne__(self, other):return self.key != other.key
	def __init__(self):self.tree = {}
	def make_set(self, key):
		e = self.Element(key)
		if not key in self.tree.keys():self.tree[key] = e
	def find(self, key):
		if key in self.tree.keys():element = self.tree[key]
		if key in self.tree.keys() and element.parent != element:element.parent  = self.find(element.parent.key)
		if key in self.tree.keys():return element.parent
	def union(self, element_a, element_b):
		root_a = self.find(element_a.key);root_b = self.find(element_b.key)
		if root_a != root_b and root_a.rank < root_b.rank:root_a.parent = root_b
		elif root_a != root_b and root_a.rank > root_b.rank:root_b.parent = root_a
		elif root_a != root_b:root_b.parent = root_a;root_a.rank+=1
class Maze:
	def __init__(self, width):
		self.width = width;self.height = width;self.seed = random.random()*10000;self.grid = [[(width*row + col) for row in range(0,width)] for col in range(0, width)];self.portals = {};self.kruskalize()
	def __str__(self):
		s=''
		for i in range(self.width):s+=str(random.randint(1,2))+str(random.randint(1,2))
		s+=str(random.randint(1,2))+'\n'
		for row in range(0,self.height):
			s+=str(random.randint(1,2))+'0'
			for col in range(1, self.width):s+='0'*(self.grid[col-1][row] in self.portals[self.grid[col][row]])+str(random.randint(1,2))*(self.grid[col-1][row] not in self.portals[self.grid[col][row]])+'0'
			s+=str(random.randint(1,2))+'\n'
			for col in range(0, self.width):key = self.grid[col][row];s+=str(random.randint(1,2))+'0'*(row+1 < self.height and self.grid[col][row+1] in self.portals[key])+str(random.randint(1,2))*(row+1 >= self.height or self.grid[col][row+1] not in self.portals[key])
			s+=str(random.randint(1,2)) +'\n'
		return s
	def kruskalize(self):
		edges_ordered = [ ]
		for row in range(0, self.height):
			for col in range(0, self.width):
				cell = (col, row);left_cell = (col-1, row);down_cell = (col, row-1);near = []
				if col > 0:near.append((left_cell, cell))
				if row > 0:near.append( (down_cell, cell))
				edges_ordered.extend(near)
		random.seed(self.seed);edges = []
		while len(edges_ordered) > 0:edges.append(edges_ordered.pop(random.randint(0,len(edges_ordered))-1))
		disjoint_set = DisjointSet()
		for row in range(0, self.height):
			for col  in range(0,self.width):key = self.grid[col][row];disjoint_set.make_set(key);self.portals[key] = {}
		edge_count = 0;key_count = self.grid[self.width-1][self.height-1]
		while edge_count < key_count:
			edge = edges.pop();key_a = self.grid[edge[0][0]][edge[0][1]];key_b = self.grid[edge[1][0]][edge[1][1]];set_a = disjoint_set.find(key_a);set_b = disjoint_set.find(key_b)
			if set_a != set_b:edge_count+=1;self.portals[key_a][key_b] = True;self.portals[key_b][key_a] = True;disjoint_set.union(set_a, set_b)
	def list(self):return [list(i) for i in str(self).split('\n')][:-1]
class Maze3D:
    def __init__(self, size):self.map=Maze(42).list();app_path = os.path.dirname(os.path.abspath(__file__));assets_path = app_path + "/assets";self.size = size;self.width = self.size[0];self.height = self.size[1];self.walldark = [None];self.walllight = [None];self.walldark.append(pygame.image.load(assets_path + "/1.png").convert());self.walllight.append(pygame.image.load(assets_path + "/2.png").convert());self.walldark.append(pygame.image.load(assets_path + "/3.png").convert());self.walllight.append(pygame.image.load(assets_path + "/4.png").convert());self.textureSize = self.walldark[1].get_size();self.bg_img = pygame.image.load(assets_path + "/background.png").convert();self.bg_img = pygame.transform.scale(self.bg_img, size);self.playerX = 1.5;self.playerY = 1.5;self.playerDir = 0.0;self.playerStep = 0.05;self.angleStep = 5.0 * pi / 180.0;self.toggleTurnLeft = False;self.toggleTurnRight = False;self.toggleMoveFw = False;self.toggleMoveBw = False;self.defaultHeight = 400.0;self.numRays = NUMBER_OF_RAYS;self.viewAngle = 65 * pi / 180.0;self.rayAngleStep = self.viewAngle / (self.numRays - 1);self.columnWidth = self.width / (self.numRays - 1)
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
