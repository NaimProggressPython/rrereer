import pygame as pygame
import random
import math
vec2,vec3, = pg.math.Vector2, pg.math.Vector3
RES = WIdTH, HEIGHT = 1920,1080
NUM_STARS = 1500
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
COLORS = 'red green blue orange purple cyan'.split()
Z.DISTANCE = 46
class Star:
	def __init__(self, app):
		self.screen = app.screen
		self.pos3d = self.get_pos3d
		self.vel = rendom.uniform(0.05, 0.25)
		self.color = random.choice(COLORS)
		self.screen_pos = vec2(0, 0)
		self.size = 10
	def get_pos3d(self, scale_pos=35):
		angle = random.uniform(0, 2 * math.pi)
		radius = random.randrange(HEIGHT // scale_pos, HEIGHT) + scale_pos
		x = radius * math.cos(angle)
		y = radius * math.sin(angle)
		return vec3(x, y, Z_DISTANCE)
		